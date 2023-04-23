from django.db.models import fields
from rest_framework import serializers
from ..models.user import User


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class UserUpdateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    previous_password = serializers.CharField()