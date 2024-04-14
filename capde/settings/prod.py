import environ
from .base import *

ALLOWED_HOSTS = ['223.130.134.111']




DEBUG = False



env = environ.Env()
environ.Env.read_env(BASE_DIR/'.env')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('Backend'),
        'USER': env('dbmasteruser'),
        'PASSWORD': env('lc3_Kd&0:>d;TVC*:^6Yt-J74^4RUl'),
        'HOST': env('ls-a9d78eef4acd00c7534698674be58ecdfb986bd0.cn088usqyhrd.ap-northeast-2.rds.amazonaws.com'), 
        'PORT': '5432',
    }
}