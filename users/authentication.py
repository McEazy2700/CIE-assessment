from django.utils import timezone
import jwt
from typing import Any, Optional, cast
from rest_framework import authentication, exceptions
from rest_framework.views import Request
from django.conf import settings

from users.models.auth import TimedAuthToken


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request: Request):
        authorization = cast(
            Optional[str], cast(dict[str, Any], request.META).get("HTTP_AUTHORIZATION")
        )

        if not authorization:
            return None

        token = authorization.split(" ").pop()
        token = TimedAuthToken.objects.filter(token=token).first()
        if not token:
            raise exceptions.AuthenticationFailed("Invalid token")
        token.last_used = timezone.now()
        token.save()

        jwt.decode(token.token, settings.SECRET_KEY, algorithms=["HS256"])

        return (token.user, None)

    def authenticate_header(self, request: Request):
        return cast(Any, 'Bearer realm="api"')
