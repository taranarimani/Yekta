from django.shortcuts import render
from rest_framework import status, viewsets
from accounts.serializers import RegisterUserSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.conf import settings
from django.contrib import auth
from accounts.models import User
import jwt


class RegisterUserViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterUserSerializer
    # permission_classes = [AllowAny]
    permission_classes = []
    http_method_names = ['post']
    queryset = User.objects.all()

    @action(detail=False, methods=['post'])
    def create_user(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'status': status.HTTP_201_CREATED})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginViewSet(viewsets.ModelViewSet):
    serializer_class = UserLoginSerializer
    permission_classes = []
    http_method_names = ['post']
    queryset = User.objects

    @action(detail=False, methods=['post'])
    def login(self, request):
        print('inja')

        data = request.data
        # username = data.get('username')
        if data.get('email'):
            user = self.queryset.get(email=data.get('email'))
            username = user.username
        else:
            username = data.get('username')
        password = data.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            print('inja3')
            auth_token = jwt.encode(
                {'username': user.username}, settings.JWT_SECRET_KEY)
            print('oinawrf')
            serializer = self.serializer_class(user)
            print('inja4')
            data = {
                'user': serializer.data, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)

        return Response({'status': 'un authorized'}, status=status.HTTP_401_UNATHORIZED)
