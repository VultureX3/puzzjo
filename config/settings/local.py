from .base import *

from .base import *

DATABASES['default']['HOST'] = 'localhost'
DATABASES['default']['PORT'] = '5432'

CORS_ORIGIN_ALLOW_ALL = True

ALLOWED_HOSTS = ['*']

EMAIL_HOST = 'localhost'
EMAIL_PORT = 8080
