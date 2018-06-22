from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='8tk1j@+_7%4yh%c!q5nqhw#bmp!=tubzc5nsi3oupt$ai#^v*x')

DEBUG = env.bool('DJANGO_DEBUG', default=True)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'auction_store',
        'USER': 'auction_store',
        'PASSWORD': '!alpha#1',
        'HOST': '127.0.0.1',
        'PORT': 5432
    }
}