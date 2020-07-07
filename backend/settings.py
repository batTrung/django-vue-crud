import os
import string

import dj_database_url
from decouple import Csv, config


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ==============================================================================
# CORE SETTINGS
# ==============================================================================

SECRET_KEY = config('SECRET_KEY', default=string.ascii_letters)

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1,localhost', cast=Csv())

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'corsheaders',
    'django_filters',
]

LOCAL_APPS = [
    'apps.common.apps.CommonConfig',
    'apps.core.apps.CoreConfig',
    'apps.accounts.apps.AccountsConfig',
    'apps.bookstore.apps.BookstoreConfig',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

SITE_ID = 1

INTERNAL_IPS = ['127.0.0.1']

if config("USE_DOCKER", default=False, cast=bool):
    import socket
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())  # noqa
    INTERNAL_IPS += [ip[:-1] + "1" for ip in ips]

ROOT_URLCONF = 'backend.urls'

WSGI_APPLICATION = 'backend.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL', default='sqlite:///%s' % os.path.join(BASE_DIR, 'db.sqlite3'))
    )
}

ADMIN_URL = config('ADMIN_URL', default='admin/')


# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ==============================================================================
# TEMPLATES SETTINGS
# ==============================================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'dist'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ==============================================================================
# AUTHENTICATION AND AUTHORIZATION SETTINGS
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "none"

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

AUTH_USER_MODEL = 'accounts.CustomUser'


# ==============================================================================
# INTERNATIONALIZATION AND LOCALIZATION SETTINGS
# ==============================================================================

LANGUAGE_CODE = config('LANGUAGE_CODE', default='en')

TIME_ZONE = config('TIME_ZONE', default='UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True


# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# ==============================================================================
# STATIC & MEDIA FILES SETTINGS
# ==============================================================================

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'dist', 'static'),
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# ==============================================================================
# THIRD-PARTY APPS SETTINGS
# ==============================================================================

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'backend.pagination.CustomPageNumberPagination',
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
}

CORS_ORIGIN_WHITELIST = config(
    'CORS_ORIGIN_WHITELIST',
    default='http://localhost:8080,http://127.0.0.1:8080',
    cast=Csv(),
)

REST_USE_JWT = True

SWAGGER_SETTINGS = {
    'LOGIN_URL': 'account_login',
    'LOGOUT_URL': 'account_logout',
}
