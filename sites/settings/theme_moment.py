# -*- coding: UTF-8 -*-
from base import *

PAGINATION_DEFAULT_PAGINATION = 20

TEMPLATE_DIRS += (
    os.path.join(HERE, 'themes/moment/templates'),
)

STATICFILES_DIRS += (
    os.path.join(HERE, 'themes/moment/static'),
)

DPRESS_SHOW_CATEGORYS_NAV = True#show categorys in nav

#DPRESS_NAV = [{"name": u"@github", "link": "https://github.com/vicalloy/"},]
DPRESS_NAV = []
DPRESS_ELSEWHERE = []
