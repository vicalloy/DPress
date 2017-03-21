from .base import *  # NOQA

DEBUG = False
ALLOWED_HOSTS = ['*']

try:
    import gunicorn  # NOQA
    INSTALLED_APPS += ('gunicorn',)  # NOQA
except:
    pass
