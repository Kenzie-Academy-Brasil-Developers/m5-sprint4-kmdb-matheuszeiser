from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from ..models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    birthdate = serializers.DateField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    bio = serializers.CharField(allow_null=True, default="")
    is_critic = serializers.BooleanField(allow_null=True, default=True)
    updated_at = serializers.DateTimeField(read_only=True)
    is_superuser = serializers.BooleanField(allow_null=True, default=False)

    def validate_email(self, value):
        email_already_exists = User.objects.filter(email=value).exists()

        if email_already_exists:
            raise serializers.ValidationError(detail="Email already exists")
        return value

    def validate_username(self, value):
        username_already_exists = User.objects.filter(username=value).exists()
        if username_already_exists:
            raise serializers.ValidationError(detail="Username is already used")
        return value

    def create(self, validated_data: dict) -> User:
        validated_data["password"] = make_password(validated_data["password"])
        user = User.objects.create(**validated_data)

        return user
