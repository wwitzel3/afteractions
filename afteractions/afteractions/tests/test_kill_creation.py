from afteractions.model.ccp import System, Item
from afteractions.model import meta, Kill, Involved, Inventory, Corp, Alliance, Pilot

from datetime import datetime

class TestKillCreation(object):
    def setUp(self):
        self.corp = Corp.create("Clown Punchers.")
        self.pilot = Pilot.create("Quebnaric Deile", self.corp)
        
        self.system = meta.Session.query(System).filter_by(name='Hemin').one()
        self.ship = meta.Session.query(Item).filter_by(name='Stabber').one()
        
        self.damage = 2000
        self.timestamp = datetime.now()
        
        self.kill_corp = Corp.create("Alpha Corp")
        self.kill_pilot = Pilot.create("n00b", self.kill_corp)
        self.kill_ship = meta.Session.query(Item).filter_by(name="Vagabond").one()
        self.kill_module = meta.Session.query(Item).filter_by(name="220mm Vulcan AutoCannon II").one()
        self.kill_damage = 2000
        self.kill_finalblow = True
        
    def test_kill_creation(self):
        kill = Kill.create(self.pilot, self.ship, self.system, self.timestamp, self.damage)
        assert kill
        
    def test_kill_inventory(self):
        kill = Kill.create(self.pilot, self.ship, self.system, self.timestamp, self.damage)
        inventory = Inventory(self.kill_module, 1, dropped=True)
        kill.inventory.append(inventory)
        meta.Session.add(kill)
        meta.Session.commit()
        assert kill
        meta.Session.delete(kill)
        meta.Session.commit()
        
    def test_kill_involved(self):
        kill = Kill.create(self.pilot, self.ship, self.system, self.timestamp, self.damage)
        involved = Involved(self.kill_pilot, self.kill_ship, self.kill_module, self.kill_damage, self.kill_finalblow)
        kill.involved.append(involved)
        
        assert kill
        meta.Session.add(kill)
        meta.Session.commit()
        
        assert kill.finalblow().pilot == self.kill_pilot
        self.kill_pilot.corp = Corp.create("Beta Corp")
        assert kill.involved[0].corp == self.kill_corp
        meta.Session.delete(kill)
        meta.Session.commit()
        