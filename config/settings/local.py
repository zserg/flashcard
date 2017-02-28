from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY',default='+8e%yero&%=^vgn6dm==h8fq)eie&gg*gg=d85gtq=#n7()2$=')

DEBUG = env.bool('DJANGO_DEBUG', default=True)


