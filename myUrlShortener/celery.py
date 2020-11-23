from django.conf import settings
from celery import Celery
import django
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myUrlShortener.settings')
django.setup()

celery_app = Celery('myUrlShortener')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
