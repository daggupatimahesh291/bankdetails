"""
WSGI config for simple project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""
path = "/home/daggupatimahesh291/simple"
import sys,os
from django.core.wsgi import get_wsgi_application
if path not in sys.path:
    sys.path.insert(0, path)

os.environ["DJANGO_SETTINGS_MODULE"] = "simple.settings"


application = get_wsgi_application()
