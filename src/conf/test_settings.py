from .settings import *
DATABASES['default'] = {
  'ENGINE': 'django.db.backends.postgresql_psycopg2',
  'NAME': 'test_db',
  'USER': 'postgres',
  'PASSWORD': 'root',
  'HOST': 'localhost',  # Empty for localhost through domain sockets or'127.0.0.1' for localhost through TCP.
  'PORT': '5432',
}

DEBUG = True

USE_TZ = False

# Importing here appconfig file
from .appconfig import *