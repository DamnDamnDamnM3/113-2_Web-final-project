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
    News
)

# 產品選項值內嵌管理介面
# Product Option Value Inline Admin Interface
class ProductOptionValueInline(admin.TabularInline):
    model = ProductOptionValue
    extra = 1  # 預設顯示一個空白的選項值欄位


# 產品選項內嵌管理介面
# Product Option Inline Admin Interface
class ProductOptionInline(admin.TabularInline):
    model = ProductOption
    extra = 1  # 預設顯示一個空白的選項欄位


# 產品變體內嵌管理介面
# Product Variant Inline Admin Interface
class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1
    show_change_link = True  # 顯示變更連結


# 產品圖片內嵌管理介面
# Product Image Inline Admin Interface
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # 預設顯示一個空白的圖片欄位


# 產品管理介面
# Product Admin Interface
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")  # 列表顯示欄位
    search_fields = ("name",)  # 搜尋欄位
    inlines = [ProductOptionInline, ProductVariantInline, ProductImageInline]  # 內嵌管理介面


# 產品選項管理介面
# Product Option Admin Interface
@admin.register(ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    list_display = ("name", "product")  # 列表顯示欄位
    list_filter = ("product",)  # 過濾選項
    inlines = [ProductOptionValueInline]  # 內嵌管理介面


# 產品變體管理介面
# Product Variant Admin Interface
@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ("product", "sku", "price", "stock")  # 列表顯示欄位
    list_filter = ("product",)  # 過濾選項
    search_fields = ("sku",)  # 搜尋欄位
    filter_horizontal = ("option_values",)  # 水平過濾器


# 購物車項目管理介面
# Cart Item Admin Interface
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "quantity")  # 列表顯示欄位
    list_filter = ("user",)  # 過濾選項


# 購買記錄管理介面
# Purchase Record Admin Interface
@admin.register(PurchaseRecord)
class PurchaseRecordAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at", "total_price")  # 列表顯示欄位
    list_filter = ("user", "created_at")  # 過濾選項


# 購買項目管理介面
# Purchase Item Admin Interface
@admin.register(PurchaseItem)
class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ("purchase", "product", "quantity", "price")  # 列表顯示欄位
    list_filter = ("purchase",)  # 過濾選項


# 球員卡管理介面
# Player Card Admin Interface
@admin.register(PlayerCard)
class PlayerCardAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "number")  # 列表顯示欄位
    list_filter = ("position",)  # 過濾選項
    search_fields = ("name", "description")  # 搜尋欄位


# 新消息管理頁面
# News admin interface
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date',) # 列表顯示
    list_filter = ('date',) # 依據日期欄位過濾
    search_fields = ('title', 'content') # 後台搜尋