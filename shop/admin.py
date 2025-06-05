from django.contrib import admin
from .models import (
    Product,
    CartItem,
    PurchaseRecord,
    PurchaseItem,
    PlayerCard,
    CardCategory,
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


@admin.register(CardCategory)
class CardCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(PlayerCard)
class PlayerCardAdmin(admin.ModelAdmin):
    list_display = ("name", "team", "position", "price", "rarity", "year", "is_active")
    list_filter = ("team", "position", "rarity", "year", "is_active")
    search_fields = ("name", "team", "description")
    list_editable = ("price", "is_active")
