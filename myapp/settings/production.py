import os
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'NAME': 'my_database',
        'USER': 'root',
        'PASSWORD': 'password',
    }
}



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'HOST': os.environ['MYSQL_ROOT_HOST'],
#         'NAME': os.environ['MYSQL_DATABASE'],
#         'USER': os.environ['MYSQL_USER'],
#         'PASSWORD': os.environ['MYSQL_ROOT_PASSWORD'],
#     }
# }
