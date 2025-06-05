from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="products/")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.quantity})"


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


class CardCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Card Categories"


class PlayerCard(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    image = models.ImageField(upload_to="player_cards/")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=1000)
    category = models.ForeignKey(CardCategory, on_delete=models.CASCADE)
    rarity = models.CharField(max_length=50)
    year = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    number = models.CharField(max_length=3, default="0")
    batting_throws = models.CharField(max_length=3, default="R/R")
    mlb_url = models.URLField(default="https://www.mlb.com/dodgers")

    def __str__(self):
        return f"{self.name} ({self.team})"
