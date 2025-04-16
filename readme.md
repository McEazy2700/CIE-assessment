# 🧾 Mini Inventory Management System

A Django RESTful API for managing product inventories, built as part of a technical assessment. Each user has their own isolated inventory, with full CRUD functionality for products and categories, advanced filtering, and a basic statistics endpoint.

## ✅ Features

- JWT-based User Authentication (Register & Login)
- Multi-tenant setup: each user manages their own inventory
- Product & Category models with relationships
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
  - Average product price
- API documentation via Swagger/OpenAPI

## 🔧 Tech Stack

- Python 3.10+
- Django 4.x
- Django REST Framework
- JWT Authentication (`djangorestframework-simplejwt`)
- Django Filter
- drf-yasg (Swagger docs)
- Docker & Docker Compose (optional)

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/inventory-api.git
cd inventory-api
