"""
WSGI configurations
"""

from django.core.wsgi import get_wsgi_application

from manage import set_django_env

set_django_env()

application = get_wsgi_application()
