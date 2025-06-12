from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("update_profile/", views.update_profile, name="update_profile"),
    path("product_list/", views.product_list, name="product_list"),
    path(
        "product_detail/<int:product_id>/", views.product_detail, name="product_detail"
    ),
    path("cart/", views.cart, name="cart"),
    path("clear_cart/", views.clear_cart, name="clear_cart"),
    # path(
    #     "add_product_to_cart/<int:product_id>/",
    #     views.add_product_to_cart,
    #     name="add_product_to_cart",
    # ),
    path("update_cart/<int:product_id>/", views.update_cart, name="update_cart"),
    path(
        "remove_product_from_cart/<int:product_id>/",
        views.remove_product_from_cart,
        name="remove_product_from_cart",
    ),
    path("checkout/", views.checkout, name="checkout"),
    path("player_cards/", views.player_cards, name="player_cards"),
    path(
        "add-card-to-cart/<int:card_id>/",
        views.add_card_to_cart,
        name="add_card_to_cart",
    ),
    path(
        "remove-card-from-cart/<int:item_id>/",
        views.remove_card_from_cart,
        name="remove_card_from_cart",
    ),
    path("history/", views.history, name="history"),
    path("team/", views.team, name='team'),
]
