from oxiterp.settings.base import *

# Override base.py settings here


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'comitfy-health.db', # This is where you put the name of the db file. 
                 # If one doesn't exist, it will be created at migration time.
    }
}

GCM_APIKEY = "AAAAEgdR9KM:APA91bGJbWnT6MzzKIxRi9aAkfgyWCCRKxMNypBgpVjiM0ywTTU3xUyyK4_8Q3O8j-vVeY_k_genzinOnul2wDJKWQa3cnhuaHvG-3BVmdnjq3H1da1DHeKGjbF9ykimR-DlsC2ktnUw"
EMAIL_HOST = "smtp.yandex.com.tr"
EMAIL_HOST_USER = "test@kulmer.com.tr"
EMAIL_HOST_PASSWORD ="Test2021"
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False

try:
    from oxiterp.settings.local import *
except:
    pass
