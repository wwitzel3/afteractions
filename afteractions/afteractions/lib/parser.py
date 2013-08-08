from datetime import datetime

from afteractions.model import meta
from afteractions.model import Kill, KillInvolved, KillItem
from afteractions.lib.pilot import new_pilot

def new_kill(kill):
    new_pilot(kill.victim)
    
    kill_q = meta.Session.query(Kill)
    kill_r = kill_q.filter_by(external_id=kill.killID).first()
    if not kill_r:
        kill_r = kill_q.filter_by(pilot_id=kill.victim.characterID).\
                      filter_by(timestamp=datetime.fromtimestamp(kill.killTime)).\
                      filter_by(system_id=kill.solarSystemID).first()
        if not kill_r:
            kill_d = Kill(external_id=kill.killID,
                          pilot_id=kill.victim.characterID,
                          corporation_id=kill.victim.corporationID,
                          alliance_id=kill.victim.allianceID,
                          system_id=kill.solarSystemID,
                          ship_id=kill.victim.shipTypeID,
                          damage=kill.victim.damageTaken,
                          timestamp=datetime.fromtimestamp(kill.killTime))
            meta.Session.add(kill_d)
            
            for attacker in kill.attackers:
                pid, cid, aid = new_pilot(attacker)
                if attacker.finalBlow:
                    kill_d.finalblow_pilot_id = pid if pid else cid
                    kill_d.finalblow_corp_id = cid
                    kill_d.finalblow_alliance_id = aid
                
                kill_d.involved.append(KillInvolved(kill_id=kill_d.id,
                                              pilot_id=attacker.characterID,
                                              ship_id=attacker.shipTypeID,
                                              module_id=attacker.weaponTypeID,
                                              damage=attacker.damageDone,
                                              finalblow=attacker.finalBlow))
            for item in kill.items:
                kill_d.items.append(KillItem(kill_id=kill_d.id,
                                             type_id=item.typeID,
                                             flag=item.flag,
                                             qty_destroyed=item.qtyDestroyed,
                                             qty_dropped=item.qtyDropped))
    meta.Session.flush()
    return kill_r
