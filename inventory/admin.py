from django.contrib import admin

from inventory.models.inventory import Category, Inventory, Product

admin.site.register(Inventory)
admin.site.register(Category)
admin.site.register(Product)
