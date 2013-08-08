
from afteractions.lib.txtkill import TxtKill
from datetime import datetime

class TestTxtKillParser(object):
    def setUp(self):
        pass
    
    def test_parse_txt_kill(self):
        kill = TxtKill(ccp_kill_txt)
        assert kill
        
ccp_kill_txt = '''2009.05.14 00:00

Victim: Bizazedo
Corp: No Trademark
Alliance: None
Faction: NONE
Destroyed: Tengu
System: Y9G-KS
Security: 0.0
Damage Taken: 28259

Involved parties:

Name: Tolarus
Security: 5.0
Corp: Clown Punchers.
Alliance: Clown Punchers Syndicate
Faction: NONE
Ship: Dominix
Weapon: Bouncer II
Damage Done: 7240

Name: Quebnaric Deile
Security: -1.7
Corp: Clown Punchers.
Alliance: Clown Punchers Syndicate
Faction: NONE
Ship: Dominix
Weapon: Bouncer II
Damage Done: 5817

Name: khufo (laid the final blow)
Security: 3.3
Corp: Malevolent Evolution
Alliance: The Church.
Faction: NONE
Ship: Stabber
Weapon: Torrent Assault Missile
Damage Done: 2897

Name: Hyletta
Security: 2.5
Corp: Clown Punchers.
Alliance: Clown Punchers Syndicate
Faction: NONE
Ship: Dominix
Weapon: Bouncer II
Damage Done: 2870

Name: Serpentis Chief Guard / Serpentis Corporation
Damage Done: 2706

Name: Sylai Leonidas
Security: 4.6
Corp: Clown Punchers.
Alliance: Clown Punchers Syndicate
Faction: NONE
Ship: Harpy
Weapon: Harpy
Damage Done: 1421

Name: Kal Shakai
Security: -4.6
Corp: Clown Punchers.
Alliance: Clown Punchers Syndicate
Faction: NONE
Ship: Armageddon
Weapon: Armageddon
Damage Done: 883

Name: Cemile
Security: 0.5
Corp: Clown Punchers.
Alliance: Clown Punchers Syndicate
Faction: NONE
Ship: Crow
Weapon: Caldari Navy Bloodclaw Light Missile
Damage Done: 832

Name: Teister
Security: 1.4
Corp: Clown Punchers.
Alliance: Clown Punchers Syndicate
Faction: NONE
Ship: Tempest
Weapon: Tempest
Damage Done: 766

Name: ts5p
Security: 4.1
Corp: Clown Punchers.
Alliance: Clown Punchers Syndicate
Faction: NONE
Ship: Tempest
Weapon: Tempest
Damage Done: 720

Name: Arancia Detto
Security: 4.6
Corp: Clown Punchers.
Alliance: Clown Punchers Syndicate
Faction: NONE
Ship: Damnation
Weapon: Caldari Navy Thunderbolt Heavy Missile
Damage Done: 450

Name: Rockstara
Security: -0.8
Corp: Clown Punchers.
Alliance: Clown Punchers Syndicate
Faction: NONE
Ship: Eris
Weapon: Eris
Damage Done: 387

Name: Nicomedes
Security: 5.0
Corp: Clown Punchers.
Alliance: Clown Punchers Syndicate
Faction: NONE
Ship: Raptor
Weapon: Raptor
Damage Done: 369

Name: Heimdal Galplen
Security: 4.9
Corp: Clown Punchers.
Alliance: Clown Punchers Syndicate
Faction: NONE
Ship: Stiletto
Weapon: Stiletto
Damage Done: 281

Name: Salvo Brunel
Security: 2.0
Corp: Clown Punchers.
Alliance: Clown Punchers Syndicate
Faction: NONE
Ship: Stiletto
Weapon: Stiletto
Damage Done: 243

Name: Oni Koroshi
Security: -1.5
Corp: Clown Punchers.
Alliance: Clown Punchers Syndicate
Faction: NONE
Ship: Punisher
Weapon: Punisher
Damage Done: 242

Name: Qween Cleopatra
Security: 2.9
Corp: Clown Punchers.
Alliance: Clown Punchers Syndicate
Faction: NONE
Ship: Ares
Weapon: Ares
Damage Done: 135

Name: Music TSP
Security: 4.5
Corp: Clown Punchers.
Alliance: Clown Punchers Syndicate
Faction: NONE
Ship: Stiletto
Weapon: Tracking Disruptor II
Damage Done: 0

Name: edsabi
Security: 4.4
Corp: Clown Punchers.
Alliance: Clown Punchers Syndicate
Faction: NONE
Ship: Ares
Weapon: Warp Disruptor II
Damage Done: 0

Name: Niraia
Security: -3.5
Corp: Clown Punchers.
Alliance: Clown Punchers Syndicate
Faction: NONE
Ship: Megathron
Weapon: Neutron Blaster Cannon II
Damage Done: 0


Destroyed items:

Heavy Assault Missile Launcher II
Heavy Assault Missile Launcher II
Heavy Assault Missile Launcher II
Caldari Navy Terror Assault Missile
Caldari Navy Terror Assault Missile
Caldari Navy Terror Assault Missile
Caldari Navy Terror Assault Missile
Caldari Navy Terror Assault Missile
Caldari Navy Terror Assault Missile
Large Shield Extender II
Large Shield Extender II
Shadow Serpentis Warp Disruptor
Corelum C-Type 10MN MicroWarpdrive
Photon Scattering Field II
Damage Control II
Caldari Navy Ballistic Control System
Caldari Navy Ballistic Control System
Heavy Electrochemical Capacitor Booster I (Cargo)
Electron Blaster Cannon I, Qty: 2 (Cargo)
Core Defence Field Extender I, Qty: 2
Anti-Explosive Screen Reinforcer II
Tengu Offensive - Accelerated Ejection Bay
Tengu Propulsion - Gravitational Capacitor
Tengu Defensive - Supplemental Screening
Tengu Engineering - Capacitor Regeneration Matrix
Tengu Electronics - Obfuscation Manifold

Dropped items:

Heavy Assault Missile Launcher II
Heavy Assault Missile Launcher II
Caldari Navy Terror Assault Missile
Caldari Navy Terror Assault Missile
Caldari Navy Terror Assault Missile
Caldari Navy Terror Assault Missile
Caldari Navy Invulnerability Field
Photon Scattering Field II
Caldari Navy Ballistic Control System
Regulated Mega Ion Phase Cannon I (Cargo)
Caldari Navy Terror Assault Missile, Qty: 1995 (Cargo)
Terror Assault Missile, Qty: 9415 (Cargo)
Electron Blaster Cannon I (Cargo)'''