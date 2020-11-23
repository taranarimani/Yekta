from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from urlShorteners.serializers import UrlSerializer
from urlShorteners.permisions import IsUser
from urlShorteners.models import Url


# Create your views here.


class UrlViewSet(viewsets.ModelViewSet):

    http_method_names = ['post']
    permission_classes = [IsUser]
    serializer_class = UrlSerializer
    queryset = Url.objects.all()

    @action(detail=False, methods=['post'])
    def create_url(self, request):
        pass
