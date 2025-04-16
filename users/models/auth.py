import base64
from datetime import timedelta
import os
from typing import Any
from django.utils import timezone
import jwt
import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings

User = get_user_model()


class TimedAuthToken(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, unique=True
    )

    token = models.CharField(max_length=500)
    refresh_token = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    expires_at = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_used = models.DateTimeField(auto_now=True)

    def save(self, *args: Any, **kwargs: dict[str, Any]) -> None:
        AUTH_TOKEN = settings.AUTH_TOKEN

        if not self.refresh_token:
            self.refresh_token = base64.urlsafe_b64encode(os.urandom(30)).decode()

        if not self.token:
            self.token = jwt.encode(
                {
                    "email": self.user.email,
                    "iat": timezone.now(),
                    "exp": timezone.now()
                    + timedelta(hours=AUTH_TOKEN.get("KEY_VALID_HOURS", 24)),
                },
                settings.SECRET_KEY,
            )

        self.expires_at = timezone.now() + timedelta(
            hours=AUTH_TOKEN.get("REFRESH_VALID_HOURS", 24 * 7)
        )

        return super(TimedAuthToken, self).save(*args, **kwargs)
