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

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""
"""
# for postgreSQL
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'ecommerce',
       'USER': 'postgres',
       'PASSWORD': '123654789',
       'HOST': '127.0.0.1',
       'PORT': '5432',
   }
}
"""
