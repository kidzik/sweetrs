import os
import sys
sys.stdout = sys.stderr

os.environ['DJANGO_SETTINGS_MODULE'] = 'sweetrs.settings'

sys.path.append('/usr/lib/python2.5/site-packages/django')
sys.path.append('/var/www/sweetrs.org/web/src')
sys.path.append('/var/www/sweetrs.org/web/src/sweetrs')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
