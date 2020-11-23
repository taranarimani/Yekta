from celery import shared_task


@shared_task
def addba(a, b):
    return a+b
