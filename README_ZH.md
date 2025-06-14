# Suntory Sunbirds 網路商店

一個基於 Django 的電子商務平台，專門販售棒球球員卡及相關商品。

## 功能特色

- 使用者認證與授權
- 商品目錄（支援變體和選項）
- 購物車功能
- 購買歷史記錄
- 球員卡收藏管理
- 響應式設計

## 資料庫結構

### 核心模型

1. **商品 (Product)**
   - 基本商品資訊（名稱、價格、描述）
   - 支援多種變體和選項

2. **商品選項與選項值 (ProductOption & ProductOptionValue)**
   - 管理商品變體（例如：尺寸、顏色）
   - 靈活的選項-值系統

3. **商品變體 (ProductVariant)**
   - 特定商品變體，包含 SKU
   - 個別定價和庫存管理

4. **商品圖片 (ProductImage)**
   - 每個商品可有多張圖片
   - 支援變體特定圖片

5. **球員卡 (PlayerCard)**
   - 棒球球員資訊
   - 包含球員統計數據、球隊、位置
   - 卡片稀有度和年份資訊

6. **購物車項目 (CartItem)**
   - 購物車管理
   - 支援商品變體
   - 價格追蹤

7. **購買記錄與購買項目 (PurchaseRecord & PurchaseItem)**
   - 訂單歷史
   - 詳細購買資訊

## 使用者交互

1. **認證系統**
   - 使用者註冊
   - 登入/登出
   - 密碼管理

2. **購物體驗**
   - 瀏覽商品
   - 查看商品詳情
   - 加入購物車
   - 結帳流程

3. **使用者儀表板**
   - 查看購買歷史
   - 管理個人資料
   - 追蹤訂單

## 技術架構

- Django 5.2
- SQLite 資料庫
- Bootstrap 前端框架
- Python 3.x

## 安裝說明

1. 複製專案
2. 建立虛擬環境：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. 安裝依賴套件：
   ```bash
   pip install -r requirements.txt
   ```
4. 執行資料庫遷移：
   ```bash
   python manage.py migrate
   ```
5. 啟動開發伺服器：
   ```bash
   python manage.py runserver
   ```

## 開發說明

專案遵循 Django 標準專案結構：
- `shop/` - 主要應用程式目錄
- `templates/` - HTML 模板
- `static/` - 靜態檔案（CSS、JS、圖片）
- `media/` - 使用者上傳檔案

## 授權說明

本專案為專有且機密。 