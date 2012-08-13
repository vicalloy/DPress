import os
import sys
import site

def add_site_dir(site_dirs):
    prev_sys_path = list(sys.path) 
    for directory in site_dirs:
        site.addsitedir(directory)
    new_sys_path = [] 
    for item in list(sys.path): 
        if item not in prev_sys_path: 
            new_sys_path.append(item) 
            sys.path.remove(item) 
    sys.path[:0] = new_sys_path 

HERE = os.path.dirname(__file__)
ROOT_PATH = os.path.abspath(os.path.join(HERE, '../'))

ALLDIRS = [os.path.join(ROOT_PATH, 'env/lib/python2.7/site-packages'), os.path.join(ROOT_PATH, 'sites')]
add_site_dir(ALLDIRS)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
