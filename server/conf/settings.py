"""
Evennia settings file.
The available options are found in the default settings file found
here:
{settings_default}
Remember:
Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.
When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).
"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "Cursed Library"

# own changes
TELNET_ENABLED = True
TELNET_PORTS = [13133]
#TELNET_INTERFACES = ['192.168.137.49']

#WEBSERVER_INTERFACES = ['192.168.137.49']
#WEBSERVER_PORTS = [(13130, 5001)]
#ALLOWED_HOSTS = ["*"]

TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'de-de'

#IDMAPPER_CACHE_MAXSIZE = 100      # (MB)
TIME_FACTOR = 1.0

GUEST_ENABLED = True
GUEST_LIST = ["Sissy-" + str(s+1) for s in range(9)]

IRC_ENABLED = True

######################################################################
# Django web features
######################################################################


# The secret key is randomly seeded upon creation. It is used to sign
# Django's cookies. Do not share this with anyone. Changing it will
# log out all active web browsing sessions. Game web client sessions
# may survive.
SECRET_KEY = '5(r:%@Gmg-?}NU3d[/ul8+t.SJ$",c`|qxsDo"Z='

# Allow multiple sessions per player; one character per session
MULTISESSION_MODE = 2
MAX_NR_CHARACTERS = 10

# Other defaults
PROTOTYPE_MODULES = ('world.content.prototypes_armor',
                     'world.content.prototypes_items',
                     'world.content.prototypes_misc',
                     'world.content.prototypes_mobs',
                     'world.content.prototypes_weapons'
                     )
BASE_BATCHPROCESS_PATHS = ['world.content', 'evennia.contrib']

<<<<<<< HEAD
######################################################################
# Evennia Database config
######################################################################

# Database config syntax:
# ENGINE - path to the the database backend. Possible choices are:
#            'django.db.backends.sqlite3', (default)
#            'django.db.backends.mysql',
#            'django.db.backends.postgresql_psycopg2',
#            'django.db.backends.oracle' (untested).
# NAME - database name, or path to the db file for sqlite3
# USER - db admin (unused in sqlite3)
# PASSWORD - db admin password (unused in sqlite3)
# HOST - empty string is localhost (unused in sqlite3)
# PORT - empty string defaults to localhost (unused in sqlite3)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(GAME_DIR, "server", "evennia.db3"),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''
        }}

######################################################################
# Django web features
######################################################################

# Absolute path to the directory that holds file uploads from web apps.
# Example: "/home/media/media.lawrence.com"
MEDIA_ROOT = os.path.join(GAME_DIR, "web", "media")

# The master urlconf file that contains all of the sub-branches to the
# applications. Change this to add your own URLs to the website.
ROOT_URLCONF = 'web.urls'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure
# to use a trailing slash. Django1.4+ will look for admin files under
# STATIC_URL/admin.
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(GAME_DIR, "web", "static")

# Directories from which static files will be gathered from.
STATICFILES_DIRS = (
    os.path.join(GAME_DIR, "web", "static_overrides"),
    os.path.join(EVENNIA_DIR, "web", "static"),)

# We setup the location of the website template as well as the admin site.
TEMPLATE_DIRS = (
    os.path.join(GAME_DIR, "web", "template_overrides"),
    os.path.join(EVENNIA_DIR, "web", "templates", ACTIVE_TEMPLATE),
    os.path.join(EVENNIA_DIR, "web", "templates"),)

# The secret key is randomly seeded upon creation. It is used to sign
# Django's cookies. Do not share this with anyone. Changing it will
# log out all active web browsing sessions. Game web client sessions
# may survive.
SECRET_KEY = '5(r:%@Gmg-?}2b354234v52%"34vfg$,c`|qxsDo"Z='
=======
>>>>>>> 4d75b9d5e80f939195614174b8cc70050bb36d2c
