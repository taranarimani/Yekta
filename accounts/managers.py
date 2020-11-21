from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, username=None, email=None, password=None):

        if not username:
            raise ValueError(_('user must have username'))
        if not email:
            raise ValueError(_('user must have email'))

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username=None, email=None, password=None):
        user = self.create_user(
            username=username, email=email, password=password)
        user.admin = True
        user.save(using=self._db)
        return user
