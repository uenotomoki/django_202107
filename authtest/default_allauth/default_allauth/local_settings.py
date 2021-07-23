import os

SECRET_KEY = 'nlk4rm9odxs%)jv3zv7luppk3p&s6_e4l0w+j_sip^ojg86k9$'

#settings.pyからそのままコピー
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#settings.pyからそのままコピー
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

