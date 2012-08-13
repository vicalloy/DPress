SETTINGS = 'dev'
try:
    from pre import SETTINGS
except:
    pass
exec 'from %s import *' % SETTINGS

try:
    from local import *
except:
    pass