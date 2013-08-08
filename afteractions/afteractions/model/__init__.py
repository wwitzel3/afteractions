"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import orm

from pylons import config
import os

from datetime import datetime

from afteractions.lib.helpers import random_string, salted_hash

from afteractions.model import meta
from afteractions.model.ccp import Item, Group, Region, System, TypeEffect

from sqlalchemy import Column, ForeignKey, select, and_, func
from sqlalchemy import Integer, String, Boolean, DateTime, Float
from sqlalchemy.orm import column_property, relation, dynamic_loader

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(metadata=meta.metadata)

def init_model(engine):
    meta.Session.configure(bind=engine)
    meta.engine = engine
    
class Pilot(Base):
    __tablename__ = 'aa_pilot'
    id = Column('id', Integer, primary_key=True)
    eve_id = Column('eve_id', Integer, default=0)
    name = Column('name', String)
    
    corp_id = Column('corp_id', Integer, ForeignKey('aa_corp.id'))
        
    def __init__(self, name, corp):
        self.name = name
        self.corp = corp
    @classmethod
    def create(cls, name, corp):
        pilot = meta.Session.query(cls).filter_by(name=name).first()
        if pilot:
            pilot.corp = corp
            return pilot
        else:
            return cls(name, corp)
    def get_corp_id(self):
        return self.corp_id
    
    def get_alliance_id(self):
        if self.corp.alliance:
            return self.corp.alliance.id
        else:
            return 0
        
    def has_portrait(self):
        try:
            portrait_path = os.path.join(config.get('portraits'), 'portraits', '256', str(self.eve_id) + '.jpeg')
        except TypeError, e:
            return False

        portrait = os.path.isfile(portrait_path)
        if self.eve_id and portrait:
            return True
        else:
            return False
        
    def __cmp__(self, other):
        if self.id == other.id or self.eve_id == other.eve_id:
            return 0
        elif self.id < other.id or self.eve_id < other.eve_id:
            return -1
        elif self.id > other.id or self.eve_id > other.eve_id:
            return 1

class Corp(Base):
    __tablename__ = 'aa_corp'
    id = Column('id', Integer, primary_key=True)
    eve_id = Column('eve_id', Integer)
    name = Column('name', String, index=True, unique=True)
    pilots = relation(Pilot)
    
    alliance_id = Column('alliance_id', Integer, ForeignKey('aa_alliance.id'))
    
    def __init__(self, name, alliance=None):
        self.name = name
        if alliance:
            self.alliance = alliance
    @classmethod
    def create(cls, name):
        corp = meta.Session.query(cls).filter_by(name=name).first()
        if corp:
            return corp
        else:
            return cls(name)

class Alliance(Base):
    __tablename__ = 'aa_alliance'
    id = Column('id', Integer, primary_key=True)
    eve_id = Column('eve_id', Integer)
    name = Column('name', String)
    corps = relation(Corp)
    
    def __init__(self, name):
        self.name = name
    @classmethod
    def create(cls, name):
        corp = meta.Session.query(cls).filter_by(name=name).first()
        if corp:
            return corp
        else:
            return cls(name)

class Comment(Base):
    __tablename__ = 'aa_comment'
    id = Column('id', Integer, primary_key=True)
    kill_id = Column('kill_id', Integer, ForeignKey('aa_kill.id'), primary_key=True)
    ipaddress = Column('ipaddress', String)
    name = Column('name', String)
    
class Involved(Base):
    __tablename__ = 'aa_kill_involved'
    kill_id = Column('kill_id', Integer, ForeignKey('aa_kill.id'), primary_key=True)
    pilot_id = Column('pilot_id', Integer, ForeignKey('aa_pilot.id'), primary_key=True)
    corp_id = Column('corp_id', Integer, ForeignKey('aa_corp.id'))
    alliance_id = Column('alliance_id', Integer, ForeignKey('aa_alliance.id'))
    ship_id = Column('ship_id', Integer, ForeignKey('invTypes.typeID'))
    module_id = Column('module_id', Integer, ForeignKey('invTypes.typeID'))
    
    damage = Column('damage', Integer)
    final = Column('final', Boolean, default=False)
    
    pilot = relation(Pilot)
    ship = relation(Item, primaryjoin=ship_id==Item.id)
    module = relation(Item, primaryjoin=module_id==Item.id)
    corp = relation(Corp)
    alliance = relation(Alliance)
    
    def __init__(self, pilot, ship, module, damage, final):
        self.pilot = pilot
        self.corp = pilot.corp
        if pilot.corp.alliance:
            self.alliance = pilot.corp.alliance
        self.ship = ship
        self.module = module
        self.damage = damage
        self.final = final
        
