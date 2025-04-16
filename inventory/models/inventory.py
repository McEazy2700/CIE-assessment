from typing import Any
import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

User = get_user_model()


class Inventory(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, unique=True
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)


class Category(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, unique=True
    )

    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args: Any, **kwargs: dict[str, Any]):
        self.slug = slugify(self.name)

        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, unique=True
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    categories = models.ManyToManyField(Category)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args: Any, **kwargs: dict[str, Any]):
        slug_base = slugify(self.name)
        uuid_suffix = str(self.id)[:8]
        self.slug = f"{slug_base}-{uuid_suffix}"

        super().save(*args, **kwargs)
