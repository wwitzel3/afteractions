import logging
from datetime import datetime
from sqlalchemy import func, and_, or_

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect
from pylons import config, url

from afteractions.lib.helpers import salted_hash

from afteractions.lib.base import BaseController, render
from afteractions.lib.txtkill import TxtKill
from afteractions.lib.pilot import get_portrait_by_name

from afteractions.model import meta, Kill, Pilot, Item, Group, Config

log = logging.getLogger(__name__)

class HomeController(BaseController):

    def __before__(self):
        c.page = request.params.get('page')
        
        c.alliance_id = config.get('alliance_id')
        c.corp_id = config.get('corp_id')
        
        if not c.page:
            c.page = 1 

    def index(self):
        c.kills = meta.Session.query(Kill)
        
        c.kill_count = c.kills.filter(and_(Kill.corp_id != c.corp_id, Kill.alliance_id != c.alliance_id)).count()
        c.loss_count = c.kills.filter(or_(Kill.corp_id == c.corp_id, Kill.alliance_id == c.alliance_id)).count()
        
        c.ship_classes = Kill.by_class_for_date_range(None, None)
        
        return render('/home/index.html')

    def details(self, id):
        c.kill = meta.Session.query(Kill).filter_by(id=id)
        return render('/home/details.html')
    
    def post(self):
        return render('/home/post.html')
        
    def pilot(self, id):
        c.pilot = meta.Session.query(Pilot).filter_by(id=id).one()
        if not c.pilot.has_portrait():
            c.pilot.eve_id = get_portrait_by_name(c.pilot.name)
            meta.Session.commit()
            
        return render('/home/pilot.html')
    def about(self):
        return render('/home/about.html')
    
    def filter(self, id):
        c.kills = meta.Session.query(Kill).join(Item).join(Group)\
                .filter(Kill.ship_id==Item.id)\
                .filter(Group.id==id)
        print c.kills
        return render('/home/kills.html')
    
    def kills(self):
        c.kills = meta.Session.query(Kill).filter(and_(Kill.corp_id != c.corp_id,
                                                      Kill.alliance_id != c.alliance_id))
        return render('/home/kills.html')
    
    def losses(self):
        c.kills = meta.Session.query(Kill).filter(or_(Kill.corp_id == c.corp_id,
                                                      Kill.alliance_id == c.alliance_id))
        return render('/home/losses.html')
    
    def stats(self):
        return render('/home/stats.html')
    
    def search(self):
        return render('/home/search.html')
    
    def login(self):
        return render('/home/login.html')

    def add_kill(self):
        killmail = request.params.get('killmail')
        kill = TxtKill.parse(killmail)
        return redirect(url(controller='home', action='details', id=kill.id))
