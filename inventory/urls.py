from django.urls import include, path
from rest_framework import routers

from inventory.views.inventory import CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r"categories", CategoryViewSet, basename="categories")
router.register(r"products", ProductViewSet, basename="products")

urlpatterns = [path("", include(router.urls))]
