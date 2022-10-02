from src.settings.base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += []

MIDDLEWARE += []

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
