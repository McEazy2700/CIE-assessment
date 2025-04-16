from rest_framework import permissions
from rest_framework.views import Request
from rest_framework.viewsets import ViewSet

from inventory.models.inventory import Product


class IsProductOwner(permissions.BasePermission):
    """
    Custom permission to only allow the owner of a product to edit or delete it.
    """

    def has_object_permission(self, request: Request, view: ViewSet, obj: Product):
        return obj.inventory.owner == request.user
