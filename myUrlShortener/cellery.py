from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myUrlShortener.settings')
celery_app = Celery('myUrlShortener')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()