class Inventory(Base):
    __tablename__ = 'aa_kill_inventory'
    id = Column('id', Integer, primary_key=True)
    
    kill_id = Column('kill_id', Integer, ForeignKey('aa_kill.id'), index=True)
    type_id = Column('type_id', Integer, ForeignKey('invTypes.typeID'), index=True)
    flag_id = Column('flag_id', Integer, ForeignKey('invFlags.flagID'))
    
    order = Column('order', Integer)
    slot = Column('slot', Integer)
    qty = Column('qty', Integer)
    
    cargo = Column('cargo', Boolean, default=False, primary_key=True)
    drone = Column('drone', Boolean, default=False, primary_key=True)
    dropped = Column('dropped', Boolean, default=False, primary_key=True)
    
    item = relation(Item, primaryjoin=type_id==Item.id)
    
    def __init__(self, item, qty, order=0, flag_id=0, cargo=False, drone=False, dropped=False):
        self.item = item
        self.order = order
        self.qty = qty
        self.flag_id = flag_id
        
        self.dropped = dropped
        self.drone = drone
        self.cargo = cargo
        
        slot = item.effects.filter(TypeEffect.effect_id.in_(TypeEffect.slots.keys())).first()
        if slot:
            self.slot = slot.effect_id
        
class Kill(Base):
    __tablename__ = 'aa_kill'
    id = Column('id', Integer, primary_key=True)
    eve_id = Column('eve_id', Integer)
    
    pilot_id = Column('pilot_id', Integer, ForeignKey('aa_pilot.id'))
    corp_id = Column('corp_id', Integer, ForeignKey('aa_corp.id'))
    alliance_id = Column('alliance_id', Integer, ForeignKey('aa_alliance.id'))
    ship_id = Column('ship_id', Integer, ForeignKey('invTypes.typeID'))
    system_id = Column('system_id', Integer,
            ForeignKey('mapSolarSystems.solarsystemID'))
    
    damage = Column('damage', Integer)
    timestamp = Column('timestamp', DateTime)
    
    inventory = dynamic_loader(Inventory, cascade='all,delete-orphan')
    involved = dynamic_loader(Involved, cascade='all,delete-orphan')
    comments = dynamic_loader(Comment, cascade='all,delete-orphan')
    
    pilot = relation(Pilot)
    ship = relation(Item, primaryjoin=ship_id==Item.id)
    corp = relation(Corp)
    alliance = relation(Alliance)
    system = relation(System)
    
    def __init__(self, pilot, ship, system, timestamp, damage, eve_id=0):
        self.eve_id = eve_id
        self.pilot = pilot
        self.corp = pilot.corp
        if pilot.corp.alliance:
            self.alliance = pilot.corp.alliance
        self.ship = ship
        self.system = system
        self.damage = damage
        self.timestamp = timestamp
    
    @classmethod
    def locate(cls, pilot, ship, system, timestamp):
        kill = meta.Session.query(cls).\
                filter_by(pilot=pilot).filter_by(ship=ship).\
                filter_by(system=system).filter_by(timestamp=timestamp).first()
        return kill
    
    @classmethod
    def create(cls, pilot, ship, system, timestamp, damage, eve_id=0):
        kill = meta.Session.query(cls).\
                filter_by(pilot=pilot).filter_by(ship=ship).\
                filter_by(system=system).filter_by(timestamp=timestamp).first()
        if kill:
            return kill
        else:
            return cls(pilot, ship, system, timestamp, damage, eve_id)

    @classmethod
    def by_class_for_date_range(cls, start_date=datetime.now(), end_date=datetime.now()):
        '''select id, name, sum(killed) as killed, sum(lost) as lost from
            (
                (select count(*) as killed, 0 as lost, groupname as name, invgroups.groupid as id from invgroups
                join invtypes on invtypes.groupid = invgroups.groupid
                join aa_kill on aa_kill.ship_id = invtypes.typeid
                where aa_kill.alliance_id != 3 and aa_kill.corp_id != 0
                group by groupname, invgroups.groupid)
            
                UNION ALL

                (select 0 as killed, count(*) as lost, groupname as name, invgroups.groupid as id from invgroups
                join invtypes on invtypes.groupid = invgroups.groupid
                join aa_kill on aa_kill.ship_id = invtypes.typeid
                where aa_kill.alliance_id = 3 or aa_kill.corp_id = 0
                group by groupname, invgroups.groupid)
                
                UNION ALL
            
                (select 0 as killed, 0 as lost, groupname as name, groupid as id from invgroups where categoryid = 6 group by groupname, groupid)
            ) as ShipClassTable
            group by ShipClassTable.name, ShipClassTable.id
            order by ShipClassTable.name'''

        killed_select = sa.select([sa.func.count('*').label('killed'), sa.literal(0).label('lost'), Group.name.label('name'), Group.id.label('id')],
                                  sa.and_(Group.category_id == 6, Kill.alliance_id != 3, Kill.corp_id != 0),
                                  [sa.join(Item.__table__, Kill.__table__, Kill.ship_id == Item.id).join(Group.__table__, Group.id == Item.group_id)],
                                  group_by=[Group.name, Group.id])
        lost_select = sa.select([sa.literal(0).label('killed'), sa.func.count('*').label('lost'), Group.name.label('name'), Group.id.label('id')],
                                sa.and_(Group.category_id == 6, sa.or_(Kill.alliance_id == 3, Kill.corp_id == 0)),
                                [sa.join(Item.__table__, Kill.__table__, Kill.ship_id == Item.id).join(Group.__table__, Group.id == Item.group_id)],
                                group_by=[Group.name, Group.id])
        group_select = sa.select([sa.literal(0).label('killed'), sa.literal(0).label('lost'), Group.name.label('name'), Group.id.label('id')],
                                 Group.category_id == 6,
                                 group_by=[Group.name, Group.id])
        
        ship_class_union = sa.union_all(killed_select, lost_select, group_select).alias('aa_ship_class_tbl')
        
        ship_class_select = sa.select([ship_class_union.c.id, ship_class_union.c.name,
                                       sa.func.sum(ship_class_union.c.killed).label('killed'),
                                       sa.func.sum(ship_class_union.c.lost).label('lost')])\
                                .group_by(ship_class_union.c.name, ship_class_union.c.id)\
                                .order_by(ship_class_union.c.name)

        results = meta.engine.execute(ship_class_select)
        return results.fetchall()
    
    def finalblow(self):
        return self.involved.filter_by(final=True).one()

    def fitting(self, size='32_32'):
        """This method returns a nested list, fixed position, representation of kills
        fitting. It can be used for fitting tools or to easily render to fitting displays.
        It uses magic numbers to determine a modules location. It also will look at the qty
        and properly add item * qty to the list.
        
        It looks at the drone and cargo booleans to determine if items were not fit on the ship.
        """
        fitting = {'high':[[None,None]] * 8, 'med':[[None,None]] * 8,
                   'low':[[None,None]] * 8, 'rig':[[None,None]] * 3,
                   'subsystem':[[None,None]] * 5}
        
        def insert_at_none(item, key):
            for x in xrange(item.qty):
                for i in xrange(len(fitting[key])):
                    if fitting[key][i] == [None,None]:
                        fitting[key][i] = [item.item.name, item.item.icon(size=size)]
                        break

        for item in self.inventory:
            if item.cargo or item.drone:
                continue
            elif item.slot == 12:
                insert_at_none(item, 'high')
            elif item.slot == 13:
                insert_at_none(item, 'med')
            elif item.slot == 11:
                insert_at_none(item, 'low')
            elif item.slot == 2663:
                insert_at_none(item, 'rig')
            elif item.slot == 3772:
                insert_at_none(item, 'subsystem')

        return fitting
    
