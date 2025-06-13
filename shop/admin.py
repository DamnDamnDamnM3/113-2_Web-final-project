from django.contrib import admin
from .models import (
    Product,
    CartItem,
    PurchaseRecord,
    PurchaseItem,
    PlayerCard,
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name",)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "quantity")
    list_filter = ("user",)


@admin.register(PurchaseRecord)
class PurchaseRecordAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at", "total_price")
    list_filter = ("user", "created_at")


@admin.register(PurchaseItem)
class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ("purchase", "product", "quantity", "price")
    list_filter = ("purchase",)


@admin.register(PlayerCard)
class PlayerCardAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "number")
    list_filter = ("position",)
    search_fields = ("name", "description")
