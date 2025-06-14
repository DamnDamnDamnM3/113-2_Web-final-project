from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
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
    ProductVariant,
)
from django.urls import reverse
import json
import subprocess

# Create your views here.

# GitHub Webhook 處理函數 - 用於自動部署
# GitHub Webhook Handler Function - For automatic deployment
@csrf_exempt
def github_webhook(request):
    if request.method == "POST":
        payload = json.loads(request.body.decode("utf-8"))
        ref = payload.get("ref", "")
        if ref == "refs/heads/Python":  # 只處理 Python 分支
            try:
                result = subprocess.run(
                    ["git", "-C", "/var/www/113-2_Web-final-project", "pull", "origin", "Python"],
                    capture_output=True,
                    text=True,
                    check=True
                )
                return HttpResponse(f"Pulled successfully:\n{result.stdout}", status=200)
            except subprocess.CalledProcessError as e:
                return HttpResponse(f"Git pull failed:\n{e.stderr}", status=500)
        else:
            return HttpResponse("Not Python branch. Ignored.", status=200)
    return HttpResponse("Only POST method allowed.", status=405)

# 用戶註冊視圖 - 處理新用戶註冊
# User Registration View - Handle new user registration
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # 驗證密碼一致性
        # Validate password consistency
        if password1 != password2:
            messages.error(request, "密碼不一致")
            return redirect("shop:register")

        # 檢查用戶名是否已存在
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "用戶名已存在")
            return redirect("shop:register")

        # 檢查電子郵件是否已存在
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "電子郵件已存在")
            return redirect("shop:register")

        # 創建新用戶並自動登入
        # Create new user and auto login
        user = User.objects.create_user(
            username=username, email=email, password=password1
        )
        login(request, user)
        messages.success(request, "註冊成功！")
        return redirect("shop:home")

    return render(request, "registration/register.html")

# 用戶登入視圖 - 處理用戶登入
# User Login View - Handle user login
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
    return render(request, "registration/login.html", {"next": next_url})

# 用戶登出視圖 - 處理用戶登出
# User Logout View - Handle user logout
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "已登出")
    return redirect("shop:home")

# 商品列表視圖 - 顯示所有商品
# Product List View - Display all products
def product_list(request):
    products = Product.objects.all()
    return render(request, "shop/product_list.html", {"products": products})

# 將球員卡加入購物車 - 處理球員卡購買
# Add Player Card to Cart - Handle player card purchase
@login_required
def add_card_to_cart(request, card_id):
    card = get_object_or_404(PlayerCard, id=card_id)
    quantity = int(request.POST.get("quantity", 1))

    # 檢查是否已經在購物車中，如果是則增加數量
    # Check if already in cart, if yes then increase quantity
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user, product=card, defaults={"quantity": quantity}
    )

    if not created:
        cart_item.quantity += quantity
        cart_item.save()

    messages.success(request, f"{card.name} added to cart!")
    return redirect("shop:player_cards")

# 將商品加入購物車 - 處理商品購買
# Add Product to Cart - Handle product purchase
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get("quantity", 1))

    # 處理商品變體（如尺寸、顏色等）
    # Handle product variants (e.g., size, color)
    variant_id = request.POST.get("variant_id")
    if variant_id:
        variant = get_object_or_404(ProductVariant, id=variant_id)
        price = variant.price or product.price
    else:
        variant = None
        price = product.price

    # 創建或更新購物車項目
    # Create or update cart item
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        variant=variant,
        defaults={"quantity": quantity, "price": price}
    )

    if not created:
        cart_item.quantity += quantity
        cart_item.save()
    
    print(f"CartItem created: {created}, user: {request.user}, product: {product}, variant: {variant}, quantity: {cart_item.quantity}")

    messages.success(request, f"已將 {product.name} 加入購物車！")
    return redirect("shop:cart")

# 更新購物車 - 修改商品數量
# Update Cart - Modify product quantity
@login_required
def update_cart(request, product_id):
    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 1))
        variant_id = request.POST.get("variant_id")

        # 構建查詢過濾條件
        # Build query filters
        filters = {
            "user": request.user,
            "product_id": product_id,
        }

        if variant_id:
            filters["variant_id"] = variant_id
        else:
            filters["variant__isnull"] = True

        cart_item = get_object_or_404(CartItem, **filters)
        cart_item.quantity = quantity
        cart_item.save()
        messages.success(request, "購物車已更新")
    return redirect("shop:cart")

# 清空購物車 - 移除所有商品
# Clear Cart - Remove all items
@login_required
def clear_cart(request):
    CartItem.objects.filter(user=request.user).delete()
    messages.success(request, "購物車已清空")
    return redirect("shop:cart")

