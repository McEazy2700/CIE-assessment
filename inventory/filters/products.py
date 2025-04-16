import django_filters

from inventory.models.inventory import Category, Product


class ProductsFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(
        field_name="categories",
        queryset=Category.objects.all(),
        label="Category",
    )
    quantity_gt = django_filters.NumberFilter(
        field_name="quantity", lookup_expr="gt", label="Quantity greater than"
    )
    quantity_lt = django_filters.NumberFilter(
        field_name="quantity", lookup_expr="lt", label="Quantity less than"
    )
    quantity_gte = django_filters.NumberFilter(
        field_name="quantity", lookup_expr="gte", label="Quantity greater than or equal"
    )
    quantity_lte = django_filters.NumberFilter(
        field_name="quantity", lookup_expr="lte", label="Quantity less than or equal"
    )
    quantity_exact = django_filters.NumberFilter(
        field_name="quantity", lookup_expr="exact", label="Quantity equals"
    )
    price_min = django_filters.NumberFilter(
        field_name="price", lookup_expr="gte", label="Minimum price"
    )
    price_max = django_filters.NumberFilter(
        field_name="price", lookup_expr="lte", label="Maximum price"
    )

    class Meta:
        model = Product
        fields = [
            "category",
            "quantity_gt",
            "quantity_lt",
            "quantity_gte",
            "quantity_lte",
            "quantity_exact",
            "price_min",
            "price_max",
            "name",
        ]
