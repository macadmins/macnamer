import os, sys
import site

MACNAMER_ENV_DIR = '/home/app/macnamer'

# Use site to load the site-packages directory of our virtualenv
site.addsitedir(os.path.join(MACNAMER_ENV_DIR, 'lib/python2.7/site-packages'))

# Make sure we have the virtualenv and the Django app itself added to our path
sys.path.append(MACNAMER_ENV_DIR)
sys.path.append(os.path.join(MACNAMER_ENV_DIR, 'macnamer'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "macnamer.settings")
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()