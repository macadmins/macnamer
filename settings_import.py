#!/usr/bin/python
from os import getenv
import locale

# Read list of admins from $DOCKER_MACNAMER_ADMINS env var
admin_list = []
if getenv('DOCKER_MACNAMER_ADMINS'):
    admins_var = getenv('DOCKER_MACNAMER_ADMINS')
    if ',' in admins_var and ':' in admins_var:
        for admin in admins_var.split(':'):
            admin_list.append(tuple(admin.split(',')))
        ADMINS = tuple(admin_list)
    elif ',' in admins_var:
        admin_list.append(tuple(admins_var.split(',')))
        ADMINS = tuple(admin_list)
else:
    ADMINS = (
                ('Admin User', 'admin@test.com')
             )

# Read the preferred time zone from $DOCKER_MACNAMER_TZ, use system locale or
# set to 'America/New_York' if neither are set
if getenv('DOCKER_MACNAMER_TZ'):
    if '/' in getenv('DOCKER_MACNAMER_TZ'):
        TIME_ZONE = getenv('DOCKER_MACNAMER_TZ')
    else: TIME_ZONE = 'America/New_York'
elif getenv('TZ'):
    TIME_ZONE = getenv('TZ')
else:
    TIME_ZONE = 'America/New_York'

# Read the preferred language code from $DOCKER_MACNAMER_LANG, use system locale or
# set to 'en_US' if neither are set
if getenv('DOCKER_MACNAMER_LANG'):
    if '_' in getenv('DOCKER_MACNAMER_LANG'):
        LANGUAGE_CODE = getenv('DOCKER_MACNAMER_LANG')
    else:
        LANGUAGE_CODE = 'en_US'
# elif locale.getdefaultlocale():
#     LANGUAGE_CODE = locale.getdefaultlocale()[0]
else:
    LANGUAGE_CODE = 'en_US'

# Read the list of allowed hosts from the $DOCKER_MACNAMER_ALLOWED env var, or
# allow all hosts if none was set.
if getenv('DOCKER_MACNAMER_ALLOWED'):
    ALLOWED_HOSTS = getenv('DOCKER_MACNAMER_ALLOWED').split(',')
else:
    ALLOWED_HOSTS = ['*']