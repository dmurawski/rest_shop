from .common import *


DEBUG = True
SECRET_KEY = "django-insecure-&#t@6e*^oplc(zj=7md0ha+3wp*@0$4#&tez96+2r2pv9=1k)("

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "storefront3_db",
        "HOST": "localhost",
        "USER": "root",
        "PASSWORD": "root",
        "PORT": 3307,
    }
}