# 從購物車移除球員卡
# Remove Player Card from Cart
@login_required
def remove_card_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    messages.success(request, "Item removed from cart!")
    return redirect("shop:cart")

# 從購物車移除商品
# Remove Product from Cart
@login_required
def remove_product_from_cart(request, product_id):
    CartItem.objects.filter(user=request.user, product_id=product_id).delete()
    messages.success(request, "商品已從購物車移除")
    return redirect("shop:cart")

# 結帳處理 - 完成訂單並發送確認郵件
# Checkout Process - Complete order and send confirmation email
@login_required
def checkout(request):
    if request.method == "POST":
        cart_items = CartItem.objects.filter(user=request.user)
        if not cart_items.exists():
            return redirect("cart")

        # 創建購買記錄
        # Create purchase record
        purchase_record = PurchaseRecord.objects.create(
            user=request.user,
            total_price=sum(item.product.price * item.quantity for item in cart_items),
        )

        # 添加購買項目
        # Add purchase items
        for item in cart_items:
            PurchaseItem.objects.create(
                purchase=purchase_record,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
            )

        # 發送確認郵件
        # Send confirmation email
        try:
            subject = "訂單確認通知"
            message = f"""
            親愛的 {request.user.username}：

            感謝您的購買！您的訂單已經成功建立。

            訂單編號：{purchase_record.id}
            訂單時間：{purchase_record.created_at}
            總金額：${int(purchase_record.total_price)}

            訂購商品：
            {chr(10).join([f'- {item.product.name} x {item.quantity} (${int(item.price)})' for item in purchase_record.purchaseitem_set.all()])}

            如有任何問題，請隨時與我們聯繫。

            祝您購物愉快！
            """
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [request.user.email, "admin@mail.jw-albert.tw"]

            print(f"Attempting to send email to {recipient_list}")  # 調試信息
            send_mail(subject, message, from_email, recipient_list)
            print("Email sent successfully")  # 調試信息
        except Exception as e:
            print(f"Failed to send email: {str(e)}")  # 調試信息
            # 即使郵件發送失敗，我們仍然繼續處理訂單

        # 清空購物車
        # Clear cart
        cart_items.delete()

        return redirect("shop:profile")
    return redirect("shop:cart")

# 商品詳情視圖 - 顯示單個商品的詳細資訊
# Product Detail View - Display detailed information of a single product
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    variants = product.variants.all()

    # 檢查商品是否有圖片和選項
    # Check if product has images and options
    has_images = product.images.exists()
    image_count = product.images.count()
    has_options = product.options.exists()

    return render(request, "shop/product_detail.html", {
        "product": product,
        "variants": variants,
        "has_images": has_images,
        "image_count": image_count,
        "has_options": has_options
    })

# 首頁視圖 - 顯示網站首頁
# Home Page View - Display website homepage
def home(request):
    return render(request, "main/home.html")

# 球員卡列表視圖 - 顯示所有球員卡
# Player Cards List View - Display all player cards
def player_cards(request):
    cards = PlayerCard.objects.all()
    return render(request, "main/player_cards.html", {"cards": cards})

# 球隊頁面視圖 - 顯示球隊資訊
# Team Page View - Display team information
def team(request):
    return render(request, "main/team.html")

# 購物車視圖 - 顯示用戶的購物車內容
# Cart View - Display user's cart contents
@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user).select_related('variant', 'product')
    total = sum((item.price or item.product.price) * item.quantity for item in cart_items)
    return render(request, "shop/cart.html", {"cart_items": cart_items, "total": total})

# 用戶資料視圖 - 顯示用戶資料和購買記錄
# User Profile View - Display user profile and purchase records
@login_required
def profile(request):
    purchase_records = PurchaseRecord.objects.filter(user=request.user).order_by(
        "-created_at"
    )
    return render(request, "shop/profile.html", {"purchase_records": purchase_records})

# 更新用戶資料視圖 - 處理用戶資料更新
# Update User Profile View - Handle user profile updates
@login_required
def update_profile(request):
    if request.method == "POST":
        email = request.POST.get("email")
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        user = request.user
        # 驗證目前密碼
        # Validate current password
        if not user.check_password(current_password):
            messages.error(request, "目前密碼錯誤")
            return redirect("shop:profile")

        # 檢查新電子郵件是否已存在
        # Check if new email already exists
        if email != user.email and User.objects.filter(email=email).exists():
            messages.error(request, "電子郵件已存在")
            return redirect("shop:profile")

        # 更新用戶資料
        # Update user profile
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
