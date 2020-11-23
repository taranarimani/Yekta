from urlShorteners.models import Url
from rest_framework import serializers


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = [
            'base_url', 'short_url'
        ]

    def create(self, validated_data):
        print('qabl')
        validated_data['user'] = self.context.get('request').user.id
        print('baad')
        return super(UrlSerializer, self).create(validated_data)
