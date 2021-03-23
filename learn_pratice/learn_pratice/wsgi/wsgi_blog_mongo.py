
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learn_pratice.settings.dev_mongo')

application = get_wsgi_application()
