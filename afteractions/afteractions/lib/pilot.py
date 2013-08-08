'''helper methods for looking up a characterID from name
and fetching a portrait given a characterID.
'''

# Name to ID: http://api.eve-online.com/eve/CharacterID.xml.aspx?names=CCP%20Garthagk
# Portrait Grab: http://img.eve.is/serv.asp?s=256&c=797400947
import cgi
import urllib, urllib2
import os
import logging

from xml.dom import minidom
from pylons import config

from afteractions.lib.api import api_request
from afteractions.model import meta, Pilot, Corp, Alliance

log = logging.getLogger(__name__)

def get_portrait_by_name(name):    
    xml = api_request('CharacterID', {'names':name})
    row = xml.getElementsByTagName("row")[0]
    char_attr = row.attributes['characterID']
    get_portrait_by_id(char_attr.value)
    return char_attr.value

def get_portrait_by_id(charid):
    try:
        root = config.get('portraits')
        if not root:
            raise IOError
                    
        url = 'http://img.eve.is/serv.asp'
        params = urllib.urlencode({'s':256, 'c':charid})
        
        request = urllib2.Request(url + '?' + params)
        response = urllib2.urlopen(request)
        output = response.read()
        
        path =  os.path.join(root, 'portraits', '256', charid + '.jpeg')
        print path
        
        portrait = open(path,'wb')
        portrait.write(output)
        portrait.close()
    
    except urllib2.HTTPError, e:
        print "error saving protrait: %s" % (e)
    except IOError, e:
        print "unable to determine save path, set portraits in you configuration file."

def new_pilot(pilot):
    '''This takes an XML representation of a pilot as produced from eveapi lib when
    parsing the KillLog.aspx.xml requests.
    '''
    pilot_id = pilot.characterID if pilot.characterID else pilot.corporationID
        
    plt = meta.Session.query(Pilot).filter_by(id=pilot_id).first()
    corp = meta.Session.query(Corporation).filter_by(id=pilot.corporationID).first()
    alliance = meta.Session.query(Alliance).filter_by(id=pilot.allianceID).first()
    
    if not alliance and not pilot.allianceID == 0:
        meta.Session.add(Alliance(id=pilot.allianceID,
                                  name=pilot.allianceName))
    
    if not corp:
        meta.Session.add(Corporation(id=pilot.corporationID,
                                     name=pilot.corporationName,
                                     alliance_id=pilot.allianceID))
    else:
        if not corp.alliance_id == pilot.allianceID:
            corp.alliance_id = pilot.allianceID
    
    if not plt:
        pilot_name = pilot.characterName if pilot.characterName else pilot.corporationName
        plt = Pilot(id=pilot_id, name=pilot_name, corp_id=pilot.corporationID)
        meta.Session.add(plt)
    else:
        if not plt.corp_id == pilot.corporationID:
            plt.corp_id = pilot.corporationID
    return (pilot_id, pilot.corporationID, pilot.allianceID)