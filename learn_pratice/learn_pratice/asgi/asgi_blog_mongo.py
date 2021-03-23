

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learn_pratice.settings.dev_mongo')

application = get_asgi_application()
