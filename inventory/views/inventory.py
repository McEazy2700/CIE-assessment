from typing import Any
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.views import Request, Response

from inventory.filters.products import ProductsFilter
from inventory.models.inventory import Category, Inventory, Product
from inventory.permissions.inventory import IsProductOwner
from inventory.serializers.inventory import (
    CategorySerializer,
    InventorySerializer,
    InventoryStatisticsSerializer,
    ProductResponseSerializer,
    ProductSerializer,
)


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = InventorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CategorySerializer
    search_fields = ["name"]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsProductOwner]
    serializer_class = ProductSerializer
    filterset_class = ProductsFilter
    search_fields = ["name"]

    def get_queryset(self):
        return self.filter_queryset(
            self.queryset.filter(inventory__owner=self.request.user)
        )

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ProductResponseSerializer
        return super().get_serializer_class()

    def create(self, request: Request, *args: Any, **kwargs: dict[str, Any]):
        serializer = self.serializer_class(data=request.data)
        _ = serializer.is_valid(raise_exception=True)

        inventory = Inventory.objects.filter(owner=request.user).first()
        if not inventory:
            inventory = Inventory.objects.create(owner=request.user)

        print({"Inventory": inventory})
        product = serializer.save(inventory=inventory)

        serializer = self.serializer_class(product)
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: InventoryStatisticsSerializer},
    )
    @action(methods=["GET"], detail=False, url_name="statistics", url_path="statistics")
    def statistics(self, request: Request):
        inventory, _ = Inventory.objects.get_or_create(owner=request.user)

        return Response(
            {"data": InventoryStatisticsSerializer(inventory).data},
            status=status.HTTP_201_CREATED,
        )
