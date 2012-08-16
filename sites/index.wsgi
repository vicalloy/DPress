#for sae
import os
import sys

app_root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(app_root, 'libs/virtualenv.bundle.zip'))
sys.path.insert(0, app_root)

import tempfile
#tempfile.tempdir = 'tempdir'
#tempfile.tempdir = sae.core.get_tmp_dir()
import StringIO
class StringIOExt(StringIO.StringIO):
    name = ""
    size = 0
def TemporaryFile(mode='w+b', bufsize=-1, suffix="",
                   prefix='', dir=None, delete=True):
    #f = StringIO.StringIO()
    f = StringIOExt()
    return f
tempfile.TemporaryFile = TemporaryFile
tempfile.NamedTemporaryFile = TemporaryFile
 
import sae
import sae.storage
import django.core.handlers.wsgi

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
application = sae.create_wsgi_app(django.core.handlers.wsgi.WSGIHandler())
