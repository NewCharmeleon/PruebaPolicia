"""
WSGI config for PruebaPolicia project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PruebaPolicia.settings")
sys.path.append('/var/django-projects/PruebaPolicia/')
sys.path.append('/var/django-projects')


application = get_wsgi_application()

