from urlShorteners.models import Url
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from urlShorteners.serializers import UrlSerializer
from urlShorteners.permisions import IsUser
from urlShorteners.tasks import short_url_task


# Create your views here.


class UrlViewSet(viewsets.ModelViewSet):

    http_method_names = ['post']
    permission_classes = [IsUser]
    serializer_class = UrlSerializer
    queryset = Url.objects.all()
    throttle_classes = 'create_url_rate_throttle'

    @action(detail=False, methods=['post'])
    def create_url(self, request):
        print('inja')
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            short_url = short_url_task.delay(request.data.get(
                'base_url'), request.data.get('suggestion'), serializer.id)
            serializer.short_url = short_url
            serializer.save()
            return Response(short_url, {'status': status.HTTP_201_CREATED})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
