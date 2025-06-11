from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .models import (
    Product,
    CartItem,
    PurchaseRecord,
    PurchaseItem,
    PlayerCard,
)
from django.urls import reverse

# Create your views here.


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "密碼不一致")
            return redirect("shop:register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "用戶名已存在")
            return redirect("shop:register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "電子郵件已存在")
            return redirect("shop:register")

        user = User.objects.create_user(
            username=username, email=email, password=password1
        )
        login(request, user)
        messages.success(request, "註冊成功！")
        return redirect("shop:home")

    return render(request, "shop/register.html")


def login_view(request):
    next_url = request.GET.get("next") or request.POST.get("next")
    if next_url in [None, "", "None"]:
        next_url = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "登入成功！")
            return redirect(next_url) if next_url else redirect(reverse("shop:home"))
        else:
            messages.error(request, "用戶名或密碼錯誤")
    return render(request, "shop/login.html", {"next": next_url})


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "已登出")
    return redirect("shop:home")


def hello(request):
    return render(request, "shop/hello.html")


def product_list(request):
    products = Product.objects.all()
    return render(request, "shop/product_list.html", {"products": products})


@login_required
def add_card_to_cart(request, card_id):
    card = get_object_or_404(PlayerCard, id=card_id)
    quantity = int(request.POST.get("quantity", 1))

    # 檢查是否已經在購物車中
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user, product=card, defaults={"quantity": quantity}
    )

    if not created:
        cart_item.quantity += quantity
        cart_item.save()

    messages.success(request, f"{card.name} added to cart!")
    return redirect("shop:player_cards")


@login_required
def add_product_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get("quantity", 1))

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user, product=product, defaults={"quantity": quantity}
    )

    if not created:
        cart_item.quantity += quantity
        cart_item.save()

    messages.success(request, f"{product.name} 已加入購物車！")
    return redirect("shop:product_list")


@login_required
def update_cart(request, product_id):
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        cart_item = get_object_or_404(
            CartItem, user=request.user, product_id=product_id
        )
        cart_item.quantity = quantity
        cart_item.save()
        messages.success(request, "購物車已更新")
    return redirect("shop:cart")


@login_required
def clear_cart(request):
    CartItem.objects.filter(user=request.user).delete()
    messages.success(request, "購物車已清空")
    return redirect("shop:cart")


@login_required
def remove_card_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    messages.success(request, "Item removed from cart!")
    return redirect("shop:cart")


@login_required
def remove_product_from_cart(request, product_id):
    CartItem.objects.filter(user=request.user, product_id=product_id).delete()
    messages.success(request, "商品已從購物車移除")
    return redirect("shop:cart")


@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items.exists():
        messages.error(request, "購物車是空的！")
        return redirect("shop:cart")

    # 創建購買記錄
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    purchase = PurchaseRecord.objects.create(user=request.user, total_price=total_price)

    # 創建購買項目
    for item in cart_items:
        PurchaseItem.objects.create(
            purchase=purchase,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price,
        )

    # 清空購物車
    cart_items.delete()

    messages.success(request, "購買成功！")
    return redirect("shop:profile")


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "shop/product_detail.html", {"product": product})


@login_required
def history(request):
    records = PurchaseRecord.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "shop/history.html", {"records": records})


def home(request):
    return render(request, "shop/home.html")


def player_cards(request):
    cards = PlayerCard.objects.all()
    return render(request, "shop/player_cards.html", {"cards": cards})


@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, "shop/cart.html", {"cart_items": cart_items, "total": total})


@login_required
def profile(request):
    purchase_records = PurchaseRecord.objects.filter(user=request.user).order_by(
        "-created_at"
    )
    return render(request, "shop/profile.html", {"purchase_records": purchase_records})


@login_required
def update_profile(request):
    if request.method == "POST":
        email = request.POST.get("email")
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        user = request.user
        if not user.check_password(current_password):
            messages.error(request, "目前密碼錯誤")
            return redirect("shop:profile")

        if email != user.email and User.objects.filter(email=email).exists():
            messages.error(request, "電子郵件已存在")
            return redirect("shop:profile")

        user.email = email
        if new_password:
            if new_password != confirm_password:
                messages.error(request, "新密碼不一致")
                return redirect("shop:profile")
            user.set_password(new_password)
        user.save()

        messages.success(request, "個人資料已更新")
        return redirect("shop:profile")

    return redirect("shop:profile")
