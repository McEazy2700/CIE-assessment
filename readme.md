# 🧾 Mini Inventory Management System

A Django RESTful API for managing product inventories, built as part of a technical assessment. Each user has their own isolated inventory, with full CRUD functionality for products and categories, advanced filtering, and a basic statistics endpoint.

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
