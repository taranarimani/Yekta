from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_validation_email_task(user):

    send_mail('validation', 'you register to shortener site ,please confirmation',
              'narimanitara@gmail.com', list(user.email))
