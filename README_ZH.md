# Suntory Sunbirds 網路商店

一個基於 Django 的電子商務平台，用於販售排球選手卡和相關商品。

## 功能特色

- 使用者認證和授權
- 產品目錄（支援變體和選項）
- 購物車功能
- 購買歷史記錄追蹤
- 選手卡收藏管理
- 響應式設計

## 資料庫結構

### 核心模型

1. **產品 (Product)**
   - 基本產品資訊（名稱、價格、描述）
   - 支援多種變體和選項

2. **產品選項 (ProductOption) 和產品選項值 (ProductOptionValue)**
   - 管理產品變體（例如：尺寸、顏色）
   - 靈活的選項-值系統

3. **產品變體 (ProductVariant)**
   - 特定產品變體，包含 SKU
   - 個別定價和庫存管理

4. **產品圖片 (ProductImage)**
   - 每個產品可有多張圖片
   - 支援變體特定圖片

5. **選手卡 (PlayerCard)**
   - 排球選手資訊
   - 包含選手統計數據、隊伍、位置

6. **購物車項目 (CartItem)**
   - 購物車管理
   - 支援產品變體

7. **購買記錄 (PurchaseRecord) 和購買項目 (PurchaseItem)**
   - 訂單歷史
   - 詳細購買資訊

## 使用者互動

1. **認證**
   - 使用者註冊
   - 登入/登出
   - 密碼管理

2. **購物體驗**
   - 瀏覽產品
   - 查看產品詳情
   - 將商品加入購物車
   - 結帳流程

3. **使用者儀表板**
   - 查看購買歷史
   - 管理個人資料
   - 追蹤訂單

## 技術堆疊

- Django 5.2
- SQLite 資料庫
- Bootstrap 前端框架
- Python 3.x

## 安裝說明

1. 複製專案儲存庫
2. 建立虛擬環境：
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows 系統：venv\Scripts\activate
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

## 開發

專案遵循 Django 的標準專案結構：
- `shop/` - 主要應用程式目錄
- `templates/` - HTML 模板
- `static/` - 靜態檔案（CSS、JS、圖片）
- `media/` - 使用者上傳的檔案

## 開發團隊

本專案由 DamnM3 團隊開發：
- Albert
- Andy
- Lacne

## 授權

本專案採用 MIT 授權條款。詳見 [LICENSE](LICENSE) 檔案。

MIT 授權條款允許您：
- 自由使用、修改、分發本專案
- 用於商業用途
- 修改原始碼
- 分發修改後的版本

唯一的條件是必須保留原始的授權聲明。 