import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect
from pylons import url

from afteractions.lib.base import BaseController, render
from afteractions.lib import auth as auth

from afteractions.lib.helpers import salted_hash
from afteractions.model import meta, Config

log = logging.getLogger(__name__)

class AdminController(BaseController):
    @auth.require_admin
    def index(self):
        return render('/admin/index.html')

    def login(self):
        password = request.params.get('password')        
        config = meta.Session.query(Config).filter_by(name='password').first()
        if password and config:
            password = salted_hash(password, config.salt)
            if password == config.value:
                session['admin'] = True
                session.save()
                return redirect(url(controller='admin', action='index'))
        return redirect(url(controller='home', action='login'))
    
    def logout(self):
        admin = session.get('admin')
        if admin:
            session.pop('admin')
        session.save()
        return redirect(url(controller='admin', action='login'))
