# 🧾 Mini Inventory Management System

A Django RESTful API for managing product inventories, built as part of a technical assessment. Each user has their own isolated inventory, with full CRUD functionality for products and categories, advanced filtering, and a basic statistics endpoint.

View (https://dbdiagram.io/d/CIE-asssment-678baabd6b7fa355c349d4a8)[ERD]

## ✅ Features

- JWT-based User Authentication (Register & Login)
- Multi-tenant setup: each user manages their own inventory
- Inventory, Product & Category models with relationships
- CRUD operations:
  - Products
  - Categories
- Filtering:
  - By category
  - By quantity (`gt`, `lt`, `exact`, etc.)
  - By price range (`min`, `max`)
- Inventory Statistics:
  - Total number of products
  - Total quantity in stock
  - Total value of products in stock
  - Average product price
- API documentation via Swagger/OpenAPI and Redoc

## 🔧 Tech Stack

- Python 3.10+
- Django 5.x
- Django REST Framework
- Django Filter
- drf-yasg (Swagger docs)
- Docker / Podman (optional)

## 🚀 Getting Started


### With Docker / Podman

#### 1. Clone the Repository

```bash
git clone https://github.com/McEazy2700/CIE-assessment.git
cd CIE-assessment
```

#### 2. Setup environement variables

```bash
mv .env.example .env
```
#### 3. Build docker container

```bash
# docker
docker compose up --build

# podman
podman compose up --build
```

### With Python Virtual Environments

#### 1. Clone the Repository

```bash
git clone https://github.com/McEazy2700/CIE-assessment.git
cd CIE-assessment
```

#### 2. Setup environement variables

```bash
mv .env.example .env
```

#### 3. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 4. Install dependencies
```bash
pip install -r requirements.txt
```

#### 5. Run migrations
```bash
python manage.py migrate
```

#### 6. Run the Server
```bash
python manage.py runserver
```

### Access the API
- Swagger Docs: http://localhost:8080/api/docs/
- Admin Panel: http://localhost:8080/admin/

### API Endpoints
Method | Endpoint | Description
POST | /users/auth/register/ | User Registration
POST | /users/auth/login/ | User Login
GET | /api/products/ | List all user products
POST | /api/products/ | Create a new product
GET | /api/products/statistics/ | Inventory statistics
GET | /api/products/?category=<id> | Filter products by category
GET | /api/products/?price_min=10&price_max=100 | Filter by price range
GET | /api/products/?quantity_gt=10 | Filter by quantity
GET | /api/categories/ | List all categories
POST | /api/categories/ | Create a category
