from rest_framework import serializers
from accounts.models import User


class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = [
            'email', 'username', 'password'
        ]

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user


class LoginSerializer(serializers.ModelSerializer):
    pass

    # class Meta:
    #     model = user
    #     fields
