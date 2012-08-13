from base import *

DEBUG = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#devserver
#MIDDLEWARE_CLASSES += ('devserver.middleware.DevServerMiddleware',)
#INSTALLED_APPS = ('devserver',) + INSTALLED_APPS#devserver must in first

#debug_toolbar
INSTALLED_APPS += ('debug_toolbar',)
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INTERNAL_IPS = ('127.0.0.2',)
