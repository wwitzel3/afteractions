from datetime import datetime

from afteractions.model import meta

from afteractions.model import Pilot, Corp, Alliance, Kill, Involved, Inventory
from afteractions.model.ccp import System, Item

class TxtKill(object):
    def __init__(self, ccp_kill_txt):
        self.kill = None
        
        self.timestamp = None
        self.victim = None
        self.involved = None
        self.destroyed = None
        self.dropped = None
        
        self.kill_txt = ccp_kill_txt.replace('\r','')
        self.kill_list = self.kill_txt.split('\n')
        
        self.pos = 0
        
        self._parse()
        self.kill_baby_batter()
        
    @classmethod
    def parse(cls, ccp_kill_txt):
        txt_kill = cls(ccp_kill_txt)
        return txt_kill.kill
    
    def kill_baby_batter(self):
        '''This takes all the bull shit dictionaries and shit and makes kill, inventory, and involved
        objects out of all the shit and commits it to the database.
        
        This will throw some exceptions if it can't find items or ships and what not. It will use existing
        Pilot, Alliance, Corp entries to avoid duplicates and will just return if a kill already exists'''
        try:
            timestamp = datetime.strptime(self.timestamp, '%Y.%m.%d %H:%M:%S')
        except ValueError, e:
            timestamp = datetime.strptime(self.timestamp, '%Y.%m.%d %H:%M')

        corp = Corp.create(self.victim['corp'])
        if (self.victim['alliance']):
            corp.alliance = Alliance.create(self.victim['alliance'])
        pilot = Pilot.create(self.victim['name'], corp)
        meta.Session.add(pilot)
        meta.Session.commit()
        
        ship = Item.locate(self.victim['ship'])
        damage = self.victim['damage']
        system = System.locate(self.victim['system'])
                
        kill = Kill.locate(pilot, ship, system, timestamp)
        if kill:
            self.kill = kill
            return
        
        self.kill = Kill.create(pilot, ship, system, timestamp, damage)
        
        for attacker in self.involved:
            corp = Corp.create(attacker['corp'])
            if (attacker['alliance']):
                corp.alliance = Alliance.create(attacker['alliance'])
            pilot = Pilot.create(attacker['name'], corp)
            ship = Item.locate(attacker['ship'])
            weapon = Item.locate(attacker['weapon'])
            damage = attacker['damage']
            final = attacker['final']
            meta.Session.add(pilot)
            self.kill.involved.append(Involved(pilot, ship, weapon, damage, final))
        
        self._add_inventory(self.destroyed['fit'], False, False, False)
        self._add_inventory(self.dropped['fit'], True, False, False)
        self._add_inventory(self.dropped['cargo'], True, True, False)
        self._add_inventory(self.destroyed['cargo'], False, True, False)
        self._add_inventory(self.dropped['drone'], True, False, True)
        self._add_inventory(self.destroyed['drone'], False, False, True)
                         
        meta.Session.add(self.kill)
        meta.Session.commit()
    
    def _add_inventory(self, items, dropped=False, cargo=False, drone=False):
        for module in items:
            item = Item.locate(module)
            self.kill.inventory.append(Inventory(item, items[module]['qty'], dropped=dropped, cargo=cargo, drone=drone))
    
    def _parse(self):
        '''I don't really like this fixed position, static content
        dependent parsing shit, but I don't really see a better option
        and honestly CCP doesn't change up their kill format too much.
        
        First line is always the date, followed by the vic in question.
        Once you read the Involved parties: you are parsing pilots of the kill.
        
        Then you get to destroyed and dropped items. This is a little more fun
        as you basically have to use tokens in the string to determine if the
        items were in the cargo, drone, or fit.
        
        You also need to track your own qty at this point. Slot items will be listed
        individually, matching items like rigs can potentially have a Qty as well as
        items in the cargo hold, drone bay, and loaded charges.
        '''                
        self.timestamp = self.kill_list[self.pos]
        self.pos = 1
        
        self.victim = self.pilot_to_dict(self.capture_to_match(self.pos, 'Involved parties:'))
        self.involved = [self.pilot_to_dict(pilot) for pilot in self.involved_to_pilots(self.capture_to_match(self.pos+1, 'Destroyed items:'))]
        
        self.destroyed = self.items_to_dict(self.capture_to_match(self.pos+1, 'Dropped items:'))
        self.dropped = self.items_to_dict(self.capture_to_match(self.pos+1, None))

    def capture_to_match(self, start_pos, token):
        if token == None:
            return self.kill_list[start_pos:]
        _tmp = []
        for pos,line in enumerate(self.kill_list[start_pos:]):
            if line.find(token) == -1:
                _tmp.append(line)
            else:
                self.pos = pos + start_pos
                break
        return _tmp
    
    def involved_to_pilots(self, involved):
        involved_pilots, pilot = [], []
        for line in involved:
            if line == '':
                if len(pilot) > 0:
                    involved_pilots.append(pilot)
                pilot = []
                continue
            else:
                pilot.append(line)
        return involved_pilots
    
    def items_to_dict(self, items):
        items_dict = {}
        cargo_dict = {}
        drone_dict = {}
        
        check = lambda f: f > -1
        
        for item in items:
            if item == '':
                continue
            has_qty = check(item.find('Qty:'))
            is_cargo = check(item.find('(Cargo)'))
            is_drone = check(item.find('(Drone Bay)'))
        
            if has_qty == False and is_cargo == False and is_drone == False:
                if (items_dict.get(item)):
                    items_dict[item]['qty'] += 1
                else:
                    items_dict[item] = {'qty':1}
            elif has_qty == True and is_cargo == False and is_drone == False:
                name,qty = item.split(',')
                qty = int(qty.split('Qty: ')[1])
                if (items_dict.get(name)):
                    items_dict[name]['qty'] += qty
                else:
                    items_dict[name] = {'qty':qty}
            elif has_qty == False and is_cargo == True:
                name = item.split(' (Cargo)')[0]
                if (cargo_dict.get(name)):
                    cargo_dict[name]['qty'] += 1
                else:
                    cargo_dict[name] = {'qty':1}
            elif has_qty == True and is_cargo == True:
                name,qty = item.split(',')
                qty = int(qty.split(' (')[0].split('Qty: ')[1])
                if (cargo_dict.get(name)):
                    cargo_dict[name]['qty'] += qty
                else:
                    cargo_dict[name] = {'qty':qty}
            elif has_qty == False and is_drone == True:
                name = item.split(' (Drone Bay)')[0]
                if (drone_dict.get(name)):
                    drone_dict[name]['qty'] += 1
                else:
                    drone_dict[name] = {'qty':1}
            elif has_qty == True and is_drone == True:
                name,qty = item.split(',')
                qty = int(qty.split(' (')[0].split('Qty: ')[1])
                if (drone_dict.get(name)):
                    drone_dict[name]['qty'] += qty
                else:
                    drone_dict[name] = {'qty':qty}
        return {'fit':items_dict, 'cargo':cargo_dict, 'drone':drone_dict}
    
    def pilot_to_dict(self, pilot):
        '''This takes a list of CCP kill strings that represent a pilot.
        Can be either a vic or an involved. The result is a dict that can
        be used to lookup and then create any Alliance, Corp, Pilot objects
        that are needed.'''
        pilot_dict = {'name':None, 'corp':None, 'alliance':None, 'system':None,
                      'ship':None, 'weapon':None, 'damage':0, 'final':False}
        
        for line in pilot:
            if line.find('Victim:') > -1 or line.find('Name:') > -1:
                if line.find(' / ') > -1:
                    pilot_dict['name'], pilot_dict['corp'] = line.split(': ')[1].split(' / ')
                elif line.find('(laid the final blow)') > -1:
                    pilot_dict['final'] = True
                    pilot_dict['name'] = (line.split(': ')[1].split('(')[0])
                else:
                    pilot_dict['name'] = line.split(': ')[1]
            elif line.find('Corp:') > -1:
                pilot_dict['corp'] = line.split(': ')[1]
            elif line.find('Alliance:') > -1:
                pilot_dict['alliance'] = line.split(': ')[1]
            elif line.find('Damage Done:') > -1 or line.find('Damage Taken:') > -1:
                pilot_dict['damage'] = int(line.split(': ')[1])
            elif line.find('Ship:') > -1 or line.find('Destroyed:') > -1:
                pilot_dict['ship'] = line.split(': ')[1]
            elif line.find('Weapon:') > -1:
                pilot_dict['weapon'] = line.split(': ')[1]
            elif line.find('System:') > -1:
                pilot_dict['system'] = line.split(': ')[1]
        return pilot_dict