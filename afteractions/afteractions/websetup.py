"""Setup the afteractions application"""
import logging

from afteractions.config.environment import load_environment
from afteractions.model import meta, Alliance, Config

from afteractions.lib.helpers import random_string

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup afteractions here"""
    load_environment(conf.global_conf, conf.local_conf)

    # Create the tables if they don't already exist
    meta.metadata.create_all(bind=meta.engine)
    
    password = random_string()
    config = Config()
    config.set('password', password, salt=True)
    meta.Session.commit()
    
    log.info('Temporary administrative password is: %s' % (password))