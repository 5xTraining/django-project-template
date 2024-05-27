"""
WSGI configurations
"""

from os import environ as ENV
from manage import set_django_env
from django.core.wsgi import get_wsgi_application

set_django_env()

application = get_wsgi_application()
