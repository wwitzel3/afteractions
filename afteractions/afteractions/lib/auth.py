from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect
from pylons import url
from decorator import decorator

def require_admin(f, *args, **kws):
    try:
        admin = session.get('admin')
        if not admin:
                return redirect(url(controller="home", action="index"))
        else:
            return f(*args, **kws)
    except AttributeError, e:
        # trying to access a dead profile in memory, redirect to logout
        return redirect(url(controller="home", action="index"))
require_admin = decorator(require_admin)
