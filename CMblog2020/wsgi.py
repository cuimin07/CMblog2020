"""
WSGI config for CMblog2020 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('CMblog2020.settings.production', 'CMblog2020.settings')

application = get_wsgi_application()
