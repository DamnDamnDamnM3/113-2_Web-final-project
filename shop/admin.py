from django.contrib import admin
from .models import (
    Product,
    ProductImage,
    ProductOption,
    ProductOptionValue,
    ProductVariant,
    CartItem,
    PurchaseRecord,
    PurchaseItem,
    PlayerCard,
)


class ProductOptionValueInline(admin.TabularInline):
    model = ProductOptionValue
    extra = 1


class ProductOptionInline(admin.TabularInline):
    model = ProductOption
    extra = 1


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1
    show_change_link = True


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name",)
    inlines = [ProductOptionInline, ProductVariantInline, ProductImageInline]


@admin.register(ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    list_display = ("name", "product")
    list_filter = ("product",)
    inlines = [ProductOptionValueInline]


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ("product", "sku", "price", "stock")
    list_filter = ("product",)
    search_fields = ("sku",)
    filter_horizontal = ("option_values",)


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
