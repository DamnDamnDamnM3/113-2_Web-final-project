from django.apps import AppConfig


# 商店應用程式配置類別
# Shop Application Configuration Class
class ShopConfig(AppConfig):
    # 設定預設主鍵欄位類型為 BigAutoField
    # Set default primary key field type to BigAutoField
    default_auto_field = 'django.db.models.BigAutoField'
    
    # 設定應用程式名稱為 'shop'
    # Set application name to 'shop'
    name = 'shop'
