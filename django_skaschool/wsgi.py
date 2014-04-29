"""
WSGI config for django_skaschool project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_skaschool.settings")
# use settings_production

#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()

os.environ["DJANGO_SETTINGS_MODULE"] = "django_skaschool.settings_production"

# handler for mod_wsgi to work with apache2 user authentication
# ref: https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/apache-auth/
from django.contrib.auth.handlers.modwsgi import check_password

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()

