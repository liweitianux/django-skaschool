"""
Django settings for django_skaschool project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(__file__)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = open(os.path.join(PROJECT_DIR, 'secret_key.txt')).read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# ALLOWED_HOSTS is required when deploying with DEBUG=False,
# otherwise server will throw 400 bad request errors.
ALLOWED_HOSTS = []


# Application definition
# DEFAULT_APPS: django framework apps
DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
# THIRD_PARTY_APPS
THIRD_PARTY_APPS = (
    'south',
    'bootstrap3',
    'registration',
    'captcha',
)
# LOCAL_APPS
LOCAL_APPS = (
    'account',
    'page',
    'notice',
    'archive',
    'schedule',
    'tools',    # fake app to hold generic utilities
)
# INSTALLED_APPS
INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_skaschool.urls'

WSGI_APPLICATION = 'django_skaschool.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-cn'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

# LOCALE_PATHS: where django looks for translation files
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

USE_TZ = True

# contrib.sites
SITE_ID = 1

# The URL where requests are redirected after login when the
# 'contrib.auth.login' view gets no 'next' parameter.
LOGIN_REDIRECT_URL = '/accounts/profile/'

# The URL where requests are redirected for login,
# especially when using the 'login_required()' decorator.
LOGIN_URL = '/accounts/login/'

# The URL redirected to after logout
LOGOUT_URL = '/accounts/logout/'


## template directories
TEMPLATE_DIRS = (
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates'),
)

## static directories
STATICFILES_DIRS = (
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'static'),
)

## static root
# absolute path to the directory where 'collectstatic' will collect
# static files for deployment
#STATIC_ROOT = '/var/www/example.com/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'

## media root
# absolute filesystem path to the directory that hold user-uploaded files
#MEDIA_ROOT = '/var/www/example.com/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')

# media url
MEDIA_URL = '/media/'

## email settings
from settings_email import *


#################################################
## bootstrap3
# Serve bootstrap3 from local.
# Otherwise 'respond.js' requires extra configuration with css on CDN.
BOOTSTRAP3 = {
    'jquery_url': '//code.jquery.com/jquery-1.11.0.min.js',
    #'base_url': '//netdna.bootstrapcdn.com/bootstrap/3.1.1/',
    'base_url': '/static/third-party/bootstrap/3.1.1/',
    'css_url': None,
    'theme_url': None,
    'javascript_url': None,
    'javascript_in_head': False,
    'horizontal_label_class': 'col-md-2',
    'horizontal_field_class': 'col-md-4',
}

## django-registration
# One-week activation window
ACCOUNT_ACTIVATION_DAYS = 7
# whether registration of new accounts if currently permitted
REGISTRATION_OPEN = True

## django-recaptcha
# global key (recaptcha.net)
RECAPTCHA_PUBLIC_KEY = '6Lf8dvISAAAAAPljExJQcAkx4jDZPOYbTGXYXCME'
RECAPTCHA_PRIVATE_KEY = '6Lf8dvISAAAAAH75mmLlVWOp6JB9Gx6WARR_6HXb'

#################################################
## allowed content types to be uploaded by user
ALLOWED_CONTENT_TYPES = [
    'application/gzip',                 # gzip
    'application/msword',               # doc
    'application/pdf',                  # pdf
    'application/postscript',           # postscript
    'application/rar',                  # rar
    'application/vnd.ms-excel',         # xls
    'application/vnd.oasis.opendocument.spreadsheet',   # ods
    'application/vnd.oasis.opendocument.text',          # odt
    'application/vnd.oasis.opendocument.presentation',  # odp
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',            # xlsx
    'application/vnd.openxmlformats-officedocument.wordprocessingml.document',      # docx
    'application/vnd.openxmlformats-officedocument.presentationml.presentation',    # pptx
    'application/wps-office.doc',       # wps doc/rtf
    'application/wps-office.dps',       # wps dps
    'application/wps-office.et',        # wps et
    'application/wps-office.ppt',       # wps ppt
    'application/wps-office.pptx',      # wps pptx
    'application/wps-office.wps',       # wps wps
    'application/wps-office.xls',       # wps xls
    'application/zip',                  # zip
    'application/x-7z-compressed',      # 7z
    'application/x-bzip2',              # bz2
    'application/x-dvi',                # dvi
    'application/x-latex',              # latex
    'application/x-rar-compressed',     # rar
    'application/x-tar',                # tar
    'image/bmp',                        # bmp
    'image/gif',                        # gif
    'image/jpeg',                       # jpg
    'image/png',                        # png
    'image/tiff',                       # tif
    'text/csv',                         # csv
    'text/plain',                       # txt
    'text/rtf',                         # rtf
    'text/x-markdown',                  # markdown
    'text/x-tex',                       # latex
]
## allowed filesize of uploaded files
ALLOWED_MAX_UPLOAD_SIZE = 10485760      # 10 MB


# vim: set ts=4 sw=4 tw=0 fenc=utf-8 ft=python: 
