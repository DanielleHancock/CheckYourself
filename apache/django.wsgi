import os
import sys

path = '/var/www/CheckYourself'
if path not in sys.path:
    sys.path.insert(0, '/var/www/CheckYourself')

os.environ['DJANGO_SETTINGS_MODULE'] = 'CheckYourself.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
