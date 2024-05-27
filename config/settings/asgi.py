"""
ASGI configurations
"""

from os import environ as ENV
from manage import set_django_env
from django.core.asgi import get_asgi_application

set_django_env()

application = get_asgi_application()
