# Suntory Sunbirds Web Shop

A Django-based e-commerce platform for selling volleyball player cards and related merchandise.

## Features

- User authentication and authorization
- Product catalog with variants and options
- Shopping cart functionality
- Purchase history tracking
- Player card collection management
- Responsive design

## Database Structure

### Core Models

1. **Product**
   - Basic product information (name, price, description)
   - Supports multiple variants and options

2. **ProductOption & ProductOptionValue**
   - Manages product variations (e.g., size, color)
   - Flexible option-value system

3. **ProductVariant**
   - Specific product variations with SKU
   - Individual pricing and stock management

4. **ProductImage**
   - Multiple images per product
   - Support for variant-specific images

5. **PlayerCard**
   - Volleyball player information
   - Includes player stats, team, position

6. **CartItem**
   - Shopping cart management
   - Supports product variants

7. **PurchaseRecord & PurchaseItem**
   - Order history
   - Detailed purchase information

## User Interactions

1. **Authentication**
   - User registration
   - Login/Logout
   - Password management

2. **Shopping Experience**
   - Browse products
   - View product details
   - Add items to cart
   - Checkout process

3. **User Dashboard**
   - View purchase history
   - Manage profile
   - Track orders

## Technical Stack

- Django 5.2
- SQLite Database
- Bootstrap for frontend
- Python 3.x

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Development

The project follows Django's standard project structure:
- `shop/` - Main application directory
- `templates/` - HTML templates
- `static/` - Static files (CSS, JS, images)
- `media/` - User-uploaded files

## Team

This project is developed by DamnM3 Team:
- Albert
- Andy
- Lacne

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

The MIT License allows you to:
- Freely use, modify, and distribute this project
- Use it for commercial purposes
- Modify the source code
- Distribute modified versions

The only condition is that you must retain the original license notice.
