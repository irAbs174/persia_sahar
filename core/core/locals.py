from pathlib import Path
from .sec import *
import os


# Base DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

CSRF_TRUSTED_ORIGINS = ['https://8000-cs-256274267521-default.cs-europe-west1-xedi.cloudshell.dev']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# STATIC FILES (CSS, JavaScript, Images)
''' Run command : python3 manage.py collectstatic for collect STATIC FILES '''
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',

    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# STATIC FILES DIRS
STATICFILES_DIRS = ['static']

# Manifest Static Files Storage is recommended in production, to prevent outdated
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# static root Dir configuration 
STATIC_ROOT = '/var/www/public/kikpick/static'

# STATIC URL
STATIC_URL = '/static/'

# Media root Dir configuration
MEDIA_ROOT = 'media'

MEDIA_URL = '/media/'