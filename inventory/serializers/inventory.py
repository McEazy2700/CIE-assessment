from django.contrib.auth import get_user_model
from django.db import models
from rest_framework import serializers

from inventory.models.inventory import Category, Inventory, Product

User = get_user_model()


class InventoryOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email"]


class InventoryStatisticsSerializer(serializers.ModelSerializer):
    total_products = serializers.SerializerMethodField()
    total_quantity = serializers.SerializerMethodField()
    average_price = serializers.SerializerMethodField()
    total_value = serializers.SerializerMethodField()

    class Meta:
        model = Inventory
        fields = ["total_products", "total_quantity", "average_price", "total_value"]

    def get_total_products(self, obj: Inventory) -> int:
        return Product.objects.filter(inventory=obj).count()

    def get_total_quantity(self, obj: Inventory) -> int:
        return (
            Product.objects.filter(inventory=obj).aggregate(
                total=models.Sum("quantity")
            )["total"]
            or 0
        )

    def get_average_price(self, obj: Inventory) -> int:
        return (
            Product.objects.filter(inventory=obj).aggregate(
                average_price=models.Avg("price")
            )["average_price"]
            or 0
        )

    def get_total_value(self, obj: Inventory):
        return (
            Product.objects.filter(inventory=obj).aggregate(
                total=models.Sum(models.F("price") * models.F("quantity"))
            )["total"]
            or 0
        )


class InventorySerializer(serializers.ModelSerializer):
    owner = InventoryOwnerSerializer()

    class Meta:
        model = Inventory
        fields = "__all__"
        read_only_fields = ["id", "date_added", "last_updated"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ["slug", "created_at", "last_updated", "id"]


class MinimalCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "slug", "name"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["id", "slug", "created_at", "last_updated", "inventory"]


class ProductResponseSerializer(ProductSerializer):
    inventory = InventorySerializer()
    categories = MinimalCategorySerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["id", "slug", "created_at", "last_updated"]
