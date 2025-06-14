from django.db import models
from django.contrib.auth.models import User


# 商品基本資訊模型
# Product Basic Information Model
class Product(models.Model):
    name = models.CharField(max_length=100)  # 商品名稱
    price = models.DecimalField(max_digits=8, decimal_places=2)  # 商品基本價格
    description = models.TextField(max_length=1000)  # 商品描述

    def __str__(self):
        return self.name


# 商品選項類型模型
# Product Option Type Model
class ProductOption(models.Model):
    name = models.CharField(max_length=50)  # 例如：尺寸、顏色
    product = models.ForeignKey(Product, related_name='options', on_delete=models.CASCADE)  # 關聯到商品

    def __str__(self):
        return f"{self.product.name} - {self.name}"


# 商品選項值模型
# Product Option Value Model
class ProductOptionValue(models.Model):
    option = models.ForeignKey(ProductOption, related_name='values', on_delete=models.CASCADE)  # 關聯到選項類型
    value = models.CharField(max_length=50)  # 例如：S、M、L 或 紅色、藍色

    def __str__(self):
        return f"{self.option.name}: {self.value}"


# 商品變體模型
# Product Variant Model
class ProductVariant(models.Model):
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)  # 關聯到商品
    sku = models.CharField(max_length=50, unique=True)  # 商品編號
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)  # 如果為空則使用商品基本價格
    stock = models.PositiveIntegerField(default=0)  # 庫存數量
    option_values = models.ManyToManyField(ProductOptionValue, related_name='variants')  # 關聯到選項值

    def __str__(self):
        return f"{self.product.name} - {self.sku}"


# 商品圖片模型
# Product Image Model
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)  # 關聯到商品
    image = models.ImageField(upload_to="products/")  # 商品圖片
    is_primary = models.BooleanField(default=False)  # 是否為主要圖片
    variant = models.ForeignKey(ProductVariant, related_name='images', null=True, blank=True, on_delete=models.SET_NULL)  # 關聯到商品變體

    def __str__(self):
        return f"{self.product.name} - Image {self.id}"


# 購物車項目模型
# Cart Item Model
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 關聯到使用者
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # 關聯到商品
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True, blank=True)  # 關聯到商品變體
    quantity = models.PositiveIntegerField(default=1)  # 購買數量
    price = models.DecimalField(max_digits=8, decimal_places=2)  # 單價

    def __str__(self):
        variant_str = f" - {self.variant}" if self.variant else ""
        return f"{self.user.username} - {self.product.name}{variant_str} ({self.quantity})"

    @property
    def total_price(self):
        return self.price * self.quantity  # 計算總價


# 購買記錄模型
# Purchase Record Model
class PurchaseRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 關聯到使用者
    created_at = models.DateTimeField(auto_now_add=True)  # 建立時間
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # 總金額
    items = models.ManyToManyField(Product, through="PurchaseItem")  # 關聯到商品（透過 PurchaseItem）

    def __str__(self):
        return f"{self.user.username} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"


# 購買項目模型
# Purchase Item Model
class PurchaseItem(models.Model):
    purchase = models.ForeignKey(PurchaseRecord, on_delete=models.CASCADE)  # 關聯到購買記錄
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # 關聯到商品
    quantity = models.PositiveIntegerField()  # 購買數量
    price = models.DecimalField(max_digits=8, decimal_places=2)  # 單價

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"


# 球員卡模型
# Player Card Model
class PlayerCard(models.Model):
    name = models.CharField(max_length=100)  # 球員姓名
    position = models.CharField(max_length=50)  # 球員位置
    image = models.ImageField(upload_to="player_cards/")  # 球員照片
    description = models.TextField(max_length=1000)  # 球員描述
    number = models.CharField(max_length=3, default="0")  # 球員背號
    created_at = models.DateTimeField(auto_now_add=True)  # 建立時間
    updated_at = models.DateTimeField(auto_now=True)  # 更新時間

    def __str__(self):
        return f"{self.name} ({self.position})"
