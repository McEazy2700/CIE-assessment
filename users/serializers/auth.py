from typing import Any
from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.models.auth import TimedAuthToken
from users.serializers.users import UserSerializer


class AuthLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={"input_type": "password"})


class AuthSignUpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password1 = serializers.CharField(write_only=True, style={"input_type": "password"})
    password2 = serializers.CharField(write_only=True, style={"input_type": "password"})

    def validate(self, data: dict[str, Any]):
        """
        Check that the passwords match.
        """
        User = get_user_model()

        if User.objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError({"email": "Email already exists"})

        if data["password1"] != data["password2"]:
            raise serializers.ValidationError({"password2": "Passwords don't match."})
        return data


class TimedAuthTokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TimedAuthToken
        fields = ["token", "refresh_token", "user"]
