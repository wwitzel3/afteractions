"""
This file maps out the CCP datadump to work with afteractions. I wanted to leave the CCP part of the
data for this killboard unmolested and generate any helper tables pragmatically to allow for very
simple updates when CCP makes any schema changes.

The invtypes table contains all the information for Ships, Modules, Ammo, etc.. it has been mapped here
as Item. This will be used with some helper class methods for all item lookups.

"""
import os
from pylons import config
from afteractions.model import meta

from sqlalchemy import Column, ForeignKey, select, and_, func
from sqlalchemy import Integer, String, Boolean, DateTime
from sqlalchemy.orm import column_property, relation, dynamic_loader

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(metadata=meta.metadata)

class TypeEffect(Base):
    """The effect ID of an determines its slot location. Thanks to <INSERT GUY WHO HELPED> for the info.

        11   - Low Slot
        12   - High Slot
        13   - Medium Slot
        2663 - Rig Slot
        3772 - Subsystem Slot
        
    """
    slots = {11:'Low Slot', 12:'High Slot', 13:'Medium Slot', 2663:'Rig Slot', 3772:'Subsystem Slot'}
    
    __tablename__ = 'dgmTypeEffects'
    type_id = Column('typeid', Integer, ForeignKey('invTypes.typeID'), primary_key=True)
    effect_id = Column('effectid', Integer, primary_key=True)
    
class Item(Base):
    __tablename__ = 'invTypes'
    id = Column('typeid', Integer, primary_key=True)
    name = Column('typename', String, index=True)
    group_id = Column('groupid', Integer, ForeignKey('invGroups.groupID'))
    graphic_id = Column('graphicid', Integer)
    
    effects = dynamic_loader(TypeEffect, primaryjoin=id==TypeEffect.type_id)
    
    @classmethod
    def locate(cls, name):
        item = meta.Session.query(cls).filter_by(name=name).first()
        if item:
            return item
        else:
            print 'Unable to locate %s, using Unknown' % (name)
            item = meta.Session.query(cls).filter_by(id=99999).one()
            return item
    
    def icon(self, size='32_32'):
        return os.path.join(config.get('images'), size, '%s.png' % (self.graphic_id))
    
class Flag(Base):
    __tablename__ = 'invflags'
    id = Column('flagid', Integer, primary_key=True)
    name = Column('flagname', String)
    text = Column('flagtext', String)

class Group(Base):
    __tablename__ = 'invGroups'
    id = Column('groupid', Integer, primary_key=True)
    name = Column('groupname', String)
    
    category_id = Column('categoryid', Integer,
            ForeignKey('invCategories.categoryID'))
    
class Category(Base):
    __tablename__ = 'invCategories'
    id = Column('categoryid', Integer, primary_key=True)
    name = Column('categoryname', String)

class Region(Base):
    __tablename__ = 'mapRegions'
    id = Column('regionid', Integer, primary_key=True)
    name = Column('regionname', String)
    
class Constellation(Base):
    __tablename__ = 'mapConstellations'
    id = Column('constellationid', Integer, primary_key=True)
    name = Column('constellationname', String)
    
    region_id = Column('regionid', Integer, ForeignKey('mapRegions.regionID'))
    
class System(Base):
    __tablename__ = 'mapSolarSystems'
    id = Column('solarsystemid', Integer, primary_key=True)
    name = Column('solarsystemname', String)
    
    region_id = Column('regionid', Integer, ForeignKey('mapRegions.regionID'))
    constellation_id = Column('constellationid', Integer,
            ForeignKey('mapConstellations.constellationID'))
    
    @classmethod
    def locate(cls, name):
        return meta.Session.query(cls).filter_by(name=name).one()
    
