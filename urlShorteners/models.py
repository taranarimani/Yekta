from django.db import models
from django.urls import reverse
from accounts.models import User
from hashlib import md5
# from pyshorteners import Shortener
import re
import random
import string


class Url(models.Model):

    base_url = models.URLField()
    short_url = models.URLField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    visits = models.IntegerField(default=0)
    user = models.ForeignKey(to=User,
                             on_delete=models.CASCADE,
                             related_name="user")

    class Meta:
        verbose_name = ("Url")
        verbose_name_plural = ("Urls")
        ordering = ['-create_time']

    def __str__(self):
        return f"baseUrl:{self.base_url},visits:{self.visits}"

    def get_absolute_url(self):
        return reverse('', args=[self.create_time, self.base_url])


class UrlInfo(models.Model):

    DEVISE_MODELS = (
        ('mobile', 'Mobile'),
        ('desktop', 'Desktop'),
    )

    url = models.ForeignKey(to=Url,
                            on_delete=models.CASCADE,
                            related_name="url")
    use_time = models.DateTimeField(auto_now_add=True)
    device = models.CharField(max_length=20, choices=DEVISE_MODELS)
    browser = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Short Url Informations")
        verbose_name_plural = ("Short Urls Informations")
        ordering = ['-use_time', 'url']

    def click(self):
        self.url.visits += 1
        self.save()

    def __str__(self):
        return f"base url:{self.url.base_url},device:{self.device},use time:{self.use_time}"
