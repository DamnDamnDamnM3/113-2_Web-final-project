from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class ProductOption(models.Model):
    """商品選項類型，例如：尺寸、顏色等"""
    name = models.CharField(max_length=50)  # 例如：尺寸、顏色
    product = models.ForeignKey(Product, related_name='options', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} - {self.name}"


class ProductOptionValue(models.Model):
    """商品選項的值，例如：S、M、L 或 紅色、藍色等"""
    option = models.ForeignKey(ProductOption, related_name='values', on_delete=models.CASCADE)
    value = models.CharField(max_length=50)  # 例如：S、M、L 或 紅色、藍色

    def __str__(self):
        return f"{self.option.name}: {self.value}"


class ProductVariant(models.Model):
    """商品變體，包含特定選項組合的價格和庫存"""
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    sku = models.CharField(max_length=50, unique=True)  # 商品編號
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)  # 如果為空則使用商品基本價格
    stock = models.PositiveIntegerField(default=0)  # 庫存數量
    option_values = models.ManyToManyField(ProductOptionValue, related_name='variants')

    def __str__(self):
        return f"{self.product.name} - {self.sku}"


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/")
    is_primary = models.BooleanField(default=False)
    variant = models.ForeignKey(ProductVariant, related_name='images', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.product.name} - Image {self.id}"


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        variant_str = f" - {self.variant}" if self.variant else ""
        return f"{self.user.username} - {self.product.name}{variant_str} ({self.quantity})"

    @property
    def total_price(self):
        return self.price * self.quantity


class PurchaseRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    items = models.ManyToManyField(Product, through="PurchaseItem")

    def __str__(self):
        return f"{self.user.username} - {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(PurchaseRecord, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)  # 單價

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"


class PlayerCard(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    image = models.ImageField(upload_to="player_cards/")
    description = models.TextField(max_length=1000)
    number = models.CharField(max_length=3, default="0")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.position})"
