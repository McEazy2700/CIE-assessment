from typing import Any, cast
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework import exceptions
from rest_framework.decorators import action
from rest_framework.views import Request, Response
from drf_yasg.utils import swagger_auto_schema

from users.models.auth import TimedAuthToken
from users.models.users import CustomUser
from users.serializers.auth import (
    AuthLoginSerializer,
    AuthSignUpSerializer,
    TimedAuthTokenSerializer,
)


class AuthViewSet(viewsets.GenericViewSet):
    @swagger_auto_schema(
        tags=["auth"],
        request_body=AuthSignUpSerializer,
    )
    @action(methods=["POST"], detail=False, url_name="sign_up", url_path="sign_up")
    def sign_up(self, request: Request):
        serializer = AuthSignUpSerializer(data=request.data)
        _ = serializer.is_valid(raise_exception=True)

        validated_data = cast(dict[str, Any], serializer.validated_data)

        _ = CustomUser.objects.create_user(
            email=validated_data.get("email", ""),
            password=validated_data.get("password1", ""),
        )

        return Response(
            {"message": "User signup successfull"}, status=status.HTTP_201_CREATED
        )

    @swagger_auto_schema(
        tags=["auth"],
        request_body=AuthLoginSerializer,
    )
    @action(methods=["POST"], detail=False, url_name="sign_in", url_path="sign_in")
    def sign_in(self, request: Request):
        serializer = AuthLoginSerializer(data=request.data)
        _ = serializer.is_valid(raise_exception=True)

        validated_data = cast(dict[str, Any], serializer.validated_data)

        user = get_object_or_404(CustomUser, email=validated_data.get("email", ""))
        if not user.check_password(validated_data.get("password", "")):
            raise exceptions.AuthenticationFailed("Incorrect email or password")

        token = TimedAuthToken.objects.create(user=user)

        return Response(
            {
                "message": "Sign in successful",
                "data": TimedAuthTokenSerializer(token).data,
            },
            status=status.HTTP_201_CREATED,
        )
