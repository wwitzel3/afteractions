from afteractions.lib.eveapi import ParseXML

from datetime import datetime

class TestKillXmlParser(object):
    def setUp(self):
        self.results = ParseXML(xml)
        
    def tearDown(self):
        pass
    
    def skip_test_parse_kill_pilot(self):
        kill = self.results.kills[0]
        
        characterID = kill.victim.characterID
        corporationID = kill.victim.corporationID
        allianceID = kill.victim.allianceID
        
        assert characterID == 298944521
        assert corporationID == 1000168
        assert allianceID == 0
    
xml = '''<?xml version='1.0' encoding='UTF-8'?>
<eveapi version="2">
  <currentTime>2009-04-01 15:23:24</currentTime>
  <result>
    <rowset name="kills" key="killID" columns="killID,solarSystemID,killTime,moonID">
      <row killID="6373564" solarSystemID="30004502" killTime="2009-04-01 03:59:00" moonID="0">
        <victim characterID="298944521" characterName="Ur Mam" corporationID="1000168" corporationName="Federal Navy Academy" allianceID="0" allianceName="" factionID="0" factionName="" damageTaken="269" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1386697756" characterName="Music TSP" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.28252983890402" damageDone="203" finalBlow="1" weaponTypeID="2969" shipTypeID="24702" />
          <row characterID="246573211" characterName="Ydoc Llezsor" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0.4" damageDone="66" finalBlow="0" weaponTypeID="24702" shipTypeID="24702" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6373547" solarSystemID="30004502" killTime="2009-04-01 03:57:00" moonID="0">
        <victim characterID="298944521" characterName="Ur Mam" corporationID="1000168" corporationName="Federal Navy Academy" allianceID="0" allianceName="" factionID="0" factionName="" damageTaken="358" shipTypeID="606" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="318582956" characterName="Vibenation 2" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.96543317670918" damageDone="358" finalBlow="1" weaponTypeID="2969" shipTypeID="24702" />
          <row characterID="246573211" characterName="Ydoc Llezsor" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0.4" damageDone="0" finalBlow="0" weaponTypeID="2897" shipTypeID="24702" />
          <row characterID="283816166" characterName="Captain Mac" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="1.9" damageDone="0" finalBlow="0" weaponTypeID="28654" shipTypeID="12013" />
          <row characterID="751771895" characterName="JunkRaider" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="-0.4" damageDone="0" finalBlow="0" weaponTypeID="2404" shipTypeID="11176" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="3651" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="34" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3640" flag="0" qtyDropped="0" qtyDestroyed="1" />
        </rowset>
      </row>
      <row killID="6373432" solarSystemID="30004504" killTime="2009-04-01 03:47:00" moonID="0">
        <victim characterID="637925697" characterName="Leonidas758" corporationID="583616018" corporationName="Black Aces" allianceID="1345801112" allianceName="Dead Mans Hand" factionID="0" factionName="" damageTaken="337" shipTypeID="11379" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1386697756" characterName="Music TSP" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.28252983890402" damageDone="337" finalBlow="1" weaponTypeID="2969" shipTypeID="24702" />
          <row characterID="636046666" characterName="Mr Inevitability" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="5" damageDone="0" finalBlow="0" weaponTypeID="5399" shipTypeID="24696" />
          <row characterID="149816009" characterName="Jaedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-3.8" damageDone="0" finalBlow="0" weaponTypeID="12709" shipTypeID="24702" />
          <row characterID="1294761598" characterName="caloon" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="2.1" damageDone="0" finalBlow="0" weaponTypeID="2410" shipTypeID="24702" />
          <row characterID="283816166" characterName="Captain Mac" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="1.9" damageDone="0" finalBlow="0" weaponTypeID="28654" shipTypeID="12013" />
          <row characterID="751771895" characterName="JunkRaider" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="-0.4" damageDone="0" finalBlow="0" weaponTypeID="3244" shipTypeID="11176" />
          <row characterID="318582956" characterName="Vibenation 2" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3" damageDone="0" finalBlow="0" weaponTypeID="2969" shipTypeID="24702" />
          <row characterID="246573211" characterName="Ydoc Llezsor" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0.4" damageDone="0" finalBlow="0" weaponTypeID="2897" shipTypeID="24702" />
          <row characterID="1963396956" characterName="Quebnaric Deile" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.8" damageDone="0" finalBlow="0" weaponTypeID="2969" shipTypeID="24702" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="434" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2281" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="2048" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="377" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="1236" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="27361" flag="5" qtyDropped="1000" qtyDestroyed="0" />
          <row typeID="7993" flag="0" qtyDropped="1" qtyDestroyed="3" />
          <row typeID="26076" flag="0" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="5441" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="27361" flag="0" qtyDropped="108" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6373029" solarSystemID="30003349" killTime="2009-04-01 03:11:00" moonID="0">
        <victim characterID="1614752826" characterName="Craig Spist" corporationID="230423181" corporationName="Galactic Defence Syndicate" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" damageTaken="196" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="636046666" characterName="Mr Inevitability" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="5.00286031520726" damageDone="196" finalBlow="1" weaponTypeID="3520" shipTypeID="24696" />
          <row characterID="283816166" characterName="Captain Mac" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="1.9" damageDone="0" finalBlow="0" weaponTypeID="28654" shipTypeID="12013" />
          <row characterID="878728887" characterName="Kal Shakai" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-4.6" damageDone="0" finalBlow="0" weaponTypeID="2881" shipTypeID="22456" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6373019" solarSystemID="30003349" killTime="2009-04-01 03:10:00" moonID="0">
        <victim characterID="1614752826" characterName="Craig Spist" corporationID="230423181" corporationName="Galactic Defence Syndicate" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" damageTaken="46036" shipTypeID="638" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="636046666" characterName="Mr Inevitability" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="5.00286031520726" damageDone="13414" finalBlow="1" weaponTypeID="21640" shipTypeID="24696" />
          <row characterID="1386697756" characterName="Music TSP" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.3" damageDone="6901" finalBlow="0" weaponTypeID="2488" shipTypeID="24702" />
          <row characterID="476777753" characterName="Heimdal Galplen" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.9" damageDone="5960" finalBlow="0" weaponTypeID="2488" shipTypeID="24702" />
          <row characterID="1294761598" characterName="caloon" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="2.1" damageDone="5211" finalBlow="0" weaponTypeID="2488" shipTypeID="24702" />
          <row characterID="1963396956" characterName="Quebnaric Deile" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.8" damageDone="4269" finalBlow="0" weaponTypeID="28215" shipTypeID="24702" />
          <row characterID="283816166" characterName="Captain Mac" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="1.9" damageDone="3469" finalBlow="0" weaponTypeID="12013" shipTypeID="12013" />
          <row characterID="878728887" characterName="Kal Shakai" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-4.6" damageDone="2413" finalBlow="0" weaponTypeID="22456" shipTypeID="22456" />
          <row characterID="1736469556" characterName="Boka Smowl" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="-1.4" damageDone="2243" finalBlow="0" weaponTypeID="5401" shipTypeID="629" />
          <row characterID="272405573" characterName="Tukuarikan" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0.4" damageDone="1343" finalBlow="0" weaponTypeID="629" shipTypeID="629" />
          <row characterID="149816009" characterName="Jaedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-3.8" damageDone="813" finalBlow="0" weaponTypeID="24702" shipTypeID="24702" />
          <row characterID="1868072702" characterName="Rockstara" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.1" damageDone="0" finalBlow="0" weaponTypeID="3170" shipTypeID="11200" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="1353" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="27423" flag="5" qtyDropped="0" qtyDestroyed="1919" />
          <row typeID="16519" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="2046" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="27395" flag="0" qtyDropped="52" qtyDestroyed="50" />
          <row typeID="26088" flag="0" qtyDropped="0" qtyDestroyed="3" />
          <row typeID="2185" flag="87" qtyDropped="3" qtyDestroyed="4" />
          <row typeID="2539" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="11577" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="1952" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="16517" flag="0" qtyDropped="3" qtyDestroyed="2" />
          <row typeID="22291" flag="0" qtyDropped="1" qtyDestroyed="2" />
          <row typeID="3841" flag="0" qtyDropped="2" qtyDestroyed="1" />
          <row typeID="27395" flag="5" qtyDropped="0" qtyDestroyed="1361" />
        </rowset>
      </row>
      <row killID="6373009" solarSystemID="30003349" killTime="2009-04-01 03:09:00" moonID="0">
        <victim characterID="1728105027" characterName="MrHurlbut" corporationID="230423181" corporationName="Galactic Defence Syndicate" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" damageTaken="20410" shipTypeID="24698" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1963396956" characterName="Quebnaric Deile" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.76642961269104" damageDone="3389" finalBlow="1" weaponTypeID="2969" shipTypeID="24702" />
          <row characterID="636046666" characterName="Mr Inevitability" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="5" damageDone="6000" finalBlow="0" weaponTypeID="24696" shipTypeID="24696" />
          <row characterID="476777753" characterName="Heimdal Galplen" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.9" damageDone="3712" finalBlow="0" weaponTypeID="2488" shipTypeID="24702" />
          <row characterID="1386697756" characterName="Music TSP" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.3" damageDone="2397" finalBlow="0" weaponTypeID="2488" shipTypeID="24702" />
          <row characterID="1736469556" characterName="Boka Smowl" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="-1.4" damageDone="1791" finalBlow="0" weaponTypeID="629" shipTypeID="629" />
          <row characterID="1294761598" characterName="caloon" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="2.1" damageDone="1630" finalBlow="0" weaponTypeID="2488" shipTypeID="24702" />
          <row characterID="283816166" characterName="Captain Mac" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="1.9" damageDone="760" finalBlow="0" weaponTypeID="12013" shipTypeID="12013" />
          <row characterID="272405573" characterName="Tukuarikan" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0.4" damageDone="731" finalBlow="0" weaponTypeID="2516" shipTypeID="629" />
          <row characterID="246573211" characterName="Ydoc Llezsor" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0.4" damageDone="0" finalBlow="0" weaponTypeID="24702" shipTypeID="24702" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="2331" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="12274" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2281" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="27413" flag="0" qtyDropped="0" qtyDestroyed="55" />
          <row typeID="501" flag="0" qtyDropped="3" qtyDestroyed="2" />
          <row typeID="1353" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="27453" flag="0" qtyDropped="54" qtyDestroyed="81" />
          <row typeID="25707" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="1986" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="6160" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="27413" flag="5" qtyDropped="87" qtyDestroyed="0" />
          <row typeID="10858" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="29011" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3242" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="3841" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="27453" flag="5" qtyDropped="891" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6372989" solarSystemID="30003349" killTime="2009-04-01 03:07:00" moonID="0">
        <victim characterID="1585747136" characterName="digitalat0m" corporationID="230423181" corporationName="Galactic Defence Syndicate" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" damageTaken="9348" shipTypeID="626" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="476777753" characterName="Heimdal Galplen" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.89756758574854" damageDone="714" finalBlow="1" weaponTypeID="2969" shipTypeID="24702" />
          <row characterID="246573211" characterName="Ydoc Llezsor" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0.4" damageDone="2794" finalBlow="0" weaponTypeID="24702" shipTypeID="24702" />
          <row characterID="1963396956" characterName="Quebnaric Deile" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.8" damageDone="2699" finalBlow="0" weaponTypeID="28215" shipTypeID="24702" />
          <row characterID="149816009" characterName="Jaedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-3.8" damageDone="1211" finalBlow="0" weaponTypeID="12709" shipTypeID="24702" />
          <row characterID="751771895" characterName="JunkRaider" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="-0.4" damageDone="744" finalBlow="0" weaponTypeID="210" shipTypeID="11176" />
          <row characterID="283816166" characterName="Captain Mac" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="1.9" damageDone="611" finalBlow="0" weaponTypeID="12013" shipTypeID="12013" />
          <row characterID="1294761598" characterName="caloon" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="2.1" damageDone="302" finalBlow="0" weaponTypeID="27447" shipTypeID="24702" />
          <row characterID="1386697756" characterName="Music TSP" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.3" damageDone="153" finalBlow="0" weaponTypeID="24702" shipTypeID="24702" />
          <row characterID="272405573" characterName="Tukuarikan" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0.4" damageDone="120" finalBlow="0" weaponTypeID="629" shipTypeID="629" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="222" flag="5" qtyDropped="0" qtyDestroyed="2664" />
          <row typeID="565" flag="0" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="16355" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="16367" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="29011" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="7289" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="11277" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="25861" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="24348" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="1973" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="11329" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="12056" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="2446" flag="87" qtyDropped="2" qtyDestroyed="1" />
          <row typeID="6157" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="222" flag="0" qtyDropped="30" qtyDestroyed="59" />
        </rowset>
      </row>
      <row killID="6372214" solarSystemID="30003321" killTime="2009-04-01 02:06:00" moonID="0">
        <victim characterID="1921127490" characterName="ofstrife" corporationID="1694002910" corporationName="The Industrial Consortium" allianceID="0" allianceName="" factionID="0" factionName="" damageTaken="182" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="747677046" characterName="Ciryon Atani" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.60251097597117" damageDone="182" finalBlow="1" weaponTypeID="27413" shipTypeID="11995" />
          <row characterID="246573211" characterName="Ydoc Llezsor" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0.4" damageDone="0" finalBlow="0" weaponTypeID="3244" shipTypeID="12003" />
          <row characterID="751771895" characterName="JunkRaider" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="-0.4" damageDone="0" finalBlow="0" weaponTypeID="2889" shipTypeID="11400" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6372202" solarSystemID="30003321" killTime="2009-04-01 02:05:00" moonID="0">
        <victim characterID="596567154" characterName="Rick Skynight" corporationID="1000169" corporationName="Center for Advanced Studies" allianceID="0" allianceName="" factionID="0" factionName="" damageTaken="23955" shipTypeID="24698" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="233991150" characterName="Maelgar" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.70885186831252" damageDone="3059" finalBlow="1" weaponTypeID="2969" shipTypeID="24702" />
          <row characterID="372559142" characterName="Knat" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.8" damageDone="3644" finalBlow="0" weaponTypeID="24702" shipTypeID="24702" />
          <row characterID="318582956" characterName="Vibenation 2" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3" damageDone="3340" finalBlow="0" weaponTypeID="2488" shipTypeID="24702" />
          <row characterID="1294761598" characterName="caloon" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="2" damageDone="3171" finalBlow="0" weaponTypeID="2488" shipTypeID="24702" />
          <row characterID="1868072702" characterName="Rockstara" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.1" damageDone="2085" finalBlow="0" weaponTypeID="641" shipTypeID="641" />
          <row characterID="283816166" characterName="Captain Mac" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="1.9" damageDone="1973" finalBlow="0" weaponTypeID="2446" shipTypeID="645" />
          <row characterID="246573211" characterName="Ydoc Llezsor" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0.4" damageDone="1429" finalBlow="0" weaponTypeID="3244" shipTypeID="12003" />
          <row characterID="1987189746" characterName="Papa Murphy" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="4" damageDone="1352" finalBlow="0" weaponTypeID="2456" shipTypeID="11999" />
          <row characterID="149816009" characterName="Jaedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-3.9" damageDone="1214" finalBlow="0" weaponTypeID="27441" shipTypeID="24698" />
          <row characterID="747677046" characterName="Ciryon Atani" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.6" damageDone="720" finalBlow="0" weaponTypeID="27413" shipTypeID="11995" />
          <row characterID="1736469556" characterName="Boka Smowl" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="-1.4" damageDone="714" finalBlow="0" weaponTypeID="211" shipTypeID="629" />
          <row characterID="751771895" characterName="JunkRaider" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="-0.4" damageDone="711" finalBlow="0" weaponTypeID="11400" shipTypeID="11400" />
          <row characterID="1386697756" characterName="Music TSP" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.3" damageDone="543" finalBlow="0" weaponTypeID="2488" shipTypeID="24702" />
          <row characterID="878728887" characterName="Kal Shakai" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-4.6" damageDone="0" finalBlow="0" weaponTypeID="2571" shipTypeID="11957" />
          <row characterID="272405573" characterName="Tukuarikan" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0.4" damageDone="0" finalBlow="0" weaponTypeID="4025" shipTypeID="587" />
          <row characterID="1980242573" characterName="edsabi" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.9" damageDone="0" finalBlow="0" weaponTypeID="2571" shipTypeID="11957" />
          <row characterID="476777753" characterName="Heimdal Galplen" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.9" damageDone="0" finalBlow="0" weaponTypeID="2571" shipTypeID="11957" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="2048" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="23512" flag="87" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="27413" flag="0" qtyDropped="105" qtyDestroyed="140" />
          <row typeID="1422" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="9660" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="25711" flag="0" qtyDropped="4" qtyDestroyed="3" />
          <row typeID="20307" flag="5" qtyDropped="0" qtyDestroyed="5185" />
          <row typeID="26082" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="20409" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="3831" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="27413" flag="5" qtyDropped="278" qtyDestroyed="0" />
          <row typeID="1541" flag="0" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="26076" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2291" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="394" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3841" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="21638" flag="5" qtyDropped="0" qtyDestroyed="4" />
          <row typeID="26084" flag="0" qtyDropped="0" qtyDestroyed="1" />
        </rowset>
      </row>
      <row killID="6372196" solarSystemID="30003321" killTime="2009-04-01 02:04:00" moonID="0">
        <victim characterID="443573777" characterName="Al'Xandra" corporationID="1000169" corporationName="Center for Advanced Studies" allianceID="0" allianceName="" factionID="0" factionName="" damageTaken="677" shipTypeID="594" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="747677046" characterName="Ciryon Atani" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.60251097597117" damageDone="380" finalBlow="1" weaponTypeID="27413" shipTypeID="11995" />
          <row characterID="318582956" characterName="Vibenation 2" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3" damageDone="297" finalBlow="0" weaponTypeID="2488" shipTypeID="24702" />
          <row characterID="476777753" characterName="Heimdal Galplen" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.9" damageDone="0" finalBlow="0" weaponTypeID="2563" shipTypeID="11957" />
          <row characterID="246573211" characterName="Ydoc Llezsor" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0.4" damageDone="0" finalBlow="0" weaponTypeID="3520" shipTypeID="12003" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="10688" flag="0" qtyDropped="3" qtyDestroyed="0" />
          <row typeID="222" flag="0" qtyDropped="28" qtyDestroyed="14" />
          <row typeID="6001" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="29007" flag="0" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="29005" flag="5" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="2603" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="222" flag="5" qtyDropped="897" qtyDestroyed="0" />
          <row typeID="5322" flag="0" qtyDropped="1" qtyDestroyed="1" />
        </rowset>
      </row>
      <row killID="6372190" solarSystemID="30003321" killTime="2009-04-01 02:04:00" moonID="0">
        <victim characterID="1833837953" characterName="Nyota Sol" corporationID="1000169" corporationName="Center for Advanced Studies" allianceID="0" allianceName="" factionID="0" factionName="" damageTaken="3139" shipTypeID="627" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="372559142" characterName="Knat" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.75698474214155" damageDone="2254" finalBlow="1" weaponTypeID="2969" shipTypeID="24702" />
          <row characterID="1868072702" characterName="Rockstara" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.1" damageDone="590" finalBlow="0" weaponTypeID="3244" shipTypeID="641" />
          <row characterID="1294761598" characterName="caloon" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="2" damageDone="221" finalBlow="0" weaponTypeID="2410" shipTypeID="24702" />
          <row characterID="272405573" characterName="Tukuarikan" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0.4" damageDone="74" finalBlow="0" weaponTypeID="587" shipTypeID="587" />
          <row characterID="1736469556" characterName="Boka Smowl" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="-1.4" damageDone="0" finalBlow="0" weaponTypeID="8023" shipTypeID="629" />
          <row characterID="1987189746" characterName="Papa Murphy" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="4" damageDone="0" finalBlow="0" weaponTypeID="501" shipTypeID="11999" />
          <row characterID="233991150" characterName="Maelgar" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.7" damageDone="0" finalBlow="0" weaponTypeID="3244" shipTypeID="24702" />
          <row characterID="747677046" characterName="Ciryon Atani" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.6" damageDone="0" finalBlow="0" weaponTypeID="25715" shipTypeID="11995" />
          <row characterID="751771895" characterName="JunkRaider" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="-0.4" damageDone="0" finalBlow="0" weaponTypeID="2889" shipTypeID="11400" />
          <row characterID="318582956" characterName="Vibenation 2" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3" damageDone="0" finalBlow="0" weaponTypeID="2488" shipTypeID="24702" />
          <row characterID="1386697756" characterName="Music TSP" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.3" damageDone="0" finalBlow="0" weaponTypeID="3244" shipTypeID="24702" />
          <row characterID="246573211" characterName="Ydoc Llezsor" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0.4" damageDone="0" finalBlow="0" weaponTypeID="3520" shipTypeID="12003" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="1244" flag="5" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="12056" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3528" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3887" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="4029" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="223" flag="5" qtyDropped="1708" qtyDestroyed="0" />
          <row typeID="5239" flag="5" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2048" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="567" flag="0" qtyDropped="2" qtyDestroyed="3" />
          <row typeID="3242" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="9944" flag="0" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="223" flag="0" qtyDropped="274" qtyDestroyed="184" />
          <row typeID="2173" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="230" flag="5" qtyDropped="3000" qtyDestroyed="0" />
          <row typeID="2183" flag="87" qtyDropped="4" qtyDestroyed="1" />
        </rowset>
      </row>
      <row killID="6372188" solarSystemID="30003321" killTime="2009-04-01 02:04:00" moonID="0">
        <victim characterID="1926331074" characterName="norma weaver" corporationID="1000169" corporationName="Center for Advanced Studies" allianceID="0" allianceName="" factionID="0" factionName="" damageTaken="4021" shipTypeID="626" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1386697756" characterName="Music TSP" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.27680664554957" damageDone="620" finalBlow="1" weaponTypeID="2969" shipTypeID="24702" />
          <row characterID="372559142" characterName="Knat" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.8" damageDone="1611" finalBlow="0" weaponTypeID="2488" shipTypeID="24702" />
          <row characterID="1294761598" characterName="caloon" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="2" damageDone="530" finalBlow="0" weaponTypeID="2488" shipTypeID="24702" />
          <row characterID="476777753" characterName="Heimdal Galplen" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.9" damageDone="469" finalBlow="0" weaponTypeID="2905" shipTypeID="11957" />
          <row characterID="233991150" characterName="Maelgar" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.7" damageDone="374" finalBlow="0" weaponTypeID="3244" shipTypeID="24702" />
          <row characterID="1868072702" characterName="Rockstara" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.1" damageDone="369" finalBlow="0" weaponTypeID="641" shipTypeID="641" />
          <row characterID="751771895" characterName="JunkRaider" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="-0.4" damageDone="32" finalBlow="0" weaponTypeID="11400" shipTypeID="11400" />
          <row characterID="272405573" characterName="Tukuarikan" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0.4" damageDone="16" finalBlow="0" weaponTypeID="4025" shipTypeID="587" />
          <row characterID="747677046" characterName="Ciryon Atani" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.6" damageDone="0" finalBlow="0" weaponTypeID="25715" shipTypeID="11995" />
          <row characterID="149816009" characterName="Jaedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-3.9" damageDone="0" finalBlow="0" weaponTypeID="8101" shipTypeID="24698" />
          <row characterID="246573211" characterName="Ydoc Llezsor" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0.4" damageDone="0" finalBlow="0" weaponTypeID="3520" shipTypeID="12003" />
          <row characterID="596567154" characterName="Rick Skynight" corporationID="1000169" corporationName="Center for Advanced Studies" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="5" damageDone="0" finalBlow="0" weaponTypeID="27413" shipTypeID="24698" />
          <row characterID="1736469556" characterName="Boka Smowl" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="-1.4" damageDone="0" finalBlow="0" weaponTypeID="4029" shipTypeID="629" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="444" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3887" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="23527" flag="0" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="11267" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="12058" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2185" flag="87" qtyDropped="4" qtyDestroyed="1" />
          <row typeID="2048" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="526" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="12257" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="482" flag="5" qtyDropped="2" qtyDestroyed="2" />
          <row typeID="23525" flag="87" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="447" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="20353" flag="0" qtyDropped="0" qtyDestroyed="1" />
        </rowset>
      </row>
      <row killID="6372185" solarSystemID="30003321" killTime="2009-04-01 02:04:00" moonID="0">
        <victim characterID="1860702282" characterName="Eoras Northwind" corporationID="1000169" corporationName="Center for Advanced Studies" allianceID="0" allianceName="" factionID="0" factionName="" damageTaken="6367" shipTypeID="626" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="318582956" characterName="Vibenation 2" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.96543317670918" damageDone="973" finalBlow="1" weaponTypeID="2969" shipTypeID="24702" />
          <row characterID="747677046" characterName="Ciryon Atani" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.6" damageDone="3399" finalBlow="0" weaponTypeID="25715" shipTypeID="11995" />
          <row characterID="1736469556" characterName="Boka Smowl" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="-1.4" damageDone="1696" finalBlow="0" weaponTypeID="2514" shipTypeID="629" />
          <row characterID="476777753" characterName="Heimdal Galplen" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.9" damageDone="166" finalBlow="0" weaponTypeID="11371" shipTypeID="11957" />
          <row characterID="233991150" characterName="Maelgar" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.7" damageDone="133" finalBlow="0" weaponTypeID="2969" shipTypeID="24702" />
          <row characterID="372559142" characterName="Knat" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.8" damageDone="0" finalBlow="0" weaponTypeID="527" shipTypeID="24702" />
          <row characterID="751771895" characterName="JunkRaider" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="-0.4" damageDone="0" finalBlow="0" weaponTypeID="2889" shipTypeID="11400" />
          <row characterID="1294761598" characterName="caloon" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="2" damageDone="0" finalBlow="0" weaponTypeID="2410" shipTypeID="24702" />
          <row characterID="246573211" characterName="Ydoc Llezsor" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0.4" damageDone="0" finalBlow="0" weaponTypeID="3244" shipTypeID="12003" />
          <row characterID="1386697756" characterName="Music TSP" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.3" damageDone="0" finalBlow="0" weaponTypeID="2488" shipTypeID="24702" />
          <row characterID="149816009" characterName="Jaedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-3.9" damageDone="0" finalBlow="0" weaponTypeID="3244" shipTypeID="24698" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="13001" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="2048" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2488" flag="87" qtyDropped="2" qtyDestroyed="3" />
          <row typeID="5443" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="20351" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="12052" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="22977" flag="5" qtyDropped="0" qtyDestroyed="400" />
          <row typeID="567" flag="0" qtyDropped="1" qtyDestroyed="3" />
          <row typeID="526" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="11269" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="22977" flag="0" qtyDropped="218" qtyDestroyed="218" />
          <row typeID="1183" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="23711" flag="87" qtyDropped="5" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6372137" solarSystemID="30003321" killTime="2009-04-01 01:59:00" moonID="0">
        <victim characterID="441010356" characterName="Terri Lam" corporationID="1000169" corporationName="Center for Advanced Studies" allianceID="0" allianceName="" factionID="0" factionName="" damageTaken="1196" shipTypeID="594" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1868072702" characterName="Rockstara" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.14180391949182" damageDone="1196" finalBlow="1" weaponTypeID="2456" shipTypeID="11200" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="434" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="5319" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="217" flag="5" qtyDropped="440" qtyDestroyed="0" />
          <row typeID="8175" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="29007" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2603" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="217" flag="0" qtyDropped="210" qtyDestroyed="105" />
          <row typeID="5399" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="222" flag="5" qtyDropped="1047" qtyDestroyed="0" />
          <row typeID="7539" flag="0" qtyDropped="1" qtyDestroyed="2" />
        </rowset>
      </row>
      <row killID="6372135" solarSystemID="30003321" killTime="2009-04-01 01:59:00" moonID="0">
        <victim characterID="318582956" characterName="Vibenation 2" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="2236" shipTypeID="22456" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1926331074" characterName="norma weaver" corporationID="1000169" corporationName="Center for Advanced Studies" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="1.90421120889201" damageDone="192" finalBlow="1" weaponTypeID="2185" shipTypeID="626" />
          <row characterID="1053134250" characterName="Tlak Chilk" corporationID="1000169" corporationName="Center for Advanced Studies" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="4.8" damageDone="642" finalBlow="0" weaponTypeID="24700" shipTypeID="24700" />
          <row characterID="1921127490" characterName="ofstrife" corporationID="1694002910" corporationName="The Industrial Consortium" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="5" damageDone="602" finalBlow="0" weaponTypeID="2486" shipTypeID="626" />
          <row characterID="1833837953" characterName="Nyota Sol" corporationID="1000169" corporationName="Center for Advanced Studies" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="1" damageDone="403" finalBlow="0" weaponTypeID="2183" shipTypeID="627" />
          <row characterID="146026249" characterName="Ashina Sito" corporationID="1000169" corporationName="Center for Advanced Studies" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="5" damageDone="208" finalBlow="0" weaponTypeID="2488" shipTypeID="645" />
          <row characterID="1483783802" characterName="Brandon Bell" corporationID="1000169" corporationName="Center for Advanced Studies" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="5" damageDone="189" finalBlow="0" weaponTypeID="21638" shipTypeID="627" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="28668" flag="5" qtyDropped="0" qtyDestroyed="75" />
          <row typeID="12625" flag="5" qtyDropped="461" qtyDestroyed="0" />
          <row typeID="2889" flag="0" qtyDropped="1" qtyDestroyed="6" />
          <row typeID="22782" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3244" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="22778" flag="0" qtyDropped="0" qtyDestroyed="10" />
          <row typeID="12625" flag="0" qtyDropped="10" qtyDestroyed="25" />
          <row typeID="527" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="1236" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="22778" flag="5" qtyDropped="20" qtyDestroyed="0" />
          <row typeID="3831" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="440" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2605" flag="0" qtyDropped="0" qtyDestroyed="1" />
        </rowset>
      </row>
      <row killID="6372127" solarSystemID="30003321" killTime="2009-04-01 01:59:00" moonID="0">
        <victim characterID="233991150" characterName="Maelgar" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="3002" shipTypeID="12044" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1053134250" characterName="Tlak Chilk" corporationID="1000169" corporationName="Center for Advanced Studies" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="4.77631474686635" damageDone="1024" finalBlow="1" weaponTypeID="2478" shipTypeID="24700" />
          <row characterID="1921127490" characterName="ofstrife" corporationID="1694002910" corporationName="The Industrial Consortium" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="5" damageDone="1333" finalBlow="0" weaponTypeID="626" shipTypeID="626" />
          <row characterID="1860702282" characterName="Eoras Northwind" corporationID="1000169" corporationName="Center for Advanced Studies" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="5" damageDone="382" finalBlow="0" weaponTypeID="2488" shipTypeID="626" />
          <row characterID="644435029" characterName="omnikan" corporationID="1838710448" corporationName="Dark Star Productions" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="5" damageDone="152" finalBlow="0" weaponTypeID="2203" shipTypeID="626" />
          <row characterID="712412231" characterName="Aldric Gelec" corporationID="1000169" corporationName="Center for Advanced Studies" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="1.7" damageDone="111" finalBlow="0" weaponTypeID="2183" shipTypeID="670" />
          <row characterID="0" characterName="" corporationID="1000135" corporationName="Serpentis Corporation" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0" damageDone="0" finalBlow="0" weaponTypeID="0" shipTypeID="11923" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="28668" flag="5" qtyDropped="0" qtyDestroyed="97" />
          <row typeID="13001" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="23019" flag="5" qtyDropped="0" qtyDestroyed="2135" />
          <row typeID="23009" flag="5" qtyDropped="0" qtyDestroyed="1476" />
          <row typeID="5320" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="29007" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="3170" flag="0" qtyDropped="3" qtyDestroyed="1" />
          <row typeID="16311" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="10190" flag="0" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="6003" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="23009" flag="0" qtyDropped="69" qtyDestroyed="207" />
          <row typeID="5837" flag="0" qtyDropped="1" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6372123" solarSystemID="30003321" killTime="2009-04-01 01:58:00" moonID="0">
        <victim characterID="1386697756" characterName="Music TSP" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="927" shipTypeID="11198" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1921127490" characterName="ofstrife" corporationID="1694002910" corporationName="The Industrial Consortium" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="5.00680830698044" damageDone="64" finalBlow="1" weaponTypeID="2486" shipTypeID="626" />
          <row characterID="1053134250" characterName="Tlak Chilk" corporationID="1000169" corporationName="Center for Advanced Studies" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="4.8" damageDone="863" finalBlow="0" weaponTypeID="2488" shipTypeID="24700" />
          <row characterID="1860702282" characterName="Eoras Northwind" corporationID="1000169" corporationName="Center for Advanced Studies" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="5" damageDone="0" finalBlow="0" weaponTypeID="2488" shipTypeID="626" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="21898" flag="5" qtyDropped="1080" qtyDestroyed="0" />
          <row typeID="2889" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="1447" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3244" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="16527" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="527" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="19814" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="1236" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="27333" flag="0" qtyDropped="5" qtyDestroyed="0" />
          <row typeID="21898" flag="0" qtyDropped="96" qtyDestroyed="0" />
          <row typeID="440" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="2605" flag="0" qtyDropped="0" qtyDestroyed="1" />
        </rowset>
      </row>
      <row killID="6372117" solarSystemID="30003321" killTime="2009-04-01 01:58:00" moonID="0">
        <victim characterID="712412231" characterName="Aldric Gelec" corporationID="1000169" corporationName="Center for Advanced Studies" allianceID="0" allianceName="" factionID="0" factionName="" damageTaken="2367" shipTypeID="626" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="233991150" characterName="Maelgar" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.70885186831252" damageDone="1145" finalBlow="1" weaponTypeID="3170" shipTypeID="12044" />
          <row characterID="747677046" characterName="Ciryon Atani" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.6" damageDone="315" finalBlow="0" weaponTypeID="27413" shipTypeID="11995" />
          <row characterID="149816009" characterName="Jaedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-3.9" damageDone="302" finalBlow="0" weaponTypeID="24473" shipTypeID="11365" />
          <row characterID="476777753" characterName="Heimdal Galplen" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.9" damageDone="257" finalBlow="0" weaponTypeID="11371" shipTypeID="11371" />
          <row characterID="1736469556" characterName="Boka Smowl" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="-1.4" damageDone="249" finalBlow="0" weaponTypeID="2514" shipTypeID="587" />
          <row characterID="272405573" characterName="Tukuarikan" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0.4" damageDone="99" finalBlow="0" weaponTypeID="486" shipTypeID="670" />
          <row characterID="318582956" characterName="Vibenation 2" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3" damageDone="0" finalBlow="0" weaponTypeID="2889" shipTypeID="22456" />
          <row characterID="878728887" characterName="Kal Shakai" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-4.6" damageDone="0" finalBlow="0" weaponTypeID="2559" shipTypeID="11957" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="2454" flag="87" qtyDropped="5" qtyDestroyed="0" />
          <row typeID="7331" flag="0" qtyDropped="2" qtyDestroyed="2" />
          <row typeID="230" flag="0" qtyDropped="479" qtyDestroyed="159" />
          <row typeID="4029" flag="0" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="4569" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="16375" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="5601" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="12056" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="16383" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="230" flag="5" qtyDropped="0" qtyDestroyed="1704" />
        </rowset>
      </row>
      <row killID="6371324" solarSystemID="30003321" killTime="2009-04-01 00:47:00" moonID="0">
        <victim characterID="1798934072" characterName="Dreadful Rorq" corporationID="1000171" corporationName="Republic University" allianceID="0" allianceName="" factionID="0" factionName="" damageTaken="398" shipTypeID="588" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="372559142" characterName="Knat" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.75698474214155" damageDone="398" finalBlow="1" weaponTypeID="2977" shipTypeID="11371" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="3651" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="3636" flag="0" qtyDropped="1" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6370572" solarSystemID="30003831" killTime="2009-03-31 23:39:00" moonID="0">
        <victim characterID="1511184505" characterName="Thor's Fury" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="299" shipTypeID="596" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="0" characterName="" corporationID="1000120" corporationName="Federation Navy" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0" damageDone="299" finalBlow="1" weaponTypeID="0" shipTypeID="10056" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="3651" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="3634" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="34" flag="5" qtyDropped="0" qtyDestroyed="1" />
        </rowset>
      </row>
      <row killID="6370510" solarSystemID="30003277" killTime="2009-03-31 23:33:00" moonID="0">
        <victim characterID="1511184505" characterName="Thor's Fury" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="233" shipTypeID="589" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="725122352" characterName="Kel Solaar" corporationID="838258154" corporationName="Einherjar Rising" allianceID="703129312" allianceName="Cry Havoc." factionID="0" factionName="" securityStatus="0.0628946339293623" damageDone="233" finalBlow="1" weaponTypeID="2889" shipTypeID="22456" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="451" flag="0" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="434" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="5405" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="246" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="1445" flag="0" qtyDropped="0" qtyDestroyed="2" />
        </rowset>
      </row>
      <row killID="6370507" solarSystemID="30003321" killTime="2009-03-31 23:33:00" moonID="0">
        <victim characterID="1707320548" characterName="wreoiuwoeiruwer" corporationID="1000115" corporationName="University of Caille" allianceID="0" allianceName="" factionID="0" factionName="" damageTaken="266" shipTypeID="606" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1788740659" characterName="Qween Cleopatra" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.33478689522677" damageDone="266" finalBlow="1" weaponTypeID="3170" shipTypeID="12042" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="3651" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="3640" flag="0" qtyDropped="0" qtyDestroyed="1" />
        </rowset>
      </row>
      <row killID="6370365" solarSystemID="30003320" killTime="2009-03-31 23:22:00" moonID="0">
        <victim characterID="1818790777" characterName="CaribouCourse" corporationID="1000115" corporationName="University of Caille" allianceID="0" allianceName="" factionID="0" factionName="" damageTaken="103" shipTypeID="606" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1788740659" characterName="Qween Cleopatra" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.33478689522677" damageDone="103" finalBlow="1" weaponTypeID="3170" shipTypeID="11200" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="3651" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="3640" flag="0" qtyDropped="1" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6369613" solarSystemID="30003320" killTime="2009-03-31 22:20:00" moonID="0">
        <victim characterID="878728887" characterName="Kal Shakai" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="15154" shipTypeID="24702" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1440965095" characterName="MadMamma" corporationID="1677789023" corporationName="Meltd0wn" allianceID="295773986" allianceName="Imperial Republic Of the North" factionID="0" factionName="" securityStatus="3.19880600107366" damageDone="8198" finalBlow="1" weaponTypeID="3138" shipTypeID="16227" />
          <row characterID="500079254" characterName="ToxicAid" corporationID="252480084" corporationName="Sensus Numinis" allianceID="295773986" allianceName="Imperial Republic Of the North" factionID="0" factionName="" securityStatus="5" damageDone="6173" finalBlow="0" weaponTypeID="2410" shipTypeID="11995" />
          <row characterID="284097085" characterName="LordAvatar" corporationID="252480084" corporationName="Sensus Numinis" allianceID="295773986" allianceName="Imperial Republic Of the North" factionID="0" factionName="" securityStatus="4.8" damageDone="446" finalBlow="0" weaponTypeID="3033" shipTypeID="670" />
          <row characterID="1860852979" characterName="sonur" corporationID="252480084" corporationName="Sensus Numinis" allianceID="295773986" allianceName="Imperial Republic Of the North" factionID="0" factionName="" securityStatus="2.1" damageDone="337" finalBlow="0" weaponTypeID="3244" shipTypeID="11178" />
          <row characterID="281722300" characterName="Jonny Dep" corporationID="1677789023" corporationName="Meltd0wn" allianceID="295773986" allianceName="Imperial Republic Of the North" factionID="0" factionName="" securityStatus="-0.9" damageDone="0" finalBlow="0" weaponTypeID="2575" shipTypeID="670" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="21937" flag="5" qtyDropped="300" qtyDestroyed="0" />
          <row typeID="12265" flag="0" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="1952" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="519" flag="0" qtyDropped="0" qtyDestroyed="3" />
          <row typeID="3244" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="12076" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="527" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="21896" flag="0" qtyDropped="0" qtyDestroyed="6" />
          <row typeID="2969" flag="0" qtyDropped="4" qtyDestroyed="2" />
          <row typeID="2048" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="11269" flag="0" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="29011" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="21904" flag="5" qtyDropped="0" qtyDestroyed="660" />
          <row typeID="21896" flag="5" qtyDropped="540" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6369583" solarSystemID="30003320" killTime="2009-03-31 22:17:00" moonID="0">
        <victim characterID="1868072702" characterName="Rockstara" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="15056" shipTypeID="16229" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="500079254" characterName="ToxicAid" corporationID="252480084" corporationName="Sensus Numinis" allianceID="295773986" allianceName="Imperial Republic Of the North" factionID="0" factionName="" securityStatus="5.00373985283113" damageDone="2394" finalBlow="1" weaponTypeID="27441" shipTypeID="11995" />
          <row characterID="244544610" characterName="Raist Varis" corporationID="252480084" corporationName="Sensus Numinis" allianceID="295773986" allianceName="Imperial Republic Of the North" factionID="0" factionName="" securityStatus="5" damageDone="7073" finalBlow="0" weaponTypeID="21640" shipTypeID="24696" />
          <row characterID="154792017" characterName="Echnathonn" corporationID="252480084" corporationName="Sensus Numinis" allianceID="295773986" allianceName="Imperial Republic Of the North" factionID="0" factionName="" securityStatus="5" damageDone="3568" finalBlow="0" weaponTypeID="21640" shipTypeID="12023" />
          <row characterID="284097085" characterName="LordAvatar" corporationID="252480084" corporationName="Sensus Numinis" allianceID="295773986" allianceName="Imperial Republic Of the North" factionID="0" factionName="" securityStatus="4.8" damageDone="2021" finalBlow="0" weaponTypeID="11393" shipTypeID="11393" />
          <row characterID="1440965095" characterName="MadMamma" corporationID="1677789023" corporationName="Meltd0wn" allianceID="295773986" allianceName="Imperial Republic Of the North" factionID="0" factionName="" securityStatus="3.2" damageDone="0" finalBlow="0" weaponTypeID="16227" shipTypeID="16227" />
          <row characterID="1534143764" characterName="Mariejoyanna" corporationID="1677789023" corporationName="Meltd0wn" allianceID="295773986" allianceName="Imperial Republic Of the North" factionID="0" factionName="" securityStatus="1.5" damageDone="0" finalBlow="0" weaponTypeID="11957" shipTypeID="670" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="29009" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="7369" flag="0" qtyDropped="5" qtyDestroyed="2" />
          <row typeID="3244" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="23025" flag="0" qtyDropped="104" qtyDestroyed="78" />
          <row typeID="527" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="1353" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="12052" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="10190" flag="0" qtyDropped="1" qtyDestroyed="2" />
          <row typeID="1541" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="29011" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="23025" flag="5" qtyDropped="0" qtyDestroyed="300" />
          <row typeID="6157" flag="0" qtyDropped="1" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6369577" solarSystemID="30003320" killTime="2009-03-31 22:17:00" moonID="0">
        <victim characterID="1534143764" characterName="Mariejoyanna" corporationID="1677789023" corporationName="Meltd0wn" allianceID="295773986" allianceName="Imperial Republic Of the North" factionID="0" factionName="" damageTaken="4376" shipTypeID="11957" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1868072702" characterName="Rockstara" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.16413218385954" damageDone="889" finalBlow="1" weaponTypeID="7369" shipTypeID="16229" />
          <row characterID="878728887" characterName="Kal Shakai" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-4.6" damageDone="1872" finalBlow="0" weaponTypeID="24702" shipTypeID="24702" />
          <row characterID="246573211" characterName="Ydoc Llezsor" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0.4" damageDone="990" finalBlow="0" weaponTypeID="12003" shipTypeID="12003" />
          <row characterID="702180569" characterName="BoomEZ" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="2.2" damageDone="494" finalBlow="0" weaponTypeID="21640" shipTypeID="16229" />
          <row characterID="1788740659" characterName="Qween Cleopatra" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.3" damageDone="131" finalBlow="0" weaponTypeID="2466" shipTypeID="11200" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="25563" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="29009" flag="5" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="1952" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="12076" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="2563" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="26106" flag="0" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="21096" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2575" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="11325" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2571" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="16273" flag="5" qtyDropped="270" qtyDestroyed="0" />
          <row typeID="11578" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="29011" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="9784" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="2559" flag="0" qtyDropped="0" qtyDestroyed="1" />
        </rowset>
      </row>
      <row killID="6369552" solarSystemID="30003320" killTime="2009-03-31 22:15:00" moonID="0">
        <victim characterID="538844384" characterName="Lazer Rex" corporationID="1677789023" corporationName="Meltd0wn" allianceID="295773986" allianceName="Imperial Republic Of the North" factionID="0" factionName="" damageTaken="1284" shipTypeID="11186" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1788740659" characterName="Qween Cleopatra" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.33478689522677" damageDone="1284" finalBlow="1" weaponTypeID="3170" shipTypeID="11200" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="3178" flag="5" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="448" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3244" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="239" flag="0" qtyDropped="2" qtyDestroyed="1" />
          <row typeID="12058" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="1236" flag="0" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="3001" flag="0" qtyDropped="1" qtyDestroyed="2" />
          <row typeID="3530" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="2048" flag="5" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2185" flag="5" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="440" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="4029" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="2605" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="11267" flag="5" qtyDropped="1" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6365268" solarSystemID="30004500" killTime="2009-03-31 18:20:00" moonID="0">
        <victim characterID="1818790777" characterName="CaribouCourse" corporationID="1000115" corporationName="University of Caille" allianceID="0" allianceName="" factionID="0" factionName="" damageTaken="114" shipTypeID="606" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="476777753" characterName="Heimdal Galplen" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.89756758574854" damageDone="114" finalBlow="1" weaponTypeID="2889" shipTypeID="11198" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="3651" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="34" flag="5" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="3640" flag="0" qtyDropped="0" qtyDestroyed="1" />
        </rowset>
      </row>
      <row killID="6364439" solarSystemID="30004127" killTime="2009-03-31 17:10:00" moonID="0">
        <victim characterID="955882727" characterName="Arancia Detto" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="368" shipTypeID="588" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="0" characterName="" corporationID="1000084" corporationName="Amarr Navy" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0" damageDone="368" finalBlow="1" weaponTypeID="0" shipTypeID="9998" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="3651" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="34" flag="5" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="3636" flag="0" qtyDropped="1" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6364027" solarSystemID="30003504" killTime="2009-03-31 16:29:00" moonID="0">
        <victim characterID="955882727" characterName="Arancia Detto" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="566" shipTypeID="11132" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="0" characterName="" corporationID="1000088" corporationName="Sarum Family" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0" damageDone="566" finalBlow="1" weaponTypeID="0" shipTypeID="10092" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6361293" solarSystemID="30001046" killTime="2009-03-31 08:58:00" moonID="0">
        <victim characterID="888777367" characterName="KellyMargret Ackerman" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="1577" shipTypeID="19744" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="612356734" characterName="yakks" corporationID="976157507" corporationName="SPORADIC MOVEMENT" allianceID="1912505204" allianceName="Cruor-Salax Legion" factionID="0" factionName="" securityStatus="-8.3795459855755" damageDone="1577" finalBlow="1" weaponTypeID="3057" shipTypeID="24692" />
          <row characterID="308265056" characterName="Fishslapper" corporationID="976157507" corporationName="SPORADIC MOVEMENT" allianceID="1912505204" allianceName="Cruor-Salax Legion" factionID="0" factionName="" securityStatus="-0.9" damageDone="0" finalBlow="0" weaponTypeID="19952" shipTypeID="11957" />
          <row characterID="946826035" characterName="Antallis" corporationID="976157507" corporationName="SPORADIC MOVEMENT" allianceID="1912505204" allianceName="Cruor-Salax Legion" factionID="0" factionName="" securityStatus="1" damageDone="0" finalBlow="0" weaponTypeID="5403" shipTypeID="24698" />
          <row characterID="1787158306" characterName="Pace eGuerra" corporationID="976157507" corporationName="SPORADIC MOVEMENT" allianceID="1912505204" allianceName="Cruor-Salax Legion" factionID="0" factionName="" securityStatus="0.6" damageDone="0" finalBlow="0" weaponTypeID="3178" shipTypeID="12042" />
          <row characterID="178200679" characterName="BlakPhoenix" corporationID="976157507" corporationName="SPORADIC MOVEMENT" allianceID="1912505204" allianceName="Cruor-Salax Legion" factionID="0" factionName="" securityStatus="0.1" damageDone="0" finalBlow="0" weaponTypeID="564" shipTypeID="594" />
          <row characterID="801539103" characterName="SlickShoe" corporationID="976157507" corporationName="SPORADIC MOVEMENT" allianceID="1912505204" allianceName="Cruor-Salax Legion" factionID="0" factionName="" securityStatus="-4.3" damageDone="0" finalBlow="0" weaponTypeID="28654" shipTypeID="12021" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="1403" flag="0" qtyDropped="1" qtyDestroyed="2" />
          <row typeID="2046" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="11267" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="578" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="12056" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="8397" flag="0" qtyDropped="1" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6358805" solarSystemID="30003277" killTime="2009-03-31 03:23:00" moonID="0">
        <victim characterID="715132474" characterName="SilverHawk1" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="326" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="734121227" characterName="Raith Dresden" corporationID="838258154" corporationName="Einherjar Rising" allianceID="703129312" allianceName="Cry Havoc." factionID="0" factionName="" securityStatus="-0.0220461206064337" damageDone="246" finalBlow="1" weaponTypeID="27441" shipTypeID="11995" />
          <row characterID="855247117" characterName="EvilDobar" corporationID="838258154" corporationName="Einherjar Rising" allianceID="703129312" allianceName="Cry Havoc." factionID="0" factionName="" securityStatus="-0.1" damageDone="80" finalBlow="0" weaponTypeID="12003" shipTypeID="12003" />
          <row characterID="951713546" characterName="Major Spaz" corporationID="246216857" corporationName="Multiversal Enterprise Inc." allianceID="703129312" allianceName="Cry Havoc." factionID="0" factionName="" securityStatus="1.3" damageDone="0" finalBlow="0" weaponTypeID="2410" shipTypeID="22470" />
          <row characterID="795719561" characterName="Drakthzt" corporationID="838258154" corporationName="Einherjar Rising" allianceID="703129312" allianceName="Cry Havoc." factionID="0" factionName="" securityStatus="-1.8" damageDone="0" finalBlow="0" weaponTypeID="7993" shipTypeID="11176" />
          <row characterID="937203263" characterName="Malcomtempt" corporationID="838258154" corporationName="Einherjar Rising" allianceID="703129312" allianceName="Cry Havoc." factionID="0" factionName="" securityStatus="0.7" damageDone="0" finalBlow="0" weaponTypeID="2404" shipTypeID="11978" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6358793" solarSystemID="30003277" killTime="2009-03-31 03:22:00" moonID="0">
        <victim characterID="715132474" characterName="SilverHawk1" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="26068" shipTypeID="11995" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="734121227" characterName="Raith Dresden" corporationID="838258154" corporationName="Einherjar Rising" allianceID="703129312" allianceName="Cry Havoc." factionID="0" factionName="" securityStatus="-0.0220461206064337" damageDone="1449" finalBlow="1" weaponTypeID="27441" shipTypeID="11995" />
          <row characterID="951713546" characterName="Major Spaz" corporationID="246216857" corporationName="Multiversal Enterprise Inc." allianceID="703129312" allianceName="Cry Havoc." factionID="0" factionName="" securityStatus="1.3" damageDone="10074" finalBlow="0" weaponTypeID="27441" shipTypeID="22470" />
          <row characterID="695332547" characterName="Undaunted Death" corporationID="838258154" corporationName="Einherjar Rising" allianceID="703129312" allianceName="Cry Havoc." factionID="0" factionName="" securityStatus="-2" damageDone="3957" finalBlow="0" weaponTypeID="12017" shipTypeID="12017" />
          <row characterID="404896821" characterName="Kilt Ness" corporationID="838258154" corporationName="Einherjar Rising" allianceID="703129312" allianceName="Cry Havoc." factionID="0" factionName="" securityStatus="0.7" damageDone="2554" finalBlow="0" weaponTypeID="24509" shipTypeID="11993" />
          <row characterID="996304366" characterName="Mungkee" corporationID="838258154" corporationName="Einherjar Rising" allianceID="703129312" allianceName="Cry Havoc." factionID="0" factionName="" securityStatus="-0.6" damageDone="1669" finalBlow="0" weaponTypeID="3244" shipTypeID="12003" />
          <row characterID="795719561" characterName="Drakthzt" corporationID="838258154" corporationName="Einherjar Rising" allianceID="703129312" allianceName="Cry Havoc." factionID="0" factionName="" securityStatus="-1.8" damageDone="1512" finalBlow="0" weaponTypeID="27361" shipTypeID="11176" />
          <row characterID="769898528" characterName="CarbonFury" corporationID="838258154" corporationName="Einherjar Rising" allianceID="703129312" allianceName="Cry Havoc." factionID="0" factionName="" securityStatus="0.6" damageDone="1292" finalBlow="0" weaponTypeID="2488" shipTypeID="11978" />
          <row characterID="672559179" characterName="Cuny" corporationID="838258154" corporationName="Einherjar Rising" allianceID="703129312" allianceName="Cry Havoc." factionID="0" factionName="" securityStatus="-0.3" damageDone="1290" finalBlow="0" weaponTypeID="27435" shipTypeID="11995" />
          <row characterID="855247117" characterName="EvilDobar" corporationID="838258154" corporationName="Einherjar Rising" allianceID="703129312" allianceName="Cry Havoc." factionID="0" factionName="" securityStatus="-0.1" damageDone="1084" finalBlow="0" weaponTypeID="12003" shipTypeID="12003" />
          <row characterID="605972357" characterName="Kalis Vanos" corporationID="838258154" corporationName="Einherjar Rising" allianceID="703129312" allianceName="Cry Havoc." factionID="0" factionName="" securityStatus="4" damageDone="1055" finalBlow="0" weaponTypeID="24696" shipTypeID="24696" />
          <row characterID="937203263" characterName="Malcomtempt" corporationID="838258154" corporationName="Einherjar Rising" allianceID="703129312" allianceName="Cry Havoc." factionID="0" factionName="" securityStatus="0.7" damageDone="132" finalBlow="0" weaponTypeID="2488" shipTypeID="11978" />
          <row characterID="1530564077" characterName="Brice Pierce" corporationID="838258154" corporationName="Einherjar Rising" allianceID="703129312" allianceName="Cry Havoc." factionID="0" factionName="" securityStatus="0.8" damageDone="0" finalBlow="0" weaponTypeID="2571" shipTypeID="11957" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="27441" flag="5" qtyDropped="982" qtyDestroyed="0" />
          <row typeID="2281" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="2048" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="29003" flag="5" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="27441" flag="0" qtyDropped="31" qtyDestroyed="124" />
          <row typeID="2301" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="28654" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="1541" flag="0" qtyDropped="0" qtyDestroyed="3" />
          <row typeID="2410" flag="0" qtyDropped="2" qtyDestroyed="3" />
          <row typeID="3841" flag="0" qtyDropped="1" qtyDestroyed="3" />
          <row typeID="26084" flag="0" qtyDropped="0" qtyDestroyed="2" />
        </rowset>
      </row>
      <row killID="6358734" solarSystemID="30004504" killTime="2009-03-31 03:17:00" moonID="0">
        <victim characterID="1868072702" characterName="Rockstara" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="438" shipTypeID="601" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="204030014" characterName="BATTYMANNTHE DETSROYER" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="-1.45003752862487" damageDone="438" finalBlow="1" weaponTypeID="7369" shipTypeID="623" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="3651" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="34" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3638" flag="0" qtyDropped="1" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6358707" solarSystemID="30004504" killTime="2009-03-31 03:14:00" moonID="0">
        <victim characterID="975223932" characterName="Nytemaster" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" damageTaken="8118" shipTypeID="622" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="233991150" characterName="Maelgar" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.70885186831252" damageDone="3674" finalBlow="1" weaponTypeID="3170" shipTypeID="12044" />
          <row characterID="878728887" characterName="Kal Shakai" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-4.6" damageDone="4023" finalBlow="0" weaponTypeID="27315" shipTypeID="11400" />
          <row characterID="1868072702" characterName="Rockstara" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.2" damageDone="421" finalBlow="0" weaponTypeID="2488" shipTypeID="670" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="23707" flag="87" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="9141" flag="0" qtyDropped="3" qtyDestroyed="1" />
          <row typeID="533" flag="0" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="12052" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="193" flag="5" qtyDropped="3664" qtyDestroyed="0" />
          <row typeID="5399" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="1244" flag="0" qtyDropped="1" qtyDestroyed="2" />
          <row typeID="3841" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="193" flag="0" qtyDropped="64" qtyDestroyed="66" />
        </rowset>
      </row>
      <row killID="6358700" solarSystemID="30004504" killTime="2009-03-31 03:14:00" moonID="0">
        <victim characterID="1868072702" characterName="Rockstara" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="2315" shipTypeID="11200" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="193006176" characterName="Just Laz" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="-0.848236094743098" damageDone="692" finalBlow="1" weaponTypeID="489" shipTypeID="629" />
          <row characterID="753077177" characterName="RahAh nZanhOrR" corporationID="635652829" corporationName="The Empire Nation" allianceID="1345801112" allianceName="Dead Mans Hand" factionID="0" factionName="" securityStatus="5" damageDone="844" finalBlow="0" weaponTypeID="5299" shipTypeID="0" />
          <row characterID="975223932" characterName="Nytemaster" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="-1.6" damageDone="595" finalBlow="0" weaponTypeID="5399" shipTypeID="622" />
          <row characterID="719896106" characterName="NICKANATOR" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="-3.3" damageDone="174" finalBlow="0" weaponTypeID="209" shipTypeID="621" />
          <row characterID="204030014" characterName="BATTYMANNTHE DETSROYER" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="-1.5" damageDone="10" finalBlow="0" weaponTypeID="209" shipTypeID="623" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="28668" flag="5" qtyDropped="0" qtyDestroyed="31" />
          <row typeID="448" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="5973" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="12612" flag="5" qtyDropped="416" qtyDestroyed="0" />
          <row typeID="23009" flag="5" qtyDropped="0" qtyDestroyed="433" />
          <row typeID="2605" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="27377" flag="5" qtyDropped="253" qtyDestroyed="22" />
          <row typeID="16517" flag="5" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="27423" flag="5" qtyDropped="683" qtyDestroyed="0" />
          <row typeID="527" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="29011" flag="5" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="12614" flag="5" qtyDropped="0" qtyDestroyed="397" />
          <row typeID="25861" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="23009" flag="0" qtyDropped="0" qtyDestroyed="318" />
          <row typeID="2048" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="8747" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3170" flag="0" qtyDropped="0" qtyDestroyed="3" />
          <row typeID="10190" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="27395" flag="5" qtyDropped="0" qtyDestroyed="137" />
          <row typeID="581" flag="5" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2454" flag="5" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="29013" flag="5" qtyDropped="1" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6358617" solarSystemID="30004504" killTime="2009-03-31 03:05:00" moonID="0">
        <victim characterID="753077177" characterName="RahAh nZanhOrR" corporationID="635652829" corporationName="The Empire Nation" allianceID="1345801112" allianceName="Dead Mans Hand" factionID="0" factionName="" damageTaken="1125" shipTypeID="11377" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1868072702" characterName="Rockstara" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.18202342133367" damageDone="1125" finalBlow="1" weaponTypeID="3170" shipTypeID="11200" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="27377" flag="5" qtyDropped="231" qtyDestroyed="0" />
          <row typeID="1952" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="581" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="29013" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="5299" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="27377" flag="0" qtyDropped="44" qtyDestroyed="22" />
          <row typeID="27423" flag="5" qtyDropped="683" qtyDestroyed="0" />
          <row typeID="8747" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="22291" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="11577" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="26016" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="26030" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="16517" flag="0" qtyDropped="1" qtyDestroyed="2" />
          <row typeID="29011" flag="0" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="6157" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="27395" flag="5" qtyDropped="137" qtyDestroyed="754" />
        </rowset>
      </row>
      <row killID="6358035" solarSystemID="30003277" killTime="2009-03-31 02:17:00" moonID="0">
        <victim characterID="795531096" characterName="Kadashnikov" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="42" shipTypeID="11132" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="769898528" characterName="CarbonFury" corporationID="838258154" corporationName="Einherjar Rising" allianceID="703129312" allianceName="Cry Havoc." factionID="0" factionName="" securityStatus="0.641281990405148" damageDone="42" finalBlow="1" weaponTypeID="21640" shipTypeID="11978" />
          <row characterID="795719561" characterName="Drakthzt" corporationID="838258154" corporationName="Einherjar Rising" allianceID="703129312" allianceName="Cry Havoc." factionID="0" factionName="" securityStatus="-1.8" damageDone="0" finalBlow="0" weaponTypeID="7993" shipTypeID="11176" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6356461" solarSystemID="30004497" killTime="2009-03-30 23:56:00" moonID="0">
        <victim characterID="1591604456" characterName="bilko131" corporationID="1126222189" corporationName="Lions Of Judah" allianceID="173739862" allianceName="Veritas Immortalis" factionID="0" factionName="" damageTaken="414" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1788740659" characterName="Qween Cleopatra" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.33478689522677" damageDone="194" finalBlow="1" weaponTypeID="3170" shipTypeID="12042" />
          <row characterID="878728887" characterName="Kal Shakai" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-4.5" damageDone="220" finalBlow="0" weaponTypeID="27315" shipTypeID="11400" />
          <row characterID="713172734" characterName="Nicomedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="5" damageDone="0" finalBlow="0" weaponTypeID="2410" shipTypeID="11993" />
          <row characterID="246573211" characterName="Ydoc Llezsor" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0.6" damageDone="0" finalBlow="0" weaponTypeID="3244" shipTypeID="12003" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6355584" solarSystemID="30003278" killTime="2009-03-30 22:50:00" moonID="0">
        <victim characterID="741562243" characterName="jeriwo" corporationID="684116024" corporationName="Solar Dragons" allianceID="1208295500" allianceName="SOLAR FLEET" factionID="0" factionName="" damageTaken="1081" shipTypeID="11184" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1788740659" characterName="Qween Cleopatra" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.33478689522677" damageDone="1081" finalBlow="1" weaponTypeID="3170" shipTypeID="11200" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="2446" flag="5" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="1447" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="5973" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="12565" flag="0" qtyDropped="0" qtyDestroyed="4" />
          <row typeID="12767" flag="5" qtyDropped="0" qtyDestroyed="1248" />
          <row typeID="5443" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="21896" flag="5" qtyDropped="4" qtyDestroyed="4" />
          <row typeID="23071" flag="5" qtyDropped="0" qtyDestroyed="4" />
          <row typeID="1236" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="3001" flag="0" qtyDropped="1" qtyDestroyed="3" />
          <row typeID="2364" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="1183" flag="0" qtyDropped="1" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6354056" solarSystemID="30003322" killTime="2009-03-30 21:07:00" moonID="0">
        <victim characterID="596410404" characterName="Miya Kimiko" corporationID="718092388" corporationName="Bulgarian Mafia Squad" allianceID="264679431" allianceName="Sons of Tangra" factionID="0" factionName="" damageTaken="447" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="148511261" characterName="Teister" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="1.42230299738558" damageDone="447" finalBlow="1" weaponTypeID="2977" shipTypeID="11371" />
          <row characterID="823357545" characterName="The0" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.6" damageDone="0" finalBlow="0" weaponTypeID="3244" shipTypeID="11198" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6353974" solarSystemID="30004493" killTime="2009-03-30 21:04:00" moonID="0">
        <victim characterID="1299079289" characterName="bountboy" corporationID="1216230500" corporationName="Vitriol Ventures" allianceID="173739862" allianceName="Veritas Immortalis" factionID="0" factionName="" damageTaken="317" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="149816009" characterName="Jaedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-3.87968674437454" damageDone="317" finalBlow="1" weaponTypeID="2817" shipTypeID="11365" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6353836" solarSystemID="30003322" killTime="2009-03-30 20:56:00" moonID="0">
        <victim characterID="1784800199" characterName="skenoske" corporationID="718092388" corporationName="Bulgarian Mafia Squad" allianceID="264679431" allianceName="Sons of Tangra" factionID="0" factionName="" damageTaken="181" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="502417576" characterName="AyuTokin Tumi" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.35047124870897" damageDone="181" finalBlow="1" weaponTypeID="3170" shipTypeID="11200" />
          <row characterID="823357545" characterName="The0" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.6" damageDone="0" finalBlow="0" weaponTypeID="3244" shipTypeID="11198" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6353811" solarSystemID="30003322" killTime="2009-03-30 20:55:00" moonID="0">
        <victim characterID="713029960" characterName="Admiral Traun" corporationID="263585335" corporationName="Black Omega Security" allianceID="386292982" allianceName="Pandemic Legion" factionID="0" factionName="" damageTaken="125" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="148511261" characterName="Teister" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="1.42230299738558" damageDone="125" finalBlow="1" weaponTypeID="2977" shipTypeID="11371" />
          <row characterID="406827565" characterName="fnar g" corporationID="994852997" corporationName="Mortis Angelus" allianceID="833571739" allianceName="The Church." factionID="0" factionName="" securityStatus="-7.4" damageDone="0" finalBlow="0" weaponTypeID="22778" shipTypeID="22460" />
          <row characterID="761644878" characterName="Nkalv" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.3" damageDone="0" finalBlow="0" weaponTypeID="2881" shipTypeID="11400" />
          <row characterID="823357545" characterName="The0" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.6" damageDone="0" finalBlow="0" weaponTypeID="3244" shipTypeID="11198" />
          <row characterID="167284938" characterName="Silurus" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.6" damageDone="0" finalBlow="0" weaponTypeID="2889" shipTypeID="11371" />
          <row characterID="702180569" characterName="BoomEZ" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="2.2" damageDone="0" finalBlow="0" weaponTypeID="3178" shipTypeID="11200" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6353810" solarSystemID="30003322" killTime="2009-03-30 20:55:00" moonID="0">
        <victim characterID="1784800199" characterName="skenoske" corporationID="718092388" corporationName="Bulgarian Mafia Squad" allianceID="264679431" allianceName="Sons of Tangra" factionID="0" factionName="" damageTaken="5007" shipTypeID="11957" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="167284938" characterName="Silurus" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.59633001464344" damageDone="1490" finalBlow="1" weaponTypeID="2889" shipTypeID="11371" />
          <row characterID="1031466230" characterName="Waxau" corporationID="994852997" corporationName="Mortis Angelus" allianceID="833571739" allianceName="The Church." factionID="0" factionName="" securityStatus="-3" damageDone="1802" finalBlow="0" weaponTypeID="12003" shipTypeID="12003" />
          <row characterID="675430303" characterName="Unleashed CSK" corporationID="994852997" corporationName="Mortis Angelus" allianceID="833571739" allianceName="The Church." factionID="0" factionName="" securityStatus="-2.6" damageDone="448" finalBlow="0" weaponTypeID="2488" shipTypeID="0" />
          <row characterID="148511261" characterName="Teister" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="1.4" damageDone="354" finalBlow="0" weaponTypeID="11371" shipTypeID="11371" />
          <row characterID="365949102" characterName="Fumb Duck" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-0.1" damageDone="340" finalBlow="0" weaponTypeID="17812" shipTypeID="17812" />
          <row characterID="878728887" characterName="Kal Shakai" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-4.5" damageDone="314" finalBlow="0" weaponTypeID="22456" shipTypeID="22456" />
          <row characterID="296223009" characterName="BobTeh" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-2" damageDone="175" finalBlow="0" weaponTypeID="11198" shipTypeID="11198" />
          <row characterID="823357545" characterName="The0" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.6" damageDone="84" finalBlow="0" weaponTypeID="11198" shipTypeID="11198" />
          <row characterID="338577989" characterName="Jhagiti Tyran" corporationID="994852997" corporationName="Mortis Angelus" allianceID="833571739" allianceName="The Church." factionID="0" factionName="" securityStatus="-6.4" damageDone="0" finalBlow="0" weaponTypeID="19946" shipTypeID="11957" />
          <row characterID="713172734" characterName="Nicomedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="5" damageDone="0" finalBlow="0" weaponTypeID="11194" shipTypeID="11194" />
          <row characterID="733510782" characterName="saylum" corporationID="994852997" corporationName="Mortis Angelus" allianceID="833571739" allianceName="The Church." factionID="0" factionName="" securityStatus="-1.8" damageDone="0" finalBlow="0" weaponTypeID="19806" shipTypeID="11993" />
          <row characterID="1987189746" characterName="Papa Murphy" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="4" damageDone="0" finalBlow="0" weaponTypeID="587" shipTypeID="587" />
          <row characterID="502417576" characterName="AyuTokin Tumi" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.4" damageDone="0" finalBlow="0" weaponTypeID="2488" shipTypeID="11200" />
          <row characterID="1788740659" characterName="Qween Cleopatra" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.3" damageDone="0" finalBlow="0" weaponTypeID="19939" shipTypeID="11957" />
          <row characterID="702180569" characterName="BoomEZ" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="2.2" damageDone="0" finalBlow="0" weaponTypeID="11200" shipTypeID="11200" />
          <row characterID="761644878" characterName="Nkalv" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.3" damageDone="0" finalBlow="0" weaponTypeID="527" shipTypeID="11400" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="17765" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="2563" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="2575" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2516" flag="5" qtyDropped="0" qtyDestroyed="200" />
          <row typeID="29011" flag="5" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2559" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="25563" flag="0" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="16521" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="2512" flag="5" qtyDropped="0" qtyDestroyed="123" />
          <row typeID="26106" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="29009" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="6159" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="11325" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="12052" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="25861" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2488" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="265" flag="0" qtyDropped="0" qtyDestroyed="20" />
          <row typeID="2571" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="7329" flag="5" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="26108" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="17938" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="19939" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="11578" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="265" flag="5" qtyDropped="0" qtyDestroyed="180" />
          <row typeID="6173" flag="5" qtyDropped="0" qtyDestroyed="1" />
        </rowset>
      </row>
      <row killID="6353788" solarSystemID="30003322" killTime="2009-03-30 20:54:00" moonID="0">
        <victim characterID="713029960" characterName="Admiral Traun" corporationID="263585335" corporationName="Black Omega Security" allianceID="386292982" allianceName="Pandemic Legion" factionID="0" factionName="" damageTaken="4530" shipTypeID="11978" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="761644878" characterName="Nkalv" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.25427825608947" damageDone="133" finalBlow="1" weaponTypeID="2881" shipTypeID="11400" />
          <row characterID="733510782" characterName="saylum" corporationID="994852997" corporationName="Mortis Angelus" allianceID="833571739" allianceName="The Church." factionID="0" factionName="" securityStatus="-1.8" damageDone="1768" finalBlow="0" weaponTypeID="27453" shipTypeID="11993" />
          <row characterID="702180569" characterName="BoomEZ" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="2.2" damageDone="801" finalBlow="0" weaponTypeID="2456" shipTypeID="11200" />
          <row characterID="502417576" characterName="AyuTokin Tumi" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.4" damageDone="635" finalBlow="0" weaponTypeID="2488" shipTypeID="11200" />
          <row characterID="148511261" characterName="Teister" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="1.4" damageDone="597" finalBlow="0" weaponTypeID="2977" shipTypeID="11371" />
          <row characterID="365949102" characterName="Fumb Duck" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-0.1" damageDone="413" finalBlow="0" weaponTypeID="17812" shipTypeID="17812" />
          <row characterID="823357545" characterName="The0" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.6" damageDone="183" finalBlow="0" weaponTypeID="11198" shipTypeID="11198" />
          <row characterID="1788740659" characterName="Qween Cleopatra" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.3" damageDone="0" finalBlow="0" weaponTypeID="19939" shipTypeID="11957" />
          <row characterID="713172734" characterName="Nicomedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="5" damageDone="0" finalBlow="0" weaponTypeID="11194" shipTypeID="11194" />
          <row characterID="296223009" characterName="BobTeh" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-2" damageDone="0" finalBlow="0" weaponTypeID="2905" shipTypeID="11198" />
          <row characterID="406827565" characterName="fnar g" corporationID="994852997" corporationName="Mortis Angelus" allianceID="833571739" allianceName="The Church." factionID="0" factionName="" securityStatus="-7.4" damageDone="0" finalBlow="0" weaponTypeID="16523" shipTypeID="22460" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="28668" flag="5" qtyDropped="249" qtyDestroyed="0" />
          <row typeID="19131" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="2281" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="1447" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="12773" flag="5" qtyDropped="0" qtyDestroyed="3794" />
          <row typeID="12076" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="11283" flag="0" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="5011" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="10858" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="8641" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="11283" flag="5" qtyDropped="31" qtyDestroyed="0" />
          <row typeID="21896" flag="5" qtyDropped="975" qtyDestroyed="0" />
          <row typeID="3530" flag="5" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="26080" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="3841" flag="5" qtyDropped="0" qtyDestroyed="4" />
          <row typeID="1541" flag="0" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="25948" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2048" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="1405" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3082" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="8583" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="210" flag="5" qtyDropped="89" qtyDestroyed="0" />
          <row typeID="2260" flag="0" qtyDropped="0" qtyDestroyed="1" />
        </rowset>
      </row>
      <row killID="6353582" solarSystemID="30003322" killTime="2009-03-30 20:45:00" moonID="0">
        <victim characterID="839771789" characterName="uzass" corporationID="718092388" corporationName="Bulgarian Mafia Squad" allianceID="264679431" allianceName="Sons of Tangra" factionID="0" factionName="" damageTaken="17724" shipTypeID="11999" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1901781606" characterName="Surielle Zapata" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="0.858838955620167" damageDone="1090" finalBlow="1" weaponTypeID="10680" shipTypeID="11200" />
          <row characterID="1259355159" characterName="TinkerHell" corporationID="994852997" corporationName="Mortis Angelus" allianceID="833571739" allianceName="The Church." factionID="0" factionName="" securityStatus="-0.9" damageDone="6835" finalBlow="0" weaponTypeID="27413" shipTypeID="0" />
          <row characterID="233991150" characterName="Maelgar" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.7" damageDone="2444" finalBlow="0" weaponTypeID="12044" shipTypeID="12044" />
          <row characterID="722088228" characterName="JackCo" corporationID="1588486523" corporationName="Yakuza Corp" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="4.1" damageDone="1566" finalBlow="0" weaponTypeID="2488" shipTypeID="24698" />
          <row characterID="761644878" characterName="Nkalv" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.3" damageDone="1253" finalBlow="0" weaponTypeID="11400" shipTypeID="11400" />
          <row characterID="702180569" characterName="BoomEZ" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="2.2" damageDone="1246" finalBlow="0" weaponTypeID="2456" shipTypeID="11200" />
          <row characterID="148511261" characterName="Teister" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="1.4" damageDone="983" finalBlow="0" weaponTypeID="11371" shipTypeID="11371" />
          <row characterID="823357545" characterName="The0" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.6" damageDone="488" finalBlow="0" weaponTypeID="11198" shipTypeID="11198" />
          <row characterID="365949102" characterName="Fumb Duck" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-0.1" damageDone="451" finalBlow="0" weaponTypeID="17812" shipTypeID="17812" />
          <row characterID="878728887" characterName="Kal Shakai" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-4.5" damageDone="370" finalBlow="0" weaponTypeID="22456" shipTypeID="22456" />
          <row characterID="1328396909" characterName="Forgon" corporationID="994852997" corporationName="Mortis Angelus" allianceID="833571739" allianceName="The Church." factionID="0" factionName="" securityStatus="0.8" damageDone="353" finalBlow="0" weaponTypeID="2488" shipTypeID="22468" />
          <row characterID="246573211" characterName="Ydoc Llezsor" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0.5" damageDone="252" finalBlow="0" weaponTypeID="11184" shipTypeID="11184" />
          <row characterID="296223009" characterName="BobTeh" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-2" damageDone="248" finalBlow="0" weaponTypeID="11198" shipTypeID="11198" />
          <row characterID="808277084" characterName="shhmee eeeeee" corporationID="994852997" corporationName="Mortis Angelus" allianceID="833571739" allianceName="The Church." factionID="0" factionName="" securityStatus="-10" damageDone="113" finalBlow="0" weaponTypeID="2466" shipTypeID="0" />
          <row characterID="1736469556" characterName="Boka Smowl" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="-1.4" damageDone="32" finalBlow="0" weaponTypeID="587" shipTypeID="587" />
          <row characterID="795531096" characterName="Kadashnikov" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="1.7" damageDone="0" finalBlow="0" weaponTypeID="19939" shipTypeID="670" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="519" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="12773" flag="5" qtyDropped="1118" qtyDestroyed="0" />
          <row typeID="3244" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2897" flag="0" qtyDropped="3" qtyDestroyed="2" />
          <row typeID="27435" flag="5" qtyDropped="311" qtyDestroyed="0" />
          <row typeID="1405" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="1236" flag="0" qtyDropped="1" qtyDestroyed="2" />
          <row typeID="27435" flag="0" qtyDropped="0" qtyDestroyed="24" />
          <row typeID="12773" flag="0" qtyDropped="22" qtyDestroyed="33" />
          <row typeID="12076" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="8101" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3841" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="21896" flag="5" qtyDropped="0" qtyDestroyed="500" />
          <row typeID="26070" flag="0" qtyDropped="0" qtyDestroyed="2" />
        </rowset>
      </row>
      <row killID="6353578" solarSystemID="30003322" killTime="2009-03-30 20:44:00" moonID="0">
        <victim characterID="174463942" characterName="NedStark" corporationID="718092388" corporationName="Bulgarian Mafia Squad" allianceID="264679431" allianceName="Sons of Tangra" factionID="0" factionName="" damageTaken="208" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1901781606" characterName="Surielle Zapata" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="0.858838955620167" damageDone="208" finalBlow="1" weaponTypeID="10680" shipTypeID="11200" />
          <row characterID="823357545" characterName="The0" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.6" damageDone="0" finalBlow="0" weaponTypeID="3244" shipTypeID="11198" />
          <row characterID="702180569" characterName="BoomEZ" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="2.2" damageDone="0" finalBlow="0" weaponTypeID="3244" shipTypeID="11200" />
          <row characterID="246573211" characterName="Ydoc Llezsor" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0.5" damageDone="0" finalBlow="0" weaponTypeID="3001" shipTypeID="11184" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6353567" solarSystemID="30003322" killTime="2009-03-30 20:44:00" moonID="0">
        <victim characterID="795531096" characterName="Kadashnikov" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="298" shipTypeID="11194" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="360708245" characterName="Sugledvach" corporationID="718092388" corporationName="Bulgarian Mafia Squad" allianceID="264679431" allianceName="Sons of Tangra" factionID="0" factionName="" securityStatus="2.07436265132203" damageDone="168" finalBlow="1" weaponTypeID="210" shipTypeID="621" />
          <row characterID="1875342788" characterName="zume360" corporationID="718092388" corporationName="Bulgarian Mafia Squad" allianceID="264679431" allianceName="Sons of Tangra" factionID="0" factionName="" securityStatus="5" damageDone="130" finalBlow="0" weaponTypeID="11381" shipTypeID="11381" />
          <row characterID="1784800199" characterName="skenoske" corporationID="718092388" corporationName="Bulgarian Mafia Squad" allianceID="264679431" allianceName="Sons of Tangra" factionID="0" factionName="" securityStatus="2" damageDone="0" finalBlow="0" weaponTypeID="2571" shipTypeID="11957" />
          <row characterID="980579879" characterName="Sontangra" corporationID="718092388" corporationName="Bulgarian Mafia Squad" allianceID="264679431" allianceName="Sons of Tangra" factionID="0" factionName="" securityStatus="2.3" damageDone="0" finalBlow="0" weaponTypeID="2410" shipTypeID="11993" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="25563" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="10631" flag="0" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="19939" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="26106" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2514" flag="5" qtyDropped="0" qtyDestroyed="170" />
          <row typeID="2571" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="19952" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="19927" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="25861" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2516" flag="5" qtyDropped="393" qtyDestroyed="0" />
          <row typeID="2512" flag="5" qtyDropped="686" qtyDestroyed="0" />
          <row typeID="440" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="2512" flag="0" qtyDropped="0" qtyDestroyed="60" />
        </rowset>
      </row>
      <row killID="6353286" solarSystemID="30003349" killTime="2009-03-30 20:29:00" moonID="0">
        <victim characterID="365949102" characterName="Fumb Duck" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="346" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="174463942" characterName="NedStark" corporationID="718092388" corporationName="Bulgarian Mafia Squad" allianceID="264679431" allianceName="Sons of Tangra" factionID="0" factionName="" securityStatus="5.01554276391304" damageDone="346" finalBlow="1" weaponTypeID="3025" shipTypeID="12003" />
          <row characterID="729828059" characterName="Masimo" corporationID="718092388" corporationName="Bulgarian Mafia Squad" allianceID="264679431" allianceName="Sons of Tangra" factionID="0" factionName="" securityStatus="5" damageDone="0" finalBlow="0" weaponTypeID="10680" shipTypeID="11200" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6353255" solarSystemID="30003349" killTime="2009-03-30 20:28:00" moonID="0">
        <victim characterID="365949102" characterName="Fumb Duck" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="1066" shipTypeID="11198" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1281542726" characterName="Staffo 0" corporationID="718092388" corporationName="Bulgarian Mafia Squad" allianceID="264679431" allianceName="Sons of Tangra" factionID="0" factionName="" securityStatus="5.00209080298519" damageDone="499" finalBlow="1" weaponTypeID="27453" shipTypeID="11993" />
          <row characterID="616424509" characterName="Ascharot" corporationID="1541164645" corporationName="Hikage Corporation" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" securityStatus="4.3" damageDone="404" finalBlow="0" weaponTypeID="27441" shipTypeID="0" />
          <row characterID="596410404" characterName="Miya Kimiko" corporationID="718092388" corporationName="Bulgarian Mafia Squad" allianceID="264679431" allianceName="Sons of Tangra" factionID="0" factionName="" securityStatus="-0.9" damageDone="93" finalBlow="0" weaponTypeID="11200" shipTypeID="11200" />
          <row characterID="1406146843" characterName="Vortex Overdrive" corporationID="718092388" corporationName="Bulgarian Mafia Squad" allianceID="264679431" allianceName="Sons of Tangra" factionID="0" factionName="" securityStatus="-0.4" damageDone="70" finalBlow="0" weaponTypeID="11198" shipTypeID="11198" />
          <row characterID="1875342788" characterName="zume360" corporationID="718092388" corporationName="Bulgarian Mafia Squad" allianceID="264679431" allianceName="Sons of Tangra" factionID="0" factionName="" securityStatus="5" damageDone="0" finalBlow="0" weaponTypeID="3074" shipTypeID="11381" />
          <row characterID="1935949660" characterName="DuviBG" corporationID="718092388" corporationName="Bulgarian Mafia Squad" allianceID="264679431" allianceName="Sons of Tangra" factionID="0" factionName="" securityStatus="2.2" damageDone="0" finalBlow="0" weaponTypeID="8865" shipTypeID="587" />
          <row characterID="729828059" characterName="Masimo" corporationID="718092388" corporationName="Bulgarian Mafia Squad" allianceID="264679431" allianceName="Sons of Tangra" factionID="0" factionName="" securityStatus="5" damageDone="0" finalBlow="0" weaponTypeID="10680" shipTypeID="11200" />
          <row characterID="1762098058" characterName="Festina Lente" corporationID="718092388" corporationName="Bulgarian Mafia Squad" allianceID="264679431" allianceName="Sons of Tangra" factionID="0" factionName="" securityStatus="4.9" damageDone="0" finalBlow="0" weaponTypeID="10678" shipTypeID="3766" />
          <row characterID="2013480725" characterName="Diakonu" corporationID="718092388" corporationName="Bulgarian Mafia Squad" allianceID="264679431" allianceName="Sons of Tangra" factionID="0" factionName="" securityStatus="0.1" damageDone="0" finalBlow="0" weaponTypeID="3244" shipTypeID="583" />
          <row characterID="1982495930" characterName="Jack0fShadows" corporationID="718092388" corporationName="Bulgarian Mafia Squad" allianceID="264679431" allianceName="Sons of Tangra" factionID="0" factionName="" securityStatus="4" damageDone="0" finalBlow="0" weaponTypeID="7367" shipTypeID="12011" />
          <row characterID="634382004" characterName="Mahavir" corporationID="718092388" corporationName="Bulgarian Mafia Squad" allianceID="264679431" allianceName="Sons of Tangra" factionID="0" factionName="" securityStatus="-3.1" damageDone="0" finalBlow="0" weaponTypeID="2889" shipTypeID="22456" />
          <row characterID="1319553354" characterName="the POP" corporationID="718092388" corporationName="Bulgarian Mafia Squad" allianceID="264679431" allianceName="Sons of Tangra" factionID="0" factionName="" securityStatus="5" damageDone="0" finalBlow="0" weaponTypeID="3170" shipTypeID="11200" />
          <row characterID="1223335012" characterName="rogerf86" corporationID="1541164645" corporationName="Hikage Corporation" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" securityStatus="0.8" damageDone="0" finalBlow="0" weaponTypeID="11365" shipTypeID="0" />
          <row characterID="869767392" characterName="Emilia Bluu" corporationID="718092388" corporationName="Bulgarian Mafia Squad" allianceID="264679431" allianceName="Sons of Tangra" factionID="0" factionName="" securityStatus="5" damageDone="0" finalBlow="0" weaponTypeID="3242" shipTypeID="593" />
          <row characterID="713029960" characterName="Admiral Traun" corporationID="263585335" corporationName="Black Omega Security" allianceID="386292982" allianceName="Pandemic Legion" factionID="0" factionName="" securityStatus="3.1" damageDone="0" finalBlow="0" weaponTypeID="2185" shipTypeID="11978" />
          <row characterID="925173049" characterName="Raste" corporationID="718092388" corporationName="Bulgarian Mafia Squad" allianceID="264679431" allianceName="Sons of Tangra" factionID="0" factionName="" securityStatus="3" damageDone="0" finalBlow="0" weaponTypeID="2905" shipTypeID="11978" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="29148" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="16523" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="21898" flag="5" qtyDropped="2300" qtyDestroyed="0" />
          <row typeID="448" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2512" flag="5" qtyDropped="677" qtyDestroyed="0" />
          <row typeID="3244" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="22291" flag="5" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="1236" flag="0" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="12625" flag="5" qtyDropped="4762" qtyDestroyed="0" />
          <row typeID="27315" flag="5" qtyDropped="515" qtyDestroyed="0" />
          <row typeID="11563" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="1236" flag="5" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2873" flag="0" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="2516" flag="0" qtyDropped="30" qtyDestroyed="0" />
          <row typeID="12608" flag="5" qtyDropped="1052" qtyDestroyed="0" />
          <row typeID="21898" flag="0" qtyDropped="192" qtyDestroyed="0" />
          <row typeID="2516" flag="5" qtyDropped="0" qtyDestroyed="772" />
          <row typeID="3831" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="440" flag="0" qtyDropped="0" qtyDestroyed="1" />
        </rowset>
      </row>
      <row killID="6353152" solarSystemID="30003349" killTime="2009-03-30 20:23:00" moonID="0">
        <victim characterID="616424509" characterName="Ascharot" corporationID="1541164645" corporationName="Hikage Corporation" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" damageTaken="5560" shipTypeID="11957" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="878728887" characterName="Kal Shakai" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-4.49519294591247" damageDone="4009" finalBlow="1" weaponTypeID="2881" shipTypeID="22456" />
          <row characterID="1788740659" characterName="Qween Cleopatra" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.3" damageDone="853" finalBlow="0" weaponTypeID="2466" shipTypeID="11200" />
          <row characterID="365949102" characterName="Fumb Duck" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-0.1" damageDone="698" finalBlow="0" weaponTypeID="2516" shipTypeID="11198" />
          <row characterID="823357545" characterName="The0" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.6" damageDone="0" finalBlow="0" weaponTypeID="527" shipTypeID="11198" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="29009" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="12076" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2563" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="27441" flag="0" qtyDropped="30" qtyDestroyed="30" />
          <row typeID="23039" flag="5" qtyDropped="0" qtyDestroyed="500" />
          <row typeID="2410" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="2559" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="25563" flag="0" qtyDropped="1" qtyDestroyed="2" />
          <row typeID="23025" flag="5" qtyDropped="952" qtyDestroyed="0" />
          <row typeID="7367" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="26106" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2575" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="23025" flag="0" qtyDropped="25" qtyDestroyed="0" />
          <row typeID="2571" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="26108" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="29011" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3841" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="27441" flag="5" qtyDropped="0" qtyDestroyed="394" />
          <row typeID="1952" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2629" flag="5" qtyDropped="500" qtyDestroyed="0" />
          <row typeID="11578" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="1818" flag="5" qtyDropped="0" qtyDestroyed="500" />
        </rowset>
      </row>
      <row killID="6353141" solarSystemID="30003349" killTime="2009-03-30 20:22:00" moonID="0">
        <victim characterID="361823311" characterName="GRUCHOfromTRONDHEIM" corporationID="1541164645" corporationName="Hikage Corporation" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" damageTaken="8155" shipTypeID="11993" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="149816009" characterName="Jaedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-3.87968674437454" damageDone="1934" finalBlow="1" weaponTypeID="2817" shipTypeID="11365" />
          <row characterID="186363238" characterName="Salvo Brunel" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="1.5" damageDone="1808" finalBlow="0" weaponTypeID="2514" shipTypeID="11400" />
          <row characterID="233991150" characterName="Maelgar" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.7" damageDone="1368" finalBlow="0" weaponTypeID="12044" shipTypeID="12044" />
          <row characterID="634712898" characterName="Skeezor" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="-0.5" damageDone="1264" finalBlow="0" weaponTypeID="11393" shipTypeID="670" />
          <row characterID="702180569" characterName="BoomEZ" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="2.2" damageDone="637" finalBlow="0" weaponTypeID="3178" shipTypeID="11200" />
          <row characterID="1901781606" characterName="Surielle Zapata" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="0.9" damageDone="601" finalBlow="0" weaponTypeID="10680" shipTypeID="11200" />
          <row characterID="823357545" characterName="The0" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.6" damageDone="543" finalBlow="0" weaponTypeID="11198" shipTypeID="11198" />
          <row characterID="795531096" characterName="Kadashnikov" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="1.7" damageDone="0" finalBlow="0" weaponTypeID="2571" shipTypeID="11194" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="12625" flag="5" qtyDropped="0" qtyDestroyed="1184" />
          <row typeID="2281" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="27413" flag="0" qtyDropped="150" qtyDestroyed="37" />
          <row typeID="12076" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3244" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="25713" flag="0" qtyDropped="3" qtyDestroyed="2" />
          <row typeID="26088" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="5833" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2605" flag="5" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="1952" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="27413" flag="5" qtyDropped="1446" qtyDestroyed="0" />
          <row typeID="26076" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="22291" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="2889" flag="5" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="3841" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="1353" flag="0" qtyDropped="1" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6353136" solarSystemID="30003349" killTime="2009-03-30 20:22:00" moonID="0">
        <victim characterID="147790711" characterName="red smoking" corporationID="1541164645" corporationName="Hikage Corporation" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" damageTaken="666" shipTypeID="11190" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="761644878" characterName="Nkalv" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.25427825608947" damageDone="666" finalBlow="1" weaponTypeID="2881" shipTypeID="11400" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="448" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="5320" flag="0" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="29007" flag="0" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="29005" flag="5" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="1236" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="13003" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3001" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="2048" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="12565" flag="5" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="2488" flag="87" qtyDropped="2" qtyDestroyed="4" />
          <row typeID="12563" flag="0" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="440" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="2605" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="23711" flag="87" qtyDropped="1" qtyDestroyed="1" />
        </rowset>
      </row>
      <row killID="6353127" solarSystemID="30003349" killTime="2009-03-30 20:21:00" moonID="0">
        <victim characterID="502210831" characterName="ULISSE09" corporationID="1541164645" corporationName="Hikage Corporation" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" damageTaken="674" shipTypeID="11202" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1788740659" characterName="Qween Cleopatra" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.33478689522677" damageDone="592" finalBlow="1" weaponTypeID="3170" shipTypeID="11200" />
          <row characterID="246573211" characterName="Ydoc Llezsor" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0.5" damageDone="82" finalBlow="0" weaponTypeID="448" shipTypeID="11184" />
          <row characterID="713172734" characterName="Nicomedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="5" damageDone="0" finalBlow="0" weaponTypeID="2563" shipTypeID="11194" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="434" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="215" flag="5" qtyDropped="100" qtyDestroyed="0" />
          <row typeID="217" flag="5" qtyDropped="0" qtyDestroyed="158" />
          <row typeID="561" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="4029" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="523" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="221" flag="0" qtyDropped="198" qtyDestroyed="0" />
          <row typeID="25861" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="1244" flag="0" qtyDropped="1" qtyDestroyed="2" />
          <row typeID="3242" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="216" flag="0" qtyDropped="198" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6353010" solarSystemID="30003277" killTime="2009-03-30 20:16:00" moonID="0">
        <victim characterID="715132474" characterName="SilverHawk1" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="424" shipTypeID="583" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="128822322" characterName="Timmy Bettenson" corporationID="481995776" corporationName="Total Mayhem." allianceID="709664273" allianceName="Penumbra Alliance" factionID="0" factionName="" securityStatus="-3.03599140226365" damageDone="424" finalBlow="1" weaponTypeID="3138" shipTypeID="24700" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6352219" solarSystemID="30003321" killTime="2009-03-30 19:34:00" moonID="0">
        <victim characterID="1003719830" characterName="Rico Naginata" corporationID="1150111429" corporationName="DEATHFUNK" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" damageTaken="941" shipTypeID="587" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="296223009" characterName="BobTeh" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-2.00004511418916" damageDone="107" finalBlow="1" weaponTypeID="2905" shipTypeID="11198" />
          <row characterID="365949102" characterName="Fumb Duck" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-0.1" damageDone="834" finalBlow="0" weaponTypeID="2512" shipTypeID="11198" />
          <row characterID="246573211" characterName="Ydoc Llezsor" corporationID="1212227546" corporationName="Hydro Chronic" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0.5" damageDone="0" finalBlow="0" weaponTypeID="448" shipTypeID="11184" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="434" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="2046" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="185" flag="5" qtyDropped="420" qtyDestroyed="0" />
          <row typeID="486" flag="0" qtyDropped="2" qtyDestroyed="1" />
          <row typeID="2603" flag="0" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="185" flag="0" qtyDropped="46" qtyDestroyed="93" />
          <row typeID="526" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="447" flag="0" qtyDropped="1" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6350944" solarSystemID="30003320" killTime="2009-03-30 18:17:00" moonID="0">
        <victim characterID="1901781606" characterName="Surielle Zapata" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="1774" shipTypeID="11200" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="624488289" characterName="DemetRYS" corporationID="1225724619" corporationName="Steel Balls Brigade" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="3.07064412482232" damageDone="1774" finalBlow="1" weaponTypeID="2889" shipTypeID="11371" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="22961" flag="5" qtyDropped="0" qtyDestroyed="852" />
          <row typeID="29001" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="440" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="17765" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="1978" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="22961" flag="0" qtyDropped="130" qtyDestroyed="65" />
          <row typeID="1236" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="10190" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="10680" flag="0" qtyDropped="2" qtyDestroyed="1" />
          <row typeID="5439" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="5837" flag="0" qtyDropped="0" qtyDestroyed="1" />
        </rowset>
      </row>
      <row killID="6348466" solarSystemID="30003321" killTime="2009-03-30 14:34:00" moonID="0">
        <victim characterID="871788457" characterName="Danika Princip" corporationID="1888802408" corporationName="Caldari State Inc." allianceID="0" allianceName="" factionID="0" factionName="" damageTaken="99" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="365949102" characterName="Fumb Duck" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-0.0912547268323416" damageDone="99" finalBlow="1" weaponTypeID="2873" shipTypeID="11198" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6348450" solarSystemID="30003321" killTime="2009-03-30 14:32:00" moonID="0">
        <victim characterID="871788457" characterName="Danika Princip" corporationID="1888802408" corporationName="Caldari State Inc." allianceID="0" allianceName="" factionID="0" factionName="" damageTaken="1706" shipTypeID="587" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1788740659" characterName="Qween Cleopatra" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.32096463156358" damageDone="1176" finalBlow="1" weaponTypeID="3170" shipTypeID="12042" />
          <row characterID="365949102" characterName="Fumb Duck" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-0.1" damageDone="530" finalBlow="0" weaponTypeID="2512" shipTypeID="11198" />
          <row characterID="0" characterName="" corporationID="500021" corporationName="" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0" damageDone="0" finalBlow="0" weaponTypeID="0" shipTypeID="18114" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="178" flag="0" qtyDropped="184" qtyDestroyed="92" />
          <row typeID="210" flag="5" qtyDropped="100" qtyDestroyed="0" />
          <row typeID="213" flag="0" qtyDropped="0" qtyDestroyed="39" />
          <row typeID="27381" flag="5" qtyDropped="67" qtyDestroyed="403" />
          <row typeID="8817" flag="0" qtyDropped="1" qtyDestroyed="2" />
          <row typeID="523" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="8089" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="439" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="526" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="447" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="178" flag="5" qtyDropped="0" qtyDestroyed="657" />
          <row typeID="230" flag="5" qtyDropped="183" qtyDestroyed="182" />
          <row typeID="11345" flag="0" qtyDropped="0" qtyDestroyed="2" />
        </rowset>
      </row>
      <row killID="6346211" solarSystemID="30003320" killTime="2009-03-30 07:43:00" moonID="0">
        <victim characterID="1980242573" characterName="edsabi" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="431" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="825199715" characterName="Gunny1" corporationID="1483565871" corporationName="Arkons of Myth" allianceID="295773986" allianceName="Imperial Republic Of the North" factionID="0" factionName="" securityStatus="3.86067608552632" damageDone="431" finalBlow="1" weaponTypeID="3520" shipTypeID="24696" />
          <row characterID="2051819978" characterName="Avy Neruda" corporationID="1483565871" corporationName="Arkons of Myth" allianceID="295773986" allianceName="Imperial Republic Of the North" factionID="0" factionName="" securityStatus="4.7" damageDone="0" finalBlow="0" weaponTypeID="7997" shipTypeID="11993" />
          <row characterID="795528836" characterName="hom3gr0wn" corporationID="1483565871" corporationName="Arkons of Myth" allianceID="295773986" allianceName="Imperial Republic Of the North" factionID="0" factionName="" securityStatus="4" damageDone="0" finalBlow="0" weaponTypeID="2410" shipTypeID="11995" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6346203" solarSystemID="30003320" killTime="2009-03-30 07:42:00" moonID="0">
        <victim characterID="1980242573" characterName="edsabi" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="312" shipTypeID="607" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="795528836" characterName="hom3gr0wn" corporationID="1483565871" corporationName="Arkons of Myth" allianceID="295773986" allianceName="Imperial Republic Of the North" factionID="0" factionName="" securityStatus="4.01179996795076" damageDone="312" finalBlow="1" weaponTypeID="2629" shipTypeID="11995" />
          <row characterID="2051819978" characterName="Avy Neruda" corporationID="1483565871" corporationName="Arkons of Myth" allianceID="295773986" allianceName="Imperial Republic Of the North" factionID="0" factionName="" securityStatus="4.7" damageDone="0" finalBlow="0" weaponTypeID="7997" shipTypeID="11993" />
          <row characterID="683788884" characterName="Silmarillion X" corporationID="232862027" corporationName="E X O D U S" allianceID="295773986" allianceName="Imperial Republic Of the North" factionID="0" factionName="" securityStatus="0.9" damageDone="0" finalBlow="0" weaponTypeID="3520" shipTypeID="24696" />
          <row characterID="1812519662" characterName="Phantasms Shadow" corporationID="1483565871" corporationName="Arkons of Myth" allianceID="295773986" allianceName="Imperial Republic Of the North" factionID="0" factionName="" securityStatus="4.4" damageDone="0" finalBlow="0" weaponTypeID="7997" shipTypeID="24698" />
          <row characterID="825199715" characterName="Gunny1" corporationID="1483565871" corporationName="Arkons of Myth" allianceID="295773986" allianceName="Imperial Republic Of the North" factionID="0" factionName="" securityStatus="3.9" damageDone="0" finalBlow="0" weaponTypeID="3520" shipTypeID="24696" />
          <row characterID="748784062" characterName="MOJZESZ" corporationID="1794356538" corporationName="EXTERMINATUS." allianceID="295773986" allianceName="Imperial Republic Of the North" factionID="0" factionName="" securityStatus="5" damageDone="0" finalBlow="0" weaponTypeID="3082" shipTypeID="11957" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="434" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="18639" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="30013" flag="0" qtyDropped="0" qtyDestroyed="3" />
          <row typeID="30028" flag="5" qtyDropped="5" qtyDestroyed="7" />
          <row typeID="5401" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2488" flag="87" qtyDropped="1" qtyDestroyed="2" />
          <row typeID="6268" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="11370" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="30013" flag="5" qtyDropped="6" qtyDestroyed="2" />
          <row typeID="8749" flag="0" qtyDropped="0" qtyDestroyed="1" />
        </rowset>
      </row>
      <row killID="6346064" solarSystemID="30003321" killTime="2009-03-30 07:21:00" moonID="0">
        <victim characterID="683069625" characterName="Boozes" corporationID="1483565871" corporationName="Arkons of Myth" allianceID="295773986" allianceName="Imperial Republic Of the North" factionID="0" factionName="" damageTaken="892" shipTypeID="11176" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1788740659" characterName="Qween Cleopatra" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.32096463156358" damageDone="892" finalBlow="1" weaponTypeID="2466" shipTypeID="11200" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="16273" flag="5" qtyDropped="50" qtyDestroyed="0" />
          <row typeID="5973" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3244" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="26060" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="24495" flag="0" qtyDropped="27" qtyDestroyed="54" />
          <row typeID="1236" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="2032" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="24495" flag="5" qtyDropped="423" qtyDestroyed="0" />
          <row typeID="26070" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2605" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="2404" flag="0" qtyDropped="0" qtyDestroyed="3" />
        </rowset>
      </row>
      <row killID="6345169" solarSystemID="30004502" killTime="2009-03-30 05:20:00" moonID="0">
        <victim characterID="888777367" characterName="KellyMargret Ackerman" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="232" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1633925008" characterName="Tasmanian Devil" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="5.00322278334754" damageDone="214" finalBlow="1" weaponTypeID="3170" shipTypeID="11200" />
          <row characterID="697938605" characterName="Lord DeFault" corporationID="977777006" corporationName="FM Corp" allianceID="1345801112" allianceName="Dead Mans Hand" factionID="0" factionName="" securityStatus="0.1" damageDone="18" finalBlow="0" weaponTypeID="19739" shipTypeID="12038" />
          <row characterID="1979628731" characterName="Crazy Cowgirl" corporationID="145382885" corporationName="Solarflare Heavy Industries" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="-0.9" damageDone="0" finalBlow="0" weaponTypeID="3017" shipTypeID="11393" />
          <row characterID="2035736858" characterName="Tellasice Relkaw" corporationID="940434715" corporationName="Darkwave Technologies" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="5" damageDone="0" finalBlow="0" weaponTypeID="8089" shipTypeID="11198" />
          <row characterID="2035869922" characterName="ThatSmoker" corporationID="145382885" corporationName="Solarflare Heavy Industries" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="-0.6" damageDone="0" finalBlow="0" weaponTypeID="10680" shipTypeID="12042" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6345168" solarSystemID="30004502" killTime="2009-03-30 05:20:00" moonID="0">
        <victim characterID="149816009" characterName="Jaedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="382" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="158374943" characterName="Nastasia" corporationID="1907395390" corporationName="Baby Seal Clubbers" allianceID="173739862" allianceName="Veritas Immortalis" factionID="0" factionName="" securityStatus="1.05601869954875" damageDone="210" finalBlow="1" weaponTypeID="2897" shipTypeID="12013" />
          <row characterID="1979628731" characterName="Crazy Cowgirl" corporationID="145382885" corporationName="Solarflare Heavy Industries" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="-0.9" damageDone="84" finalBlow="0" weaponTypeID="11393" shipTypeID="11393" />
          <row characterID="2035869922" characterName="ThatSmoker" corporationID="145382885" corporationName="Solarflare Heavy Industries" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="-0.6" damageDone="77" finalBlow="0" weaponTypeID="2456" shipTypeID="12042" />
          <row characterID="697938605" characterName="Lord DeFault" corporationID="977777006" corporationName="FM Corp" allianceID="1345801112" allianceName="Dead Mans Hand" factionID="0" factionName="" securityStatus="0.1" damageDone="11" finalBlow="0" weaponTypeID="12038" shipTypeID="12038" />
          <row characterID="885212519" characterName="Iczer X01" corporationID="940434715" corporationName="Darkwave Technologies" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="2.2" damageDone="0" finalBlow="0" weaponTypeID="16471" shipTypeID="0" />
          <row characterID="387260615" characterName="Rigpa" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="0.3" damageDone="0" finalBlow="0" weaponTypeID="3244" shipTypeID="627" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6345167" solarSystemID="30004502" killTime="2009-03-30 05:20:00" moonID="0">
        <victim characterID="148511261" characterName="Teister" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="442" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="2035869922" characterName="ThatSmoker" corporationID="145382885" corporationName="Solarflare Heavy Industries" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="-0.647670930281236" damageDone="442" finalBlow="1" weaponTypeID="2456" shipTypeID="12042" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6345166" solarSystemID="30004502" killTime="2009-03-30 05:20:00" moonID="0">
        <victim characterID="878728887" characterName="Kal Shakai" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="339" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="158374943" characterName="Nastasia" corporationID="1907395390" corporationName="Baby Seal Clubbers" allianceID="173739862" allianceName="Veritas Immortalis" factionID="0" factionName="" securityStatus="1.05601869954875" damageDone="203" finalBlow="1" weaponTypeID="2897" shipTypeID="12013" />
          <row characterID="1979628731" characterName="Crazy Cowgirl" corporationID="145382885" corporationName="Solarflare Heavy Industries" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="-0.9" damageDone="136" finalBlow="0" weaponTypeID="11393" shipTypeID="11393" />
          <row characterID="1201859569" characterName="Ares GodOWar" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="1.9" damageDone="0" finalBlow="0" weaponTypeID="2410" shipTypeID="24698" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6345165" solarSystemID="30004502" killTime="2009-03-30 05:20:00" moonID="0">
        <victim characterID="1424923461" characterName="Brovic" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="315" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="158374943" characterName="Nastasia" corporationID="1907395390" corporationName="Baby Seal Clubbers" allianceID="173739862" allianceName="Veritas Immortalis" factionID="0" factionName="" securityStatus="1.05601869954875" damageDone="315" finalBlow="1" weaponTypeID="2897" shipTypeID="12013" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6345157" solarSystemID="30004502" killTime="2009-03-30 05:19:00" moonID="0">
        <victim characterID="888777367" characterName="KellyMargret Ackerman" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="11966" shipTypeID="16229" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="697938605" characterName="Lord DeFault" corporationID="977777006" corporationName="FM Corp" allianceID="1345801112" allianceName="Dead Mans Hand" factionID="0" factionName="" securityStatus="0.0790675227012339" damageDone="832" finalBlow="1" weaponTypeID="24535" shipTypeID="12038" />
          <row characterID="1473070250" characterName="Rhaheem" corporationID="1258269007" corporationName="Praetorian BlackGuard" allianceID="1345801112" allianceName="Dead Mans Hand" factionID="0" factionName="" securityStatus="2.6" damageDone="2297" finalBlow="0" weaponTypeID="209" shipTypeID="0" />
          <row characterID="1483002111" characterName="Mikaela" corporationID="1607489183" corporationName="Shadow Incursion" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" securityStatus="-1.5" damageDone="1588" finalBlow="0" weaponTypeID="27447" shipTypeID="11999" />
          <row characterID="1188254454" characterName="Thor Bajablast" corporationID="1313806157" corporationName="purple pot hogs" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="2.1" damageDone="1257" finalBlow="0" weaponTypeID="207" shipTypeID="0" />
          <row characterID="1201859569" characterName="Ares GodOWar" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="1.9" damageDone="1241" finalBlow="0" weaponTypeID="2456" shipTypeID="24698" />
          <row characterID="786779885" characterName="empiresteve" corporationID="977777006" corporationName="FM Corp" allianceID="1345801112" allianceName="Dead Mans Hand" factionID="0" factionName="" securityStatus="0.4" damageDone="1188" finalBlow="0" weaponTypeID="11999" shipTypeID="11999" />
          <row characterID="918538507" characterName="kr0NE11" corporationID="1637734758" corporationName="Templars of Burnination" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" securityStatus="5" damageDone="1021" finalBlow="0" weaponTypeID="2629" shipTypeID="24698" />
          <row characterID="851732403" characterName="DD1" corporationID="230423181" corporationName="Galactic Defence Syndicate" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" securityStatus="-5.9" damageDone="789" finalBlow="0" weaponTypeID="2629" shipTypeID="11993" />
          <row characterID="876199376" characterName="atlatntise" corporationID="927215459" corporationName="Aggressive Tendencies" allianceID="173739862" allianceName="Veritas Immortalis" factionID="0" factionName="" securityStatus="0.5" damageDone="687" finalBlow="0" weaponTypeID="27423" shipTypeID="11377" />
          <row characterID="1633925008" characterName="Tasmanian Devil" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="5" damageDone="510" finalBlow="0" weaponTypeID="11200" shipTypeID="11200" />
          <row characterID="1816580599" characterName="TruthState" corporationID="583616018" corporationName="Black Aces" allianceID="1345801112" allianceName="Dead Mans Hand" factionID="0" factionName="" securityStatus="4.5" damageDone="247" finalBlow="0" weaponTypeID="630" shipTypeID="630" />
          <row characterID="613588699" characterName="Dark Invoker" corporationID="145382885" corporationName="Solarflare Heavy Industries" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="-3.2" damageDone="184" finalBlow="0" weaponTypeID="11969" shipTypeID="11969" />
          <row characterID="2035869922" characterName="ThatSmoker" corporationID="145382885" corporationName="Solarflare Heavy Industries" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="-0.6" damageDone="125" finalBlow="0" weaponTypeID="12042" shipTypeID="12042" />
          <row characterID="387260615" characterName="Rigpa" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="0.3" damageDone="0" finalBlow="0" weaponTypeID="627" shipTypeID="627" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="2048" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3244" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="22979" flag="0" qtyDropped="118" qtyDestroyed="159" />
          <row typeID="527" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="2185" flag="87" qtyDropped="1" qtyDestroyed="4" />
          <row typeID="1355" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="22977" flag="5" qtyDropped="0" qtyDestroyed="500" />
          <row typeID="1952" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="5975" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="10190" flag="0" qtyDropped="2" qtyDestroyed="1" />
          <row typeID="29011" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3082" flag="0" qtyDropped="6" qtyDestroyed="1" />
          <row typeID="22979" flag="5" qtyDropped="560" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6345155" solarSystemID="30004502" killTime="2009-03-30 05:18:00" moonID="0">
        <victim characterID="149816009" characterName="Jaedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="2144" shipTypeID="11365" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="851732403" characterName="DD1" corporationID="230423181" corporationName="Galactic Defence Syndicate" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" securityStatus="-5.905614457293" damageDone="376" finalBlow="1" weaponTypeID="2629" shipTypeID="11993" />
          <row characterID="876199376" characterName="atlatntise" corporationID="927215459" corporationName="Aggressive Tendencies" allianceID="173739862" allianceName="Veritas Immortalis" factionID="0" factionName="" securityStatus="0.5" damageDone="959" finalBlow="0" weaponTypeID="13320" shipTypeID="11377" />
          <row characterID="1201859569" characterName="Ares GodOWar" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="1.9" damageDone="319" finalBlow="0" weaponTypeID="2629" shipTypeID="24698" />
          <row characterID="2035869922" characterName="ThatSmoker" corporationID="145382885" corporationName="Solarflare Heavy Industries" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="-0.5" damageDone="306" finalBlow="0" weaponTypeID="12042" shipTypeID="12042" />
          <row characterID="387260615" characterName="Rigpa" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="0.5" damageDone="76" finalBlow="0" weaponTypeID="2185" shipTypeID="627" />
          <row characterID="885212519" characterName="Iczer X01" corporationID="940434715" corporationName="Darkwave Technologies" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="2.2" damageDone="55" finalBlow="0" weaponTypeID="16511" shipTypeID="11965" />
          <row characterID="1633925008" characterName="Tasmanian Devil" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="5" damageDone="40" finalBlow="0" weaponTypeID="11200" shipTypeID="11200" />
          <row characterID="613588699" characterName="Dark Invoker" corporationID="145382885" corporationName="Solarflare Heavy Industries" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="-3.2" damageDone="10" finalBlow="0" weaponTypeID="11969" shipTypeID="11969" />
          <row characterID="786779885" characterName="empiresteve" corporationID="977777006" corporationName="FM Corp" allianceID="1345801112" allianceName="Dead Mans Hand" factionID="0" factionName="" securityStatus="0.4" damageDone="3" finalBlow="0" weaponTypeID="206" shipTypeID="11999" />
          <row characterID="958852486" characterName="mistiks" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="-0.8" damageDone="0" finalBlow="0" weaponTypeID="3244" shipTypeID="11371" />
          <row characterID="1816580599" characterName="TruthState" corporationID="583616018" corporationName="Black Aces" allianceID="1345801112" allianceName="Dead Mans Hand" factionID="0" factionName="" securityStatus="4.5" damageDone="0" finalBlow="0" weaponTypeID="630" shipTypeID="630" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="28668" flag="5" qtyDropped="0" qtyDestroyed="31" />
          <row typeID="24471" flag="5" qtyDropped="800" qtyDestroyed="0" />
          <row typeID="10631" flag="0" qtyDropped="1" qtyDestroyed="3" />
          <row typeID="3244" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="1306" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2817" flag="5" qtyDropped="802" qtyDestroyed="0" />
          <row typeID="4025" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2048" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="24475" flag="5" qtyDropped="0" qtyDestroyed="800" />
          <row typeID="24473" flag="5" qtyDropped="0" qtyDestroyed="728" />
          <row typeID="2817" flag="0" qtyDropped="33" qtyDestroyed="99" />
          <row typeID="440" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="1183" flag="0" qtyDropped="0" qtyDestroyed="2" />
        </rowset>
      </row>
      <row killID="6345152" solarSystemID="30004502" killTime="2009-03-30 05:18:00" moonID="0">
        <victim characterID="878728887" characterName="Kal Shakai" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="15358" shipTypeID="24702" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="786779885" characterName="empiresteve" corporationID="977777006" corporationName="FM Corp" allianceID="1345801112" allianceName="Dead Mans Hand" factionID="0" factionName="" securityStatus="0.3546665813619" damageDone="675" finalBlow="1" weaponTypeID="2897" shipTypeID="11999" />
          <row characterID="1483002111" characterName="Mikaela" corporationID="1607489183" corporationName="Shadow Incursion" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" securityStatus="-1.5" damageDone="9293" finalBlow="0" weaponTypeID="27447" shipTypeID="11999" />
          <row characterID="1201859569" characterName="Ares GodOWar" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="1.9" damageDone="4678" finalBlow="0" weaponTypeID="2629" shipTypeID="24698" />
          <row characterID="613588699" characterName="Dark Invoker" corporationID="145382885" corporationName="Solarflare Heavy Industries" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="-3.2" damageDone="202" finalBlow="0" weaponTypeID="11969" shipTypeID="11969" />
          <row characterID="158374943" characterName="Nastasia" corporationID="1907395390" corporationName="Baby Seal Clubbers" allianceID="173739862" allianceName="Veritas Immortalis" factionID="0" factionName="" securityStatus="1.1" damageDone="162" finalBlow="0" weaponTypeID="12013" shipTypeID="12013" />
          <row characterID="958852486" characterName="mistiks" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="-0.8" damageDone="156" finalBlow="0" weaponTypeID="11371" shipTypeID="11371" />
          <row characterID="1633925008" characterName="Tasmanian Devil" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="5" damageDone="123" finalBlow="0" weaponTypeID="3170" shipTypeID="11200" />
          <row characterID="1979628731" characterName="Crazy Cowgirl" corporationID="145382885" corporationName="Solarflare Heavy Industries" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="-0.9" damageDone="69" finalBlow="0" weaponTypeID="11393" shipTypeID="11393" />
          <row characterID="885212519" characterName="Iczer X01" corporationID="940434715" corporationName="Darkwave Technologies" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="2.2" damageDone="0" finalBlow="0" weaponTypeID="16511" shipTypeID="11965" />
          <row characterID="1816580599" characterName="TruthState" corporationID="583616018" corporationName="Black Aces" allianceID="1345801112" allianceName="Dead Mans Hand" factionID="0" factionName="" securityStatus="4.5" damageDone="0" finalBlow="0" weaponTypeID="5439" shipTypeID="630" />
          <row characterID="686200730" characterName="TUGGY" corporationID="1432894141" corporationName="Gods Killing Machines" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" securityStatus="5" damageDone="0" finalBlow="0" weaponTypeID="3244" shipTypeID="11176" />
          <row characterID="697938605" characterName="Lord DeFault" corporationID="977777006" corporationName="FM Corp" allianceID="1345801112" allianceName="Dead Mans Hand" factionID="0" factionName="" securityStatus="0.1" damageDone="0" finalBlow="0" weaponTypeID="5321" shipTypeID="12038" />
          <row characterID="918538507" characterName="kr0NE11" corporationID="1637734758" corporationName="Templars of Burnination" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" securityStatus="5" damageDone="0" finalBlow="0" weaponTypeID="2410" shipTypeID="24698" />
          <row characterID="387260615" characterName="Rigpa" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="0.5" damageDone="0" finalBlow="0" weaponTypeID="3244" shipTypeID="627" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="12265" flag="0" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="2048" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="519" flag="0" qtyDropped="0" qtyDestroyed="3" />
          <row typeID="12076" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="12771" flag="0" qtyDropped="28" qtyDestroyed="14" />
          <row typeID="1978" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3244" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="29001" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2969" flag="0" qtyDropped="3" qtyDestroyed="3" />
          <row typeID="1952" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="11269" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="29011" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="21896" flag="5" qtyDropped="684" qtyDestroyed="0" />
          <row typeID="12771" flag="5" qtyDropped="0" qtyDestroyed="186" />
        </rowset>
      </row>
      <row killID="6345151" solarSystemID="30004502" killTime="2009-03-30 05:18:00" moonID="0">
        <victim characterID="1424923461" characterName="Brovic" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="15081" shipTypeID="24696" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="918538507" characterName="kr0NE11" corporationID="1637734758" corporationName="Templars of Burnination" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" securityStatus="5.01088170437374" damageDone="3604" finalBlow="1" weaponTypeID="2629" shipTypeID="24698" />
          <row characterID="851732403" characterName="DD1" corporationID="230423181" corporationName="Galactic Defence Syndicate" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" securityStatus="-5.9" damageDone="3295" finalBlow="0" weaponTypeID="2629" shipTypeID="11993" />
          <row characterID="786779885" characterName="empiresteve" corporationID="977777006" corporationName="FM Corp" allianceID="1345801112" allianceName="Dead Mans Hand" factionID="0" factionName="" securityStatus="0.4" damageDone="1877" finalBlow="0" weaponTypeID="2897" shipTypeID="11999" />
          <row characterID="697938605" characterName="Lord DeFault" corporationID="977777006" corporationName="FM Corp" allianceID="1345801112" allianceName="Dead Mans Hand" factionID="0" factionName="" securityStatus="0.1" damageDone="1699" finalBlow="0" weaponTypeID="24535" shipTypeID="12038" />
          <row characterID="885212519" characterName="Iczer X01" corporationID="940434715" corporationName="Darkwave Technologies" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="2.2" damageDone="1133" finalBlow="0" weaponTypeID="21640" shipTypeID="11965" />
          <row characterID="1633925008" characterName="Tasmanian Devil" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="5" damageDone="660" finalBlow="0" weaponTypeID="11200" shipTypeID="11200" />
          <row characterID="2035869922" characterName="ThatSmoker" corporationID="145382885" corporationName="Solarflare Heavy Industries" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="-0.5" damageDone="609" finalBlow="0" weaponTypeID="2456" shipTypeID="12042" />
          <row characterID="958852486" characterName="mistiks" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="-0.8" damageDone="505" finalBlow="0" weaponTypeID="11371" shipTypeID="11371" />
          <row characterID="158374943" characterName="Nastasia" corporationID="1907395390" corporationName="Baby Seal Clubbers" allianceID="173739862" allianceName="Veritas Immortalis" factionID="0" factionName="" securityStatus="1.1" damageDone="376" finalBlow="0" weaponTypeID="12013" shipTypeID="12013" />
          <row characterID="387260615" characterName="Rigpa" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="0.5" damageDone="367" finalBlow="0" weaponTypeID="2185" shipTypeID="627" />
          <row characterID="1816580599" characterName="TruthState" corporationID="583616018" corporationName="Black Aces" allianceID="1345801112" allianceName="Dead Mans Hand" factionID="0" factionName="" securityStatus="4.5" damageDone="312" finalBlow="0" weaponTypeID="630" shipTypeID="630" />
          <row characterID="1979628731" characterName="Crazy Cowgirl" corporationID="145382885" corporationName="Solarflare Heavy Industries" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="-0.9" damageDone="308" finalBlow="0" weaponTypeID="11393" shipTypeID="11393" />
          <row characterID="686200730" characterName="TUGGY" corporationID="1432894141" corporationName="Gods Killing Machines" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" securityStatus="5" damageDone="203" finalBlow="0" weaponTypeID="27361" shipTypeID="11176" />
          <row characterID="1201859569" characterName="Ares GodOWar" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="1.9" damageDone="133" finalBlow="0" weaponTypeID="2456" shipTypeID="24698" />
          <row characterID="876199376" characterName="atlatntise" corporationID="927215459" corporationName="Aggressive Tendencies" allianceID="173739862" allianceName="Veritas Immortalis" factionID="0" factionName="" securityStatus="0.5" damageDone="0" finalBlow="0" weaponTypeID="13320" shipTypeID="11377" />
          <row characterID="123037519" characterName="Atropos Kahn" corporationID="145382885" corporationName="Solarflare Heavy Industries" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="1.2" damageDone="0" finalBlow="0" weaponTypeID="2571" shipTypeID="11194" />
          <row characterID="1483002111" characterName="Mikaela" corporationID="1607489183" corporationName="Shadow Incursion" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" securityStatus="-1.5" damageDone="0" finalBlow="0" weaponTypeID="2897" shipTypeID="11999" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="12818" flag="0" qtyDropped="5" qtyDestroyed="2" />
          <row typeID="1952" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2486" flag="87" qtyDropped="5" qtyDestroyed="0" />
          <row typeID="12814" flag="5" qtyDropped="7" qtyDestroyed="3" />
          <row typeID="3244" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="1306" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="12818" flag="5" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="12052" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="4025" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="2048" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3520" flag="0" qtyDropped="4" qtyDestroyed="3" />
          <row typeID="11269" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2364" flag="0" qtyDropped="0" qtyDestroyed="3" />
          <row typeID="29011" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="12257" flag="0" qtyDropped="0" qtyDestroyed="1" />
        </rowset>
      </row>
      <row killID="6345148" solarSystemID="30004502" killTime="2009-03-30 05:17:00" moonID="0">
        <victim characterID="148511261" characterName="Teister" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="12612" shipTypeID="24702" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1201859569" characterName="Ares GodOWar" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="1.90897268304593" damageDone="4833" finalBlow="1" weaponTypeID="2629" shipTypeID="24698" />
          <row characterID="697938605" characterName="Lord DeFault" corporationID="977777006" corporationName="FM Corp" allianceID="1345801112" allianceName="Dead Mans Hand" factionID="0" factionName="" securityStatus="0.1" damageDone="2725" finalBlow="0" weaponTypeID="24535" shipTypeID="12038" />
          <row characterID="786779885" characterName="empiresteve" corporationID="977777006" corporationName="FM Corp" allianceID="1345801112" allianceName="Dead Mans Hand" factionID="0" factionName="" securityStatus="0.4" damageDone="1815" finalBlow="0" weaponTypeID="11999" shipTypeID="11999" />
          <row characterID="851732403" characterName="DD1" corporationID="230423181" corporationName="Galactic Defence Syndicate" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" securityStatus="-5.9" damageDone="1318" finalBlow="0" weaponTypeID="2629" shipTypeID="11993" />
          <row characterID="2035869922" characterName="ThatSmoker" corporationID="145382885" corporationName="Solarflare Heavy Industries" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="-0.5" damageDone="483" finalBlow="0" weaponTypeID="2456" shipTypeID="12042" />
          <row characterID="387260615" characterName="Rigpa" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="0.5" damageDone="478" finalBlow="0" weaponTypeID="627" shipTypeID="627" />
          <row characterID="958852486" characterName="mistiks" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="-0.8" damageDone="466" finalBlow="0" weaponTypeID="11371" shipTypeID="11371" />
          <row characterID="1979628731" characterName="Crazy Cowgirl" corporationID="145382885" corporationName="Solarflare Heavy Industries" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="-0.9" damageDone="229" finalBlow="0" weaponTypeID="11393" shipTypeID="11393" />
          <row characterID="1816580599" characterName="TruthState" corporationID="583616018" corporationName="Black Aces" allianceID="1345801112" allianceName="Dead Mans Hand" factionID="0" factionName="" securityStatus="4.5" damageDone="166" finalBlow="0" weaponTypeID="630" shipTypeID="630" />
          <row characterID="1633925008" characterName="Tasmanian Devil" corporationID="591776049" corporationName="The Perfect Storm" allianceID="1472825340" allianceName="Controlled Chaos" factionID="0" factionName="" securityStatus="5" damageDone="56" finalBlow="0" weaponTypeID="11200" shipTypeID="11200" />
          <row characterID="2035736858" characterName="Tellasice Relkaw" corporationID="940434715" corporationName="Darkwave Technologies" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="5" damageDone="43" finalBlow="0" weaponTypeID="27361" shipTypeID="11198" />
          <row characterID="123037519" characterName="Atropos Kahn" corporationID="145382885" corporationName="Solarflare Heavy Industries" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="1.2" damageDone="0" finalBlow="0" weaponTypeID="19927" shipTypeID="11194" />
          <row characterID="885212519" characterName="Iczer X01" corporationID="940434715" corporationName="Darkwave Technologies" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" securityStatus="2.2" damageDone="0" finalBlow="0" weaponTypeID="21640" shipTypeID="11965" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="2048" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="519" flag="0" qtyDropped="2" qtyDestroyed="1" />
          <row typeID="2488" flag="87" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="12076" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="3244" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="5135" flag="0" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="4025" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="2969" flag="0" qtyDropped="2" qtyDestroyed="4" />
          <row typeID="1952" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="11269" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="29011" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="21896" flag="0" qtyDropped="12" qtyDestroyed="12" />
          <row typeID="21896" flag="5" qtyDropped="852" qtyDestroyed="0" />
          <row typeID="28326" flag="5" qtyDropped="200" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6345142" solarSystemID="30004502" killTime="2009-03-30 05:17:00" moonID="0">
        <victim characterID="1473070250" characterName="Rhaheem" corporationID="1258269007" corporationName="Praetorian BlackGuard" allianceID="1345801112" allianceName="Dead Mans Hand" factionID="0" factionName="" damageTaken="4672" shipTypeID="11993" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1424923461" characterName="Brovic" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-0.798944928325898" damageDone="1865" finalBlow="1" weaponTypeID="3520" shipTypeID="24696" />
          <row characterID="148511261" characterName="Teister" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="1.4" damageDone="1925" finalBlow="0" weaponTypeID="24702" shipTypeID="24702" />
          <row characterID="888777367" characterName="KellyMargret Ackerman" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="5" damageDone="378" finalBlow="0" weaponTypeID="16229" shipTypeID="16229" />
          <row characterID="878728887" characterName="Kal Shakai" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-4.5" damageDone="283" finalBlow="0" weaponTypeID="24702" shipTypeID="24702" />
          <row characterID="1868072702" characterName="Rockstara" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.2" damageDone="221" finalBlow="0" weaponTypeID="2488" shipTypeID="11200" />
          <row characterID="149816009" characterName="Jaedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-3.9" damageDone="0" finalBlow="0" weaponTypeID="3244" shipTypeID="11365" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="209" flag="5" qtyDropped="8140" qtyDestroyed="0" />
          <row typeID="8103" flag="0" qtyDropped="1" qtyDestroyed="4" />
          <row typeID="209" flag="0" qtyDropped="28" qtyDestroyed="112" />
          <row typeID="22291" flag="0" qtyDropped="2" qtyDestroyed="2" />
          <row typeID="394" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="3841" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="12056" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="26084" flag="0" qtyDropped="0" qtyDestroyed="2" />
        </rowset>
      </row>
      <row killID="6345139" solarSystemID="30004502" killTime="2009-03-30 05:16:00" moonID="0">
        <victim characterID="1188254454" characterName="Thor Bajablast" corporationID="1313806157" corporationName="purple pot hogs" allianceID="1082705819" allianceName="Doctrine." factionID="0" factionName="" damageTaken="3562" shipTypeID="621" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1424923461" characterName="Brovic" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-0.798944928325898" damageDone="2656" finalBlow="1" weaponTypeID="3520" shipTypeID="24696" />
          <row characterID="148511261" characterName="Teister" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="1.4" damageDone="333" finalBlow="0" weaponTypeID="2969" shipTypeID="24702" />
          <row characterID="149816009" characterName="Jaedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-3.9" damageDone="324" finalBlow="0" weaponTypeID="4025" shipTypeID="11365" />
          <row characterID="722088228" characterName="JackCo" corporationID="1588486523" corporationName="Yakuza Corp" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="4.1" damageDone="181" finalBlow="0" weaponTypeID="527" shipTypeID="11963" />
          <row characterID="888777367" characterName="KellyMargret Ackerman" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="5" damageDone="68" finalBlow="0" weaponTypeID="3082" shipTypeID="16229" />
          <row characterID="878728887" characterName="Kal Shakai" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-4.5" damageDone="0" finalBlow="0" weaponTypeID="3244" shipTypeID="24702" />
          <row characterID="1868072702" characterName="Rockstara" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.2" damageDone="0" finalBlow="0" weaponTypeID="527" shipTypeID="11200" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="12274" flag="0" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="393" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2454" flag="87" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="501" flag="0" qtyDropped="4" qtyDestroyed="1" />
          <row typeID="6005" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="209" flag="5" qtyDropped="0" qtyDestroyed="500" />
          <row typeID="209" flag="0" qtyDropped="0" qtyDestroyed="27" />
          <row typeID="207" flag="0" qtyDropped="52" qtyDestroyed="0" />
          <row typeID="578" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="208" flag="0" qtyDropped="26" qtyDestroyed="0" />
          <row typeID="206" flag="0" qtyDropped="27" qtyDestroyed="0" />
          <row typeID="208" flag="5" qtyDropped="500" qtyDestroyed="0" />
          <row typeID="207" flag="5" qtyDropped="0" qtyDestroyed="1000" />
          <row typeID="206" flag="5" qtyDropped="500" qtyDestroyed="0" />
          <row typeID="3829" flag="0" qtyDropped="2" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6342927" solarSystemID="30003321" killTime="2009-03-30 01:46:00" moonID="0">
        <victim characterID="681358337" characterName="KimMong Aykuk" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="1039" shipTypeID="607" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1023846807" characterName="swordslasher" corporationID="197015817" corporationName="ADVANCED Combat and Engineering" allianceID="812396591" allianceName="Axiom Empire" factionID="0" factionName="" securityStatus="-0.0688971629936064" damageDone="1039" finalBlow="1" weaponTypeID="27361" shipTypeID="11176" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="21096" flag="0" qtyDropped="0" qtyDestroyed="1" />
        </rowset>
      </row>
      <row killID="6342121" solarSystemID="30003321" killTime="2009-03-30 00:28:00" moonID="0">
        <victim characterID="355274556" characterName="TheUnknown" corporationID="1052673484" corporationName="Advocates of Sin" allianceID="0" allianceName="" factionID="0" factionName="" damageTaken="349" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="826540579" characterName="The Aegis" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="1.66432693984784" damageDone="349" finalBlow="1" weaponTypeID="3170" shipTypeID="11200" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6342053" solarSystemID="30003288" killTime="2009-03-30 00:23:00" moonID="0">
        <victim characterID="318582956" characterName="Vibenation 2" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="315" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="204332457" characterName="Blue Rider" corporationID="921854522" corporationName="Thanos and Killjoy Productions" allianceID="1041482450" allianceName="HUZZAH FEDERATION" factionID="0" factionName="" securityStatus="3.38132126025809" damageDone="315" finalBlow="1" weaponTypeID="3170" shipTypeID="11200" />
          <row characterID="297253361" characterName="DJJEFLYNN" corporationID="651624803" corporationName="Blind Violence" allianceID="1041482450" allianceName="HUZZAH FEDERATION" factionID="0" factionName="" securityStatus="1.2" damageDone="0" finalBlow="0" weaponTypeID="8789" shipTypeID="587" />
          <row characterID="239386620" characterName="Kerc Kasha" corporationID="1632671205" corporationName="Valiant Research Associates" allianceID="1041482450" allianceName="HUZZAH FEDERATION" factionID="0" factionName="" securityStatus="1" damageDone="0" finalBlow="0" weaponTypeID="3244" shipTypeID="12019" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6342034" solarSystemID="30003288" killTime="2009-03-30 00:21:00" moonID="0">
        <victim characterID="318582956" characterName="Vibenation 2" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="295" shipTypeID="11198" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="239386620" characterName="Kerc Kasha" corporationID="1632671205" corporationName="Valiant Research Associates" allianceID="1041482450" allianceName="HUZZAH FEDERATION" factionID="0" factionName="" securityStatus="0.959911103623379" damageDone="295" finalBlow="1" weaponTypeID="20306" shipTypeID="12019" />
          <row characterID="885892179" characterName="Nakimoto" corporationID="1202099160" corporationName="Unnatural Growth" allianceID="1041482450" allianceName="HUZZAH FEDERATION" factionID="0" factionName="" securityStatus="1" damageDone="0" finalBlow="0" weaponTypeID="2410" shipTypeID="11995" />
          <row characterID="297253361" characterName="DJJEFLYNN" corporationID="651624803" corporationName="Blind Violence" allianceID="1041482450" allianceName="HUZZAH FEDERATION" factionID="0" factionName="" securityStatus="1.2" damageDone="0" finalBlow="0" weaponTypeID="8789" shipTypeID="587" />
          <row characterID="906243146" characterName="Zebeyo" corporationID="1632671205" corporationName="Valiant Research Associates" allianceID="1041482450" allianceName="HUZZAH FEDERATION" factionID="0" factionName="" securityStatus="-1.5" damageDone="0" finalBlow="0" weaponTypeID="456" shipTypeID="2006" />
          <row characterID="938141391" characterName="Pboyt" corporationID="1632671205" corporationName="Valiant Research Associates" allianceID="1041482450" allianceName="HUZZAH FEDERATION" factionID="0" factionName="" securityStatus="-2.3" damageDone="0" finalBlow="0" weaponTypeID="2913" shipTypeID="22444" />
          <row characterID="894355258" characterName="Sikmaa" corporationID="1806492808" corporationName="Galactic Shipyards Inc" allianceID="1041482450" allianceName="HUZZAH FEDERATION" factionID="0" factionName="" securityStatus="-1" damageDone="0" finalBlow="0" weaponTypeID="2410" shipTypeID="11963" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="28668" flag="5" qtyDropped="0" qtyDestroyed="75" />
          <row typeID="3244" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="28328" flag="0" qtyDropped="25" qtyDestroyed="25" />
          <row typeID="527" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="1236" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="2905" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="2032" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="25861" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="440" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="28328" flag="5" qtyDropped="0" qtyDestroyed="646" />
          <row typeID="2605" flag="0" qtyDropped="1" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6341932" solarSystemID="30003278" killTime="2009-03-30 00:13:00" moonID="0">
        <victim characterID="747677046" characterName="Ciryon Atani" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="1185" shipTypeID="11176" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1459499801" characterName="Siphaanu" corporationID="763255741" corporationName="SkillzKillz" allianceID="1484395853" allianceName="United For 0rder" factionID="0" factionName="" securityStatus="3.80603200079983" damageDone="433" finalBlow="1" weaponTypeID="3001" shipTypeID="11393" />
          <row characterID="1878135903" characterName="Razor Z" corporationID="763255741" corporationName="SkillzKillz" allianceID="1484395853" allianceName="United For 0rder" factionID="0" factionName="" securityStatus="-0.9" damageDone="752" finalBlow="0" weaponTypeID="21867" shipTypeID="11971" />
          <row characterID="1291054333" characterName="D Bogart" corporationID="763255741" corporationName="SkillzKillz" allianceID="1484395853" allianceName="United For 0rder" factionID="0" factionName="" securityStatus="3.9" damageDone="0" finalBlow="0" weaponTypeID="2571" shipTypeID="11957" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="3244" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="527" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="1236" flag="0" qtyDropped="3" qtyDestroyed="0" />
          <row typeID="27361" flag="5" qtyDropped="428" qtyDestroyed="0" />
          <row typeID="27361" flag="0" qtyDropped="114" qtyDestroyed="0" />
          <row typeID="440" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="26070" flag="0" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="2404" flag="0" qtyDropped="1" qtyDestroyed="2" />
        </rowset>
      </row>
      <row killID="6341480" solarSystemID="30003286" killTime="2009-03-29 23:39:00" moonID="0">
        <victim characterID="940627143" characterName="Excaliblur" corporationID="651624803" corporationName="Blind Violence" allianceID="1041482450" allianceName="HUZZAH FEDERATION" factionID="0" factionName="" damageTaken="382" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="148511261" characterName="Teister" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="1.41333117524803" damageDone="382" finalBlow="1" weaponTypeID="2977" shipTypeID="11371" />
          <row characterID="365949102" characterName="Fumb Duck" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-0.1" damageDone="0" finalBlow="0" weaponTypeID="448" shipTypeID="11198" />
          <row characterID="747677046" characterName="Ciryon Atani" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.6" damageDone="0" finalBlow="0" weaponTypeID="2404" shipTypeID="11176" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6341463" solarSystemID="30003286" killTime="2009-03-29 23:38:00" moonID="0">
        <victim characterID="940627143" characterName="Excaliblur" corporationID="651624803" corporationName="Blind Violence" allianceID="1041482450" allianceName="HUZZAH FEDERATION" factionID="0" factionName="" damageTaken="15404" shipTypeID="645" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="724093268" characterName="Zentan" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.7706691035497" damageDone="606" finalBlow="1" weaponTypeID="2881" shipTypeID="11371" />
          <row characterID="148511261" characterName="Teister" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="1.4" damageDone="4768" finalBlow="0" weaponTypeID="11371" shipTypeID="11371" />
          <row characterID="149816009" characterName="Jaedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-3.8" damageDone="2160" finalBlow="0" weaponTypeID="2817" shipTypeID="11365" />
          <row characterID="878728887" characterName="Kal Shakai" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-4.5" damageDone="1343" finalBlow="0" weaponTypeID="27315" shipTypeID="11400" />
          <row characterID="747677046" characterName="Ciryon Atani" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.6" damageDone="1332" finalBlow="0" weaponTypeID="27361" shipTypeID="11176" />
          <row characterID="636046666" characterName="Mr Inevitability" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="5" damageDone="1201" finalBlow="0" weaponTypeID="27361" shipTypeID="11176" />
          <row characterID="365949102" characterName="Fumb Duck" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-0.1" damageDone="1041" finalBlow="0" weaponTypeID="2512" shipTypeID="11198" />
          <row characterID="376147608" characterName="Dreamchasr" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="5" damageDone="920" finalBlow="0" weaponTypeID="27361" shipTypeID="11176" />
          <row characterID="1868072702" characterName="Rockstara" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.2" damageDone="858" finalBlow="0" weaponTypeID="11200" shipTypeID="11200" />
          <row characterID="1409795219" characterName="skyterd2008" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.4" damageDone="685" finalBlow="0" weaponTypeID="4025" shipTypeID="22464" />
          <row characterID="823357545" characterName="The0" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.6" damageDone="303" finalBlow="0" weaponTypeID="11198" shipTypeID="11198" />
          <row characterID="318582956" characterName="Vibenation 2" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3" damageDone="187" finalBlow="0" weaponTypeID="11198" shipTypeID="11198" />
          <row characterID="713172734" characterName="Nicomedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="5" damageDone="0" finalBlow="0" weaponTypeID="2559" shipTypeID="11194" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="16379" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="22993" flag="5" qtyDropped="0" qtyDestroyed="1408" />
          <row typeID="1952" flag="0" qtyDropped="0" qtyDestroyed="3" />
          <row typeID="530" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="29009" flag="0" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="14280" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="2185" flag="87" qtyDropped="0" qtyDestroyed="5" />
          <row typeID="231" flag="5" qtyDropped="0" qtyDestroyed="5103" />
          <row typeID="2032" flag="0" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="11255" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="10190" flag="0" qtyDropped="2" qtyDestroyed="1" />
          <row typeID="14282" flag="0" qtyDropped="0" qtyDestroyed="3" />
          <row typeID="3540" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="22993" flag="0" qtyDropped="74" qtyDestroyed="114" />
          <row typeID="11277" flag="0" qtyDropped="1" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6341443" solarSystemID="30003286" killTime="2009-03-29 23:37:00" moonID="0">
        <victim characterID="825677979" characterName="ifeelit2" corporationID="755521704" corporationName="JUDGE DREAD Inc." allianceID="1041482450" allianceName="HUZZAH FEDERATION" factionID="0" factionName="" damageTaken="391" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="724093268" characterName="Zentan" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.7706691035497" damageDone="391" finalBlow="1" weaponTypeID="2881" shipTypeID="11371" />
          <row characterID="1409795219" characterName="skyterd2008" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.4" damageDone="0" finalBlow="0" weaponTypeID="8089" shipTypeID="22464" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6340792" solarSystemID="30003278" killTime="2009-03-29 22:56:00" moonID="0">
        <victim characterID="113815634" characterName="Romay" corporationID="1429008930" corporationName="GeoTech" allianceID="0" allianceName="" factionID="0" factionName="" damageTaken="162" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="724093268" characterName="Zentan" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.7706691035497" damageDone="162" finalBlow="1" weaponTypeID="2881" shipTypeID="11371" />
          <row characterID="823357545" characterName="The0" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.6" damageDone="0" finalBlow="0" weaponTypeID="3244" shipTypeID="11198" />
          <row characterID="365949102" characterName="Fumb Duck" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-0.1" damageDone="0" finalBlow="0" weaponTypeID="16523" shipTypeID="11198" />
          <row characterID="1788740659" characterName="Qween Cleopatra" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.3" damageDone="0" finalBlow="0" weaponTypeID="3170" shipTypeID="11200" />
          <row characterID="747677046" characterName="Ciryon Atani" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.6" damageDone="0" finalBlow="0" weaponTypeID="2404" shipTypeID="11176" />
          <row characterID="1868072702" characterName="Rockstara" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.2" damageDone="0" finalBlow="0" weaponTypeID="448" shipTypeID="11200" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6340774" solarSystemID="30003278" killTime="2009-03-29 22:55:00" moonID="0">
        <victim characterID="113815634" characterName="Romay" corporationID="1429008930" corporationName="GeoTech" allianceID="0" allianceName="" factionID="0" factionName="" damageTaken="28928" shipTypeID="24698" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="724093268" characterName="Zentan" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.7706691035497" damageDone="7097" finalBlow="1" weaponTypeID="2881" shipTypeID="11371" />
          <row characterID="1868072702" characterName="Rockstara" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.2" damageDone="3828" finalBlow="0" weaponTypeID="2488" shipTypeID="11200" />
          <row characterID="636046666" characterName="Mr Inevitability" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="5" damageDone="3057" finalBlow="0" weaponTypeID="27361" shipTypeID="11176" />
          <row characterID="148511261" characterName="Teister" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="1.4" damageDone="3040" finalBlow="0" weaponTypeID="11371" shipTypeID="11371" />
          <row characterID="1788740659" characterName="Qween Cleopatra" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.3" damageDone="2166" finalBlow="0" weaponTypeID="2466" shipTypeID="11200" />
          <row characterID="878728887" characterName="Kal Shakai" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-4.5" damageDone="2126" finalBlow="0" weaponTypeID="27315" shipTypeID="11400" />
          <row characterID="747677046" characterName="Ciryon Atani" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.6" damageDone="1810" finalBlow="0" weaponTypeID="3244" shipTypeID="11176" />
          <row characterID="365949102" characterName="Fumb Duck" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-0.1" damageDone="1542" finalBlow="0" weaponTypeID="2512" shipTypeID="11198" />
          <row characterID="823357545" characterName="The0" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.6" damageDone="1350" finalBlow="0" weaponTypeID="11198" shipTypeID="11198" />
          <row characterID="1409795219" characterName="skyterd2008" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.4" damageDone="795" finalBlow="0" weaponTypeID="27361" shipTypeID="22464" />
          <row characterID="318582956" characterName="Vibenation 2" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3" damageDone="758" finalBlow="0" weaponTypeID="11198" shipTypeID="11198" />
          <row characterID="149816009" characterName="Jaedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-3.8" damageDone="591" finalBlow="0" weaponTypeID="24473" shipTypeID="11365" />
          <row characterID="376147608" characterName="Dreamchasr" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="5" damageDone="445" finalBlow="0" weaponTypeID="527" shipTypeID="11176" />
          <row characterID="713172734" characterName="Nicomedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="5" damageDone="323" finalBlow="0" weaponTypeID="2512" shipTypeID="11194" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="23164" flag="5" qtyDropped="0" qtyDestroyed="30" />
          <row typeID="17938" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="2281" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="23707" flag="87" qtyDropped="0" qtyDestroyed="5" />
          <row typeID="30745" flag="5" qtyDropped="66" qtyDestroyed="0" />
          <row typeID="27441" flag="0" qtyDropped="144" qtyDestroyed="108" />
          <row typeID="30259" flag="5" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="25936" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="1422" flag="0" qtyDropped="1" qtyDestroyed="3" />
          <row typeID="23163" flag="5" qtyDropped="0" qtyDestroyed="20" />
          <row typeID="2410" flag="0" qtyDropped="5" qtyDestroyed="2" />
          <row typeID="23183" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="2303" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="30018" flag="5" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="20419" flag="5" qtyDropped="15" qtyDestroyed="0" />
          <row typeID="30488" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="25861" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="23186" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="22175" flag="5" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="30744" flag="5" qtyDropped="0" qtyDestroyed="42" />
          <row typeID="5053" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="30248" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="16375" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="30254" flag="5" qtyDropped="0" qtyDestroyed="10" />
          <row typeID="30488" flag="5" qtyDropped="1" qtyDestroyed="2" />
          <row typeID="22177" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3841" flag="0" qtyDropped="2" qtyDestroyed="1" />
          <row typeID="18639" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="20424" flag="5" qtyDropped="6" qtyDestroyed="0" />
          <row typeID="27441" flag="5" qtyDropped="0" qtyDestroyed="2762" />
          <row typeID="30021" flag="5" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="2301" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="22291" flag="5" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="23121" flag="5" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="30746" flag="5" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="26084" flag="0" qtyDropped="0" qtyDestroyed="2" />
        </rowset>
      </row>
      <row killID="6340622" solarSystemID="30003320" killTime="2009-03-29 22:47:00" moonID="0">
        <victim characterID="529188379" characterName="Odhinn Vinlandii" corporationID="1913842861" corporationName="The Colour Out of Space" allianceID="333627093" allianceName="Un-Natural Selection" factionID="0" factionName="" damageTaken="981" shipTypeID="11963" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="148511261" characterName="Teister" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="1.41333117524803" damageDone="520" finalBlow="1" weaponTypeID="2977" shipTypeID="11371" />
          <row characterID="724093268" characterName="Zentan" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.8" damageDone="326" finalBlow="0" weaponTypeID="11371" shipTypeID="11371" />
          <row characterID="365949102" characterName="Fumb Duck" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-0.1" damageDone="135" finalBlow="0" weaponTypeID="2512" shipTypeID="11198" />
          <row characterID="878728887" characterName="Kal Shakai" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-4.5" damageDone="0" finalBlow="0" weaponTypeID="2873" shipTypeID="11400" />
          <row characterID="376147608" characterName="Dreamchasr" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="5" damageDone="0" finalBlow="0" weaponTypeID="527" shipTypeID="11176" />
          <row characterID="149816009" characterName="Jaedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-3.8" damageDone="0" finalBlow="0" weaponTypeID="4025" shipTypeID="11365" />
          <row characterID="713172734" characterName="Nicomedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="5" damageDone="0" finalBlow="0" weaponTypeID="16525" shipTypeID="11194" />
          <row characterID="1788740659" characterName="Qween Cleopatra" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.3" damageDone="0" finalBlow="0" weaponTypeID="3170" shipTypeID="11200" />
          <row characterID="1409795219" characterName="skyterd2008" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.4" damageDone="0" finalBlow="0" weaponTypeID="8089" shipTypeID="22464" />
          <row characterID="1103002374" characterName="BlackRain McMillan" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.8" damageDone="0" finalBlow="0" weaponTypeID="2488" shipTypeID="12042" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="4027" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="16273" flag="5" qtyDropped="0" qtyDestroyed="160" />
          <row typeID="5975" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="1952" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="519" flag="0" qtyDropped="1" qtyDestroyed="2" />
          <row typeID="26060" flag="0" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="21096" flag="5" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="1969" flag="0" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="3244" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="9451" flag="0" qtyDropped="1" qtyDestroyed="2" />
          <row typeID="2048" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="29015" flag="0" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="21904" flag="0" qtyDropped="0" qtyDestroyed="39" />
          <row typeID="11578" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="29011" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="21904" flag="5" qtyDropped="2461" qtyDestroyed="0" />
          <row typeID="21896" flag="5" qtyDropped="0" qtyDestroyed="3500" />
          <row typeID="23705" flag="87" qtyDropped="1" qtyDestroyed="3" />
        </rowset>
      </row>
      <row killID="6340350" solarSystemID="30003350" killTime="2009-03-29 22:29:00" moonID="0">
        <victim characterID="1480209681" characterName="Celine Lyrus" corporationID="1607543602" corporationName="Morbid Obssesion" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" damageTaken="24608" shipTypeID="24698" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="724093268" characterName="Zentan" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.7706691035497" damageDone="4165" finalBlow="1" weaponTypeID="2881" shipTypeID="11371" />
          <row characterID="1103002374" characterName="BlackRain McMillan" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.8" damageDone="2747" finalBlow="0" weaponTypeID="2488" shipTypeID="12042" />
          <row characterID="1788740659" characterName="Qween Cleopatra" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.3" damageDone="2705" finalBlow="0" weaponTypeID="2466" shipTypeID="11200" />
          <row characterID="148511261" characterName="Teister" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="1.4" damageDone="2492" finalBlow="0" weaponTypeID="11371" shipTypeID="11371" />
          <row characterID="1672429356" characterName="Jel Malar" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.7" damageDone="2358" finalBlow="0" weaponTypeID="11371" shipTypeID="670" />
          <row characterID="1868072702" characterName="Rockstara" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.2" damageDone="1987" finalBlow="0" weaponTypeID="11200" shipTypeID="11200" />
          <row characterID="149816009" characterName="Jaedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-3.8" damageDone="1937" finalBlow="0" weaponTypeID="2817" shipTypeID="11365" />
          <row characterID="878728887" characterName="Kal Shakai" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-4.5" damageDone="1794" finalBlow="0" weaponTypeID="27315" shipTypeID="11400" />
          <row characterID="636046666" characterName="Mr Inevitability" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="5" damageDone="1320" finalBlow="0" weaponTypeID="27361" shipTypeID="11176" />
          <row characterID="376147608" characterName="Dreamchasr" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="5" damageDone="899" finalBlow="0" weaponTypeID="27361" shipTypeID="11176" />
          <row characterID="823357545" characterName="The0" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.6" damageDone="837" finalBlow="0" weaponTypeID="11198" shipTypeID="11198" />
          <row characterID="365949102" characterName="Fumb Duck" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-0.1" damageDone="824" finalBlow="0" weaponTypeID="2516" shipTypeID="11198" />
          <row characterID="1409795219" characterName="skyterd2008" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.4" damageDone="543" finalBlow="0" weaponTypeID="27361" shipTypeID="22464" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="2679" flag="5" qtyDropped="1714" qtyDestroyed="0" />
          <row typeID="2048" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="24490" flag="5" qtyDropped="1559" qtyDestroyed="0" />
          <row typeID="6005" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="26088" flag="0" qtyDropped="0" qtyDestroyed="3" />
          <row typeID="2281" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="20307" flag="5" qtyDropped="0" qtyDestroyed="3170" />
          <row typeID="24492" flag="5" qtyDropped="1265" qtyDestroyed="0" />
          <row typeID="22291" flag="0" qtyDropped="1" qtyDestroyed="2" />
          <row typeID="4025" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="448" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="25715" flag="0" qtyDropped="6" qtyDestroyed="1" />
          <row typeID="3841" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="20307" flag="0" qtyDropped="159" qtyDestroyed="212" />
        </rowset>
      </row>
      <row killID="6340343" solarSystemID="30003350" killTime="2009-03-29 22:29:00" moonID="0">
        <victim characterID="1672429356" characterName="Jel Malar" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" damageTaken="1782" shipTypeID="11371" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1480209681" characterName="Celine Lyrus" corporationID="1607543602" corporationName="Morbid Obssesion" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" securityStatus="-3.09907093602279" damageDone="1782" finalBlow="1" weaponTypeID="20307" shipTypeID="24698" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="21898" flag="5" qtyDropped="125" qtyDestroyed="3" />
          <row typeID="1952" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="519" flag="0" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="11563" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3888" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="21898" flag="0" qtyDropped="2" qtyDestroyed="6" />
          <row typeID="2977" flag="0" qtyDropped="3" qtyDestroyed="1" />
          <row typeID="440" flag="0" qtyDropped="1" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6339801" solarSystemID="30003347" killTime="2009-03-29 21:59:00" moonID="0">
        <victim characterID="1237513540" characterName="Infernal Saw" corporationID="985022514" corporationName="ANCIENT SYNDICATE" allianceID="0" allianceName="" factionID="0" factionName="" damageTaken="74" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="724093268" characterName="Zentan" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.7706691035497" damageDone="74" finalBlow="1" weaponTypeID="2881" shipTypeID="11371" />
          <row characterID="823357545" characterName="The0" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.6" damageDone="0" finalBlow="0" weaponTypeID="3244" shipTypeID="11198" />
          <row characterID="365949102" characterName="Fumb Duck" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-0.1" damageDone="0" finalBlow="0" weaponTypeID="3244" shipTypeID="11198" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6339779" solarSystemID="30003347" killTime="2009-03-29 21:58:00" moonID="0">
        <victim characterID="1237513540" characterName="Infernal Saw" corporationID="985022514" corporationName="ANCIENT SYNDICATE" allianceID="0" allianceName="" factionID="0" factionName="" damageTaken="428425" shipTypeID="638" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="823357545" characterName="The0" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.61201627837133" damageDone="441" finalBlow="1" weaponTypeID="2889" shipTypeID="11198" />
          <row characterID="0" characterName="" corporationID="1000135" corporationName="Serpentis Corporation" allianceID="0" allianceName="" factionID="0" factionName="" securityStatus="0" damageDone="402393" finalBlow="0" weaponTypeID="0" shipTypeID="10286" />
          <row characterID="148511261" characterName="Teister" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="1.4" damageDone="3569" finalBlow="0" weaponTypeID="11371" shipTypeID="11371" />
          <row characterID="724093268" characterName="Zentan" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.8" damageDone="3469" finalBlow="0" weaponTypeID="11371" shipTypeID="11371" />
          <row characterID="149816009" characterName="Jaedes" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-3.8" damageDone="3386" finalBlow="0" weaponTypeID="2817" shipTypeID="11365" />
          <row characterID="1672429356" characterName="Jel Malar" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.7" damageDone="2822" finalBlow="0" weaponTypeID="11371" shipTypeID="11371" />
          <row characterID="1868072702" characterName="Rockstara" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.2" damageDone="2662" finalBlow="0" weaponTypeID="11200" shipTypeID="11200" />
          <row characterID="502417576" characterName="AyuTokin Tumi" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.3" damageDone="2628" finalBlow="0" weaponTypeID="2488" shipTypeID="11200" />
          <row characterID="1788740659" characterName="Qween Cleopatra" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.3" damageDone="2360" finalBlow="0" weaponTypeID="2466" shipTypeID="11200" />
          <row characterID="636046666" characterName="Mr Inevitability" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="5" damageDone="1164" finalBlow="0" weaponTypeID="24495" shipTypeID="11176" />
          <row characterID="365949102" characterName="Fumb Duck" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-0.1" damageDone="1068" finalBlow="0" weaponTypeID="16523" shipTypeID="11198" />
          <row characterID="1901781606" characterName="Surielle Zapata" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="0.8" damageDone="1038" finalBlow="0" weaponTypeID="27361" shipTypeID="11379" />
          <row characterID="878728887" characterName="Kal Shakai" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-4.5" damageDone="866" finalBlow="0" weaponTypeID="27315" shipTypeID="11400" />
          <row characterID="1409795219" characterName="skyterd2008" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.4" damageDone="459" finalBlow="0" weaponTypeID="27361" shipTypeID="22464" />
          <row characterID="376147608" characterName="Dreamchasr" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="5" damageDone="100" finalBlow="0" weaponTypeID="527" shipTypeID="11176" />
          <row characterID="1103002374" characterName="BlackRain McMillan" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.8" damageDone="0" finalBlow="0" weaponTypeID="3178" shipTypeID="12042" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="2299" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="11561" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="1952" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="16519" flag="0" qtyDropped="1" qtyDestroyed="5" />
          <row typeID="203" flag="5" qtyDropped="0" qtyDestroyed="12631" />
          <row typeID="29009" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="10888" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="16303" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="203" flag="0" qtyDropped="120" qtyDestroyed="24" />
          <row typeID="22291" flag="0" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="11577" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="2048" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="26030" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="1447" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="29011" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="26026" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2303" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2183" flag="87" qtyDropped="1" qtyDestroyed="6" />
        </rowset>
      </row>
      <row killID="6338441" solarSystemID="30003321" killTime="2009-03-29 20:50:00" moonID="0">
        <victim characterID="159233427" characterName="radiogaga" corporationID="828800677" corporationName="Sniggerdly" allianceID="386292982" allianceName="Pandemic Legion" factionID="0" factionName="" damageTaken="245" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1901781606" characterName="Surielle Zapata" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="0.83960728326493" damageDone="245" finalBlow="1" weaponTypeID="10680" shipTypeID="11200" />
          <row characterID="1868072702" characterName="Rockstara" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.2" damageDone="0" finalBlow="0" weaponTypeID="448" shipTypeID="11200" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6338409" solarSystemID="30003321" killTime="2009-03-29 20:49:00" moonID="0">
        <victim characterID="159233427" characterName="radiogaga" corporationID="828800677" corporationName="Sniggerdly" allianceID="386292982" allianceName="Pandemic Legion" factionID="0" factionName="" damageTaken="528" shipTypeID="11200" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1868072702" characterName="Rockstara" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.24600403951789" damageDone="528" finalBlow="1" weaponTypeID="3170" shipTypeID="11200" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="4027" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="22961" flag="5" qtyDropped="464" qtyDestroyed="0" />
          <row typeID="3244" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="12612" flag="5" qtyDropped="0" qtyDestroyed="1299" />
          <row typeID="1236" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3170" flag="0" qtyDropped="1" qtyDestroyed="2" />
          <row typeID="10190" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="440" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="12612" flag="0" qtyDropped="316" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6337931" solarSystemID="30003349" killTime="2009-03-29 20:24:00" moonID="0">
        <victim characterID="1834606348" characterName="artemidoro" corporationID="1541164645" corporationName="Hikage Corporation" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" damageTaken="313" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1409795219" characterName="skyterd2008" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.39122574564441" damageDone="313" finalBlow="1" weaponTypeID="27361" shipTypeID="11379" />
          <row characterID="1901781606" characterName="Surielle Zapata" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="0.8" damageDone="0" finalBlow="0" weaponTypeID="2410" shipTypeID="11993" />
          <row characterID="1672429356" characterName="Jel Malar" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.7" damageDone="0" finalBlow="0" weaponTypeID="2905" shipTypeID="11198" />
          <row characterID="502417576" characterName="AyuTokin Tumi" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.3" damageDone="0" finalBlow="0" weaponTypeID="3170" shipTypeID="11200" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6337906" solarSystemID="30003349" killTime="2009-03-29 20:23:00" moonID="0">
        <victim characterID="1834606348" characterName="artemidoro" corporationID="1541164645" corporationName="Hikage Corporation" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" damageTaken="1179" shipTypeID="587" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1409795219" characterName="skyterd2008" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.39122574564441" damageDone="322" finalBlow="1" weaponTypeID="27361" shipTypeID="11379" />
          <row characterID="1103002374" characterName="BlackRain McMillan" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.8" damageDone="207" finalBlow="0" weaponTypeID="2185" shipTypeID="12023" />
          <row characterID="1901781606" characterName="Surielle Zapata" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="0.8" damageDone="206" finalBlow="0" weaponTypeID="2410" shipTypeID="11993" />
          <row characterID="878728887" characterName="Kal Shakai" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-4.5" damageDone="177" finalBlow="0" weaponTypeID="27441" shipTypeID="11993" />
          <row characterID="747677046" characterName="Ciryon Atani" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.5" damageDone="163" finalBlow="0" weaponTypeID="27441" shipTypeID="11993" />
          <row characterID="365949102" characterName="Fumb Duck" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-0.1" damageDone="104" finalBlow="0" weaponTypeID="2488" shipTypeID="11963" />
          <row characterID="1520592339" characterName="Stria Shijera" corporationID="1541164645" corporationName="Hikage Corporation" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" securityStatus="5" damageDone="0" finalBlow="0" weaponTypeID="22778" shipTypeID="22456" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="1403" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="16521" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="27333" flag="5" qtyDropped="0" qtyDestroyed="20" />
          <row typeID="181" flag="0" qtyDropped="107" qtyDestroyed="192" />
          <row typeID="185" flag="5" qtyDropped="0" qtyDestroyed="500" />
          <row typeID="520" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="486" flag="0" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="439" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="526" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="1244" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="27315" flag="0" qtyDropped="12" qtyDestroyed="0" />
          <row typeID="5399" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="8865" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="27321" flag="5" qtyDropped="0" qtyDestroyed="5" />
          <row typeID="181" flag="5" qtyDropped="0" qtyDestroyed="500" />
        </rowset>
      </row>
      <row killID="6337893" solarSystemID="30003349" killTime="2009-03-29 20:22:00" moonID="0">
        <victim characterID="1584517905" characterName="Manolo Dux" corporationID="1541164645" corporationName="Hikage Corporation" allianceID="309619061" allianceName="Eradication Alliance" factionID="0" factionName="" damageTaken="13183" shipTypeID="24702" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="747677046" characterName="Ciryon Atani" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.54103657344729" damageDone="3583" finalBlow="1" weaponTypeID="27441" shipTypeID="11993" />
          <row characterID="1901781606" characterName="Surielle Zapata" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="0.8" damageDone="3249" finalBlow="0" weaponTypeID="27441" shipTypeID="11993" />
          <row characterID="878728887" characterName="Kal Shakai" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-4.5" damageDone="2352" finalBlow="0" weaponTypeID="27441" shipTypeID="11993" />
          <row characterID="334945037" characterName="Zenethian" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.5" damageDone="1695" finalBlow="0" weaponTypeID="27441" shipTypeID="11993" />
          <row characterID="1103002374" characterName="BlackRain McMillan" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.8" damageDone="831" finalBlow="0" weaponTypeID="12023" shipTypeID="12023" />
          <row characterID="365949102" characterName="Fumb Duck" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-0.1" damageDone="814" finalBlow="0" weaponTypeID="2488" shipTypeID="11963" />
          <row characterID="1672429356" characterName="Jel Malar" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="2.7" damageDone="371" finalBlow="0" weaponTypeID="11198" shipTypeID="11198" />
          <row characterID="502417576" characterName="AyuTokin Tumi" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="4.3" damageDone="288" finalBlow="0" weaponTypeID="11200" shipTypeID="11200" />
          <row characterID="1409795219" characterName="skyterd2008" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.4" damageDone="0" finalBlow="0" weaponTypeID="8089" shipTypeID="11379" />
          <row characterID="1868072702" characterName="Rockstara" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.2" damageDone="0" finalBlow="0" weaponTypeID="11200" shipTypeID="11200" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="27401" flag="0" qtyDropped="106" qtyDestroyed="0" />
          <row typeID="448" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="519" flag="0" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="1973" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="11317" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="1306" flag="0" qtyDropped="0" qtyDestroyed="2" />
          <row typeID="25713" flag="0" qtyDropped="2" qtyDestroyed="0" />
          <row typeID="21896" flag="0" qtyDropped="50" qtyDestroyed="250" />
          <row typeID="4025" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="2048" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="5975" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="27401" flag="5" qtyDropped="0" qtyDestroyed="452" />
          <row typeID="29011" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="2486" flag="87" qtyDropped="6" qtyDestroyed="0" />
          <row typeID="2913" flag="0" qtyDropped="4" qtyDestroyed="2" />
          <row typeID="21896" flag="5" qtyDropped="628" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6336727" solarSystemID="30003322" killTime="2009-03-29 19:29:00" moonID="0">
        <victim characterID="1255385180" characterName="Alpha Kvaka" corporationID="1000168" corporationName="Federal Navy Academy" allianceID="0" allianceName="" factionID="0" factionName="" damageTaken="205" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="826540579" characterName="The Aegis" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="1.66432693984784" damageDone="205" finalBlow="1" weaponTypeID="3170" shipTypeID="11200" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6336684" solarSystemID="30003322" killTime="2009-03-29 19:27:00" moonID="0">
        <victim characterID="1255385180" characterName="Alpha Kvaka" corporationID="1000168" corporationName="Federal Navy Academy" allianceID="0" allianceName="" factionID="0" factionName="" damageTaken="37" shipTypeID="606" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="826540579" characterName="The Aegis" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="1.66432693984784" damageDone="37" finalBlow="1" weaponTypeID="3170" shipTypeID="11200" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="3651" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="34" flag="5" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="3640" flag="0" qtyDropped="1" qtyDestroyed="0" />
        </rowset>
      </row>
      <row killID="6336249" solarSystemID="30003321" killTime="2009-03-29 19:06:00" moonID="0">
        <victim characterID="157511159" characterName="NightFrost" corporationID="1952236257" corporationName="Project 0 Corp" allianceID="1847809696" allianceName="Outer Ring Exhumation Inc." factionID="0" factionName="" damageTaken="438" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="167284938" characterName="Silurus" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.59633001464344" damageDone="438" finalBlow="1" weaponTypeID="2969" shipTypeID="24702" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
      <row killID="6336219" solarSystemID="30003321" killTime="2009-03-29 19:04:00" moonID="0">
        <victim characterID="157511159" characterName="NightFrost" corporationID="1952236257" corporationName="Project 0 Corp" allianceID="1847809696" allianceName="Outer Ring Exhumation Inc." factionID="0" factionName="" damageTaken="1236" shipTypeID="11377" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="167284938" characterName="Silurus" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="3.59633001464344" damageDone="1236" finalBlow="1" weaponTypeID="2969" shipTypeID="24702" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed">
          <row typeID="5280" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="12620" flag="0" qtyDropped="0" qtyDestroyed="200" />
          <row typeID="3098" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="13320" flag="0" qtyDropped="2" qtyDestroyed="1" />
          <row typeID="205" flag="5" qtyDropped="340" qtyDestroyed="0" />
          <row typeID="12620" flag="5" qtyDropped="277" qtyDestroyed="0" />
          <row typeID="5299" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="29015" flag="0" qtyDropped="1" qtyDestroyed="0" />
          <row typeID="22291" flag="0" qtyDropped="1" qtyDestroyed="1" />
          <row typeID="11370" flag="0" qtyDropped="0" qtyDestroyed="1" />
          <row typeID="205" flag="0" qtyDropped="40" qtyDestroyed="20" />
        </rowset>
      </row>
      <row killID="6335972" solarSystemID="30003321" killTime="2009-03-29 18:52:00" moonID="0">
        <victim characterID="1255385180" characterName="Alpha Kvaka" corporationID="1000168" corporationName="Federal Navy Academy" allianceID="0" allianceName="" factionID="0" factionName="" damageTaken="391" shipTypeID="670" />
        <rowset name="attackers" columns="characterID,characterName,corporationID,corporationName,allianceID,allianceName,factionID,factionName,securityStatus,damageDone,finalBlow,weaponTypeID,shipTypeID">
          <row characterID="1868072702" characterName="Rockstara" corporationID="1976909889" corporationName="Clown Punchers." allianceID="422458199" allianceName="Clown Punchers Syndicate" factionID="0" factionName="" securityStatus="-1.24600403951789" damageDone="391" finalBlow="1" weaponTypeID="3170" shipTypeID="11200" />
        </rowset>
        <rowset name="items" columns="typeID,flag,qtyDropped,qtyDestroyed" />
      </row>
    </rowset>
  </result>
  <cachedUntil>2009-04-01 16:23:26</cachedUntil>
</eveapi>'''