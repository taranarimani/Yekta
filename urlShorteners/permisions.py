from rest_framework.permissions import BasePermission
from django.utils.translation import gettext_lazy as _
from accounts.models import User
from urlShorteners.models import Url


class IsUser(BasePermission):

    msg = "you don't have access"

    def has_permission(self, request, view):

        result = True
        try:
            User.objects.get(email=request.user)
        except User.DoesNotExist:
            result = False
        return result
