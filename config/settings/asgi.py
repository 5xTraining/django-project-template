"""
ASGI configurations
"""

from django.core.asgi import get_asgi_application

from manage import set_django_env

set_django_env()

application = get_asgi_application()
