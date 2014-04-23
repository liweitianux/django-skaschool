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
SECRET_KEY = '3!73+$)!f&z@li7gg^^6w13&*vk#zbw*pue#9u+0l@_(5wocb@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

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
    #'south',
    'bootstrap3',
    'registration',
)
# LOCAL_APPS
LOCAL_APPS = (
    'account',
    'page',
    'notice',
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

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_skaschool',
        'USER': 'astro',
        'PASSWORD': 'astro',
        'HOST': '',     # default: localhost
        'PORT': '',     # default: 3306
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
BOOTSTRAP3 = {
    'jquery_url': '//code.jquery.com/jquery-1.11.0.min.js',
    'base_url': '//netdna.bootstrapcdn.com/bootstrap/3.1.1/',
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

# vim: set ts=4 sw=4 tw=0 fenc=utf-8 ft=python: 