class Price(Base):
    __tablename__ = 'aa_price'
    type_id = Column('type_id', Integer, ForeignKey('invTypes."typeID"'), primary_key=True)
    price = Column('price', Float)

class CampaignMatrix(Base):
    __tablename__ = 'aa_campaign_matrix'
    campaign_id = Column('campaign_id', Integer, ForeignKey('aa_campaign.id'), primary_key=True)
    
    corp_id = Column('corp_id', Integer, ForeignKey('aa_corp.id'))
    alliance_id = Column('alliance_id', Integer, ForeignKey('aa_alliance.id'))
    
    region_id = Column('region_id', Integer, ForeignKey('mapRegions.regionID'))
    constellation_id = Column('constellation_id', Integer,
            ForeignKey('mapConstellations.constellationID'))
    system_id = Column('system_id', Integer,
            ForeignKey('mapSolarSystems.solarsystemID'))
    
class Campaign(Base):
    __tablename__ = 'aa_campaign'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    start_date = Column('start_date', DateTime, default=datetime.now())
    end_date = Column('end_date', DateTime)
    
    matrix = relation(CampaignMatrix, cascade='all,delete-orphan')
    report = Column('report', String)
    video = Column('video', String)

class Config(Base):
    '''See the README.txt for the set of available configuration options, not all of them
    maybe presented through the administrative interface. You will be able to set these manually
    through the administration interface if there is not specific UI forms for setting certain values.
    
    Many of these values will be set during installation and will have to be manually changed in the DB
    if you wanted to alter them at a later date.
    
    If a value provides a salt, then it will be hashed and a check only value using that salt.
    '''
    __tablename__ = 'aa_config'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String, index=True, nullable=False)
    value = Column('value', String)
    salt = Column('salt', String)
    
    @classmethod
    def set(cls, name, value, salt=False):
        config = meta.Session.query(cls).filter_by(name=name).first()
        if config:
            if salt:
                config.salt = random_string()
                config.value = salted_hash(value, config.salt)
            else:
                config.value = value
        else:
            config = cls()
            config.name = name
            if salt:
                config.salt = random_string()
                config.value = salted_hash(value, config.salt)
            else:
                config.value = value
            meta.Session.add(config)

### Down up relations
Pilot.corp = relation(Corp, primaryjoin=Pilot.corp_id==Corp.id)
Corp.alliance = relation(Alliance, primaryjoin=Corp.alliance_id==Alliance.id)
Item.price = relation(Price, primaryjoin=Price.type_id==Item.id, uselist=False)
