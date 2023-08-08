from .base import *
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('NAME'),
        'USER': os.environ.get('USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': 5432
    }
}
ALLOWED_HOSTS=['*']