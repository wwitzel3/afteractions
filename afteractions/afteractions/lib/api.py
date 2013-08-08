'''Handles EVE api lookups and parsing of killmails.
This is an expensive parser. The idea is that posts happen once, views
happen a lot, so I am going to do all my updates during the posting process.

This will also populate pilot, corporation, and alliance information based on the
IDs provided in the XML. It will also do a lookup and move pilots and corporations
to new outfits.
'''

import cgi
import urllib, urllib2
import os
import logging

from xml.dom import minidom
from pylons import config
log = logging.getLogger(__name__)

def api_request(api, params):
    try:
        url = 'http://api.eve-online.com/eve/%s.xml.aspx' % (api)
        params = urllib.urlencode(params)

        request = urllib2.Request(url + '?' + params)
        response = urllib2.urlopen(request)
        output = response.read()
        response.close()
        
        xml = minidom.parseString(output)
        return xml
    except urllib2.HTTPError, e:
        log.error("error looking up %s: %s" % (api, e))
        
def eve_central_request(api, params):
    try:
        pass
    except urllib2.HTTPError, e:
        log.error("error eve-central %s: %s" % (api, e))
