from .common import *

DEBUG = True
SECRET_KEY = 'django-insecure-51j2hpj&6a^fo5if*$r7)^e9vkkmmbcq01@f$bd@126j0vy8vy'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ecommerce',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '123654789'

    }
}


CELERY_BROKER_URL = 'redis://redis:6379/1'
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://localhost:6379/2',
        'TIMEOUT': 10 * 60,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

EMAIL_HOST = 'smtp4dev'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 2525

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True
}
