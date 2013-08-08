"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
#from webhelpers.html.tags import checkbox, password
from webhelpers import paginate


import string
import hashlib
from random import choice

def random_string(size=9):
    return ''.join([choice(string.letters + string.digits) for i in range(size)])

def salted_hash(value, salt):
    '''Return a salted hashed value of value'''
    hash = hashlib.sha1(value)
    salted_hash = hashlib.sha1(hash.hexdigest() + salt)
    return salted_hash.hexdigest()