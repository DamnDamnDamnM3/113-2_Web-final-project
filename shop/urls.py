from django.urls import path
from . import views
from .views import github_webhook

# 設定應用程式名稱
# Set application name
app_name = "shop"

# URL 路由配置
# URL Routing Configuration
urlpatterns = [
    # GitHub Webhook 路由
    # GitHub Webhook Route
    path('webhook/', github_webhook, name='github_webhook'),
    
    # 首頁路由
    # Home Page Route
    path("", views.home, name="home"),
    
    # 用戶認證相關路由
    # User Authentication Routes
    path("register/", views.register, name="register"),  # 註冊
    path("login/", views.login_view, name="login"),      # 登入
    path("logout/", views.logout_view, name="logout"),   # 登出
    
    # 用戶資料相關路由
    # User Profile Routes
    path("profile/", views.profile, name="profile"),                     # 個人資料
    path("update_profile/", views.update_profile, name="update_profile"), # 更新個人資料
    
    # 商品相關路由
    # Product Routes
    path("product_list/", views.product_list, name="product_list"),     # 商品列表
    path(
        "product_detail/<int:product_id>/", views.product_detail, name="product_detail"  # 商品詳情
    ),
    
    # 購物車相關路由
    # Shopping Cart Routes
    path("cart/", views.cart, name="cart"),                             # 購物車
    path("clear_cart/", views.clear_cart, name="clear_cart"),           # 清空購物車
    path(
        "add_to_cart/<int:product_id>/", views.add_to_cart, name="add_to_cart",  # 加入購物車
    ),
    path("update_cart/<int:product_id>/", views.update_cart, name="update_cart"), # 更新購物車
    path(
        "remove_product_from_cart/<int:product_id>/", views.remove_product_from_cart, name="remove_product_from_cart",  # 從購物車移除商品
    ),
    
    # 結帳路由
    # Checkout Route
    path("checkout/", views.checkout, name="checkout"),
    
    # 球員卡相關路由
    # Player Card Routes
    path("player_cards/", views.player_cards, name="player_cards"),     # 球員卡列表
    path(
        "add-card-to-cart/<int:card_id>/", views.add_card_to_cart, name="add_card_to_cart",  # 加入球員卡到購物車
    ),
    path(
        "remove-card-from-cart/<int:item_id>/", views.remove_card_from_cart, name="remove_card_from_cart",  # 從購物車移除球員卡
    ),
    
    # 球隊相關路由
    # Team Route
    path("team/", views.team, name="team"),                             # 球隊頁面
]
