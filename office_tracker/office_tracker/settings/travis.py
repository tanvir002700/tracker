import os
from .base import *

SECRET_KEY = '!ok^nac(io_tz+%kc0y&rj)a@1y04@&=g7+#u(_j#$6x^=c**+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

if 'TRAVIS' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE':   'django.db.backends.postgresql_psycopg2',
            'NAME':     'traker',
            'USER':     'postgres',
            'PASSWORD': '',
            'HOST':     'localhost',
            'PORT':     '',
        }
    }
