from django.shortcuts import render
from rest_framework import status, viewsets
from accounts.serializers import RegisterUserSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

from accounts.models import User


class RegisterUserViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterUserSerializer
    permission_classes = []
    http_method_names = ['post']
    queryset = User.objects.all()

    @action(detail=False, methods=['post'])
    def create_user(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print('injs')
            return Response({'status': status.HTTP_201_CREATED})
        else:
            print('pos')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
