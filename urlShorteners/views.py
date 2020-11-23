from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from urlShorteners.serializers import UrlSerializer
from urlShorteners.permisions import IsUser
from urlShorteners.models import Url
from urlShorteners.tasks import addba


# Create your views here.


class UrlViewSet(viewsets.ModelViewSet):
    print('inja')
    http_method_names = ['post']
    permission_classes = [IsUser]
    serializer_class = UrlSerializer
    queryset = Url.objects.all()

    @action(detail=False, methods=['post'])
    def create_url(self, request):
        print('injajj')
        addba.delay(3, 4)
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            print('valid')
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
