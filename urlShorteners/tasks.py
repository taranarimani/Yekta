from celery import shared_task
from hashlib import md5
# from pyshorteners import Shortener
import re
import random
# import string
import time


@shared_task
def add(x, y):

    return x + y


@shared_task
def task_short_url(base_url, suggestion):

    lenght = 8
    # res = ''.join(random.choices(
    #     string.ascii_uppercase + self.create_time, k=n))
    res = ''.join(random.choices(
        base_url + time.time(), k=n))
    # short_url = Shortener(self.user.username)
    short_url = md5(res.encode()).hexdigest()[:lenght]
    short_url = f"https://myURLshortner.{(re.search('https://(.*)/',base_url)).group(1)}/r/{short_url}{suggestion}"
    # if id is duplicate
    return short_url
