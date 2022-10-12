"""
WSGI config for pysakoinnin_sahk_asiointi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pysakoinnin_sahk_asiointi.settings")

application = get_wsgi_application()
