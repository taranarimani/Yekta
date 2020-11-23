from urlShorteners.models import Url
from rest_framework import serializers


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = [
            'base_url'
        ]

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user.id
        validated_data["user_id"] = user
        print(validated_data)
        url = Url.objects.create(**validated_data)
        return url
