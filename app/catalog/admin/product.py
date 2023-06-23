from django.contrib import admin

from ..models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "name",
        "price",
        "category__name",
    ]
    list_filter = [
        "category__name",
    ]
    search_fields = [
        "name",
        "description",
    ]
