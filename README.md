# Django CRUD Shop Management System

A Django-based web application for managing shop inventory with CRUD operations and M-Pesa payment integration.

## Features

- **Product Management**: Full CRUD operations for products (Create, Read, Update, Delete)
- **Admin Dashboard**: View all products in a centralized dashboard
- **Product Details**: Name, price, description, brand, category, and quantity tracking
- **M-Pesa Integration**: Secure payment processing using M-Pesa STK Push
- **Responsive Templates**: Clean HTML templates for all operations

## Technologies Used

- **Backend**: Django 5.2.4
- **Database**: SQLite3 (default)
- **Payment Gateway**: M-Pesa via django-daraja
- **Frontend**: HTML, CSS
- **Environment Management**: python-dotenv

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd DjangoCRUD
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the project root and add the following:
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1

   # M-Pesa Configuration
   MPESA_ENVIRONMENT=sandbox  # or production
   MPESA_CONSUMER_KEY=your-consumer-key
   MPESA_CONSUMER_SECRET=your-consumer-secret
   MPESA_EXPRESS_SHORTCODE=your-shortcode
   MPESA_PASSKEY=your-passkey
   INITIATOR_NAME=your-initiator-name
   SECURITY_CREDENTIALS=your-security-credentials
   B2C_SHORTCODE=your-b2c-shortcode
   ```

5. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   Open your browser and go to `http://127.0.0.1:8000`

## Usage

### Admin Dashboard
- Navigate to the home page to view all products
- Add new products using the "Add Item" functionality
- Update existing products by clicking the update link
- Delete products using the delete link

### Adding Products
- Fill in product details: name, price, description, brand, category, quantity
- Click "Add Item" to save the product

### Updating Products
- Click the update link next to any product
- Modify the product details
- Click "Update Item" to save changes

### M-Pesa Payments
- Navigate to the payment form
- Enter phone number and amount
- Click "Pay" to initiate STK Push

## Project Structure

```
DjangoCRUD/
├── Admin/                    # Main app
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates
│   │   ├── admin.html       # Admin dashboard
│   │   ├── add_item.html    # Add product form
│   │   ├── update_item.html # Update product form
│   │   └── payment_form.html # M-Pesa payment form
│   ├── models.py            # Product model
│   ├── views.py             # View functions
│   └── urls.py              # URL patterns
├── Shop/                    # Django project settings
│   ├── settings.py          # Project configuration
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
├── static/                  # Static files
│   └── css/
│       └── main.css         # Custom styles
├── manage.py                # Django management script
├── .env                     # Environment variables (create this)
├── .gitignore               # Git ignore rules
└── README.md                # Project documentation
```

## API Endpoints

- `GET /` - Admin dashboard (list all products)
- `GET/POST /add_item/` - Add new product
- `POST /delete/<id>/` - Delete product by ID
- `GET/POST /update/<id>/` - Update product by ID
- `GET/POST /mpesa_pay/` - Process M-Pesa payment

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

