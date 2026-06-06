# E-Commerce Platform

A fully functional, responsive, and robust E-Commerce web application built with a modern tech stack: **Django (Django REST Framework)** for the backend and **React + Redux Toolkit** for the frontend.

## 🚀 Core Features

### User & Authentication
* **User Registration & Login:** Secure authentication using JSON Web Tokens (JWT).
* **User Profile:** Users can update their profile information and view order history.
* **Admin Role:** Special privileges for admin users to manage products, users, and orders.

### Product & Catalog
* **Product Listing:** View all available products with pagination.
* **Product Details:** Detailed view for each product including images, price, stock status, description, and reviews.
* **Search & Filter:** Search products by keywords.
* **Reviews & Ratings:** Logged-in users can leave reviews and rate products.
* **Inventory Management:** Tracks `countInStock` and prevents ordering out-of-stock items.

### Shopping & Checkout
* **Shopping Cart:** Add/remove items, adjust quantities. Cart state is managed seamlessly by Redux.
* **Checkout Process:** Step-by-step wizard for shipping address, payment method selection, and order summary.
* **Payment Integration:** Live PayPal integration for processing payments securely.
* **Order Tracking:** Users can track the status of their orders (Paid, Delivered).

### Admin Dashboard
* **Product Management:** Create, Edit, and Delete products.
* **User Management:** View all users, edit user roles, or delete users.
* **Order Management:** View all orders in the system, mark them as delivered, and track payment status.

---

## 🛠️ Tech Stack

### Frontend
* **React** (v19) - UI Library
* **Redux Toolkit** - Global State Management
* **React Router DOM** - Application Routing
* **React Bootstrap** - UI Components & Responsive Styling
* **Axios** - HTTP client for API requests
* **PayPal React JS** - Payment gateway integration

### Backend
* **Django** (v5.2) - High-level Python Web Framework
* **Django REST Framework (DRF)** - Building RESTful Web APIs
* **Simple JWT** - JSON Web Token authentication for DRF
* **PostgreSQL / SQLite** - Relational Database Management System
* **CORS Headers** - Handling Cross-Origin Resource Sharing

---

## 📁 Project Structure

```text
ecommerce/
├── backend/                  # Django REST Framework backend
│   ├── backend/              # Core Django settings and configurations
│   ├── base/                 # Main Django app (Models, Views, URLs, Serializers)
│   ├── static/               # Static files & user-uploaded media (product images)
│   ├── manage.py             # Django entry point
│   └── frontend/             # React Frontend application
│       ├── src/              # React source code (Components, Screens, Redux Slices)
│       ├── public/           # Public assets
│       └── package.json      # Frontend dependencies
└── myenv/                    # Python Virtual Environment
```

---

## 💻 Installation & Setup

Follow these instructions to get the project up and running on your local machine.

### Prerequisites
* Python (3.8+)
* Node.js & npm (v16+)
* PostgreSQL (Optional, if you want to use the configured DB instead of SQLite)

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd ecommerce
```

### 2. Backend Setup
Activate your virtual environment and install dependencies.
```bash
# Activate virtual environment
# Windows:
myenv\Scripts\activate
# macOS/Linux:
source myenv/bin/activate

cd backend

# Install Python dependencies
pip install -r requirements.txt
# (If requirements.txt is missing, install manually: pip install django djangorestframework djangorestframework-simplejwt django-cors-headers psycopg2)

# Set up the database (Make sure your PostgreSQL server is running if using Postgres)
python manage.py makemigrations
python manage.py migrate

# Create a superuser (Admin)
python manage.py createsuperuser

# Start the Django development server
python manage.py runserver
```

### 3. Frontend Setup
Open a new terminal window/tab.
```bash
cd backend/frontend

# Install Node.js dependencies
npm install

# Start the React development server
npm start
```
The React app will typically run on `http://localhost:3000` and the Django backend on `http://localhost:8000`.

---

## 📸 Screenshots
*(Images will be added here later)*

---

## ⚙️ Environment Variables

To fully utilize all features, you may need to configure certain environment variables (e.g., in a `.env` file for both frontend and backend).

**Backend (Django):**
* `SECRET_KEY`: Django secret key
* `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`: Database credentials
* `DEBUG`: Set to `True` for development, `False` for production

**Frontend (React):**
* `REACT_APP_PAYPAL_CLIENT_ID`: Your PayPal developer client ID for processing transactions.

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📝 License
This project is open source and available under the [MIT License](LICENSE).

## Screenshots

Home
![Home](_images/solarshop_01.png)

Product Detail
![Product Detail](_images/solarshop_02.png)

Cart
![Cart](_images/solarshop_03.png)

Product Management
![Product Management](_images/solarshop_04.png)
