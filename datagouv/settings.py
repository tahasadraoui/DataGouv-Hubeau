"""
Django settings for datagouv project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import sys
import logging
import datetime
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3zrs@no=$jlt*!&xi8*r7w_il)-r$f@ae#-)d)i5i!u2u1d@2x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # DRF
    'rest_framework',
    'drf_yasg',
    'django_filters',

    # Unit tests
    'django_nose',

    # Project apps
    'datagouv.api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'datagouv.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'datagouv.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'datagouv',
        'USER': 'datagouvmaster',
        'PASSWORD': 'Datagouv$2021',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser',
    ],
}

# Remove Django Login
SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
}

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# Logging
# https://docs.djangoproject.com/en/3.1/topics/logging/#configuring-logging
DEFAUT_LOGGING_LEVEL = 'INFO'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        # 'standard': {
        #     'format': '[%(asctime)s] [%(levelname)s] [%(name)s:%(module)s:%(lineno)s - %(funcName)s()] %(message)s'
        # },
        'standard': {
            'format': '[%(asctime)s] [%(levelname)s] [%(name)s:%(module)s:%(lineno)s] %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': DEFAUT_LOGGING_LEVEL,
        },
        'file_incoming': {
            'level': DEFAUT_LOGGING_LEVEL,
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/datagouv.log',
            'maxBytes': 1024*1024*5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'file_outgoing': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'standard',
            'level': DEFAUT_LOGGING_LEVEL,
            'filename': 'logs/datagouv.outgoing.'+str(datetime.date.today())+'.log',
            'when': 'D',
            'interval': 1
        },
    },
    'loggers': {
        'DataGouv': {
            'handlers': ['file_incoming', 'console'],
            'level': DEFAUT_LOGGING_LEVEL,
            'propagate': False
        },
        'django': {
            'handlers': ['file_incoming', 'console'],
            'level': 'INFO',
            'propagate': False
        },
        'django.server': {
            'handlers': ['file_incoming', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # 'django.db.backends': {
        #     'handlers': ['file_outgoing', 'console'],
        #     'level': 'DEBUG',
        #     'propagate': False,
        # },
        'urllib3.connectionpool': {
            'handlers': ['file_outgoing', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
        'requests.packages.urllib3': {
            'handlers': ['file_outgoing', 'console'],
            'level': 'INFO',
            'propagate': False,
        }
    }
}

# Unit tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--cover-html-dir=reports/cover']

TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'
if TESTING:
    logging.disable(logging.CRITICAL)
