from rest_framework import authentication, exceptions
from django.conf import settings
from accounts.models import User
import jwt


class JwtAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)
        if not auth_data:
            return None

        prefix, token = auth_data.decode('utf-8').split(' ')
        try:
            payload = jwt.decode(token, settings.JWT_SECRET_KEY)
            user = User.objects.get(username=payload['username'])
            return (user, token)
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed(
                'your token is invalid ! login')
        except jwt.ExpiredSignature as identifier:
            raise exceptions.AuthenticationFailed(
                'your token is expired ! login')
        return super().authenticate(request)
