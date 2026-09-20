# Point of Sale (POS-API) Backend API

This project is a high-performance, headless backend REST API designed to serve as the centralized core engine for a modern Point of Sale (POS) system. By decoupling business logic from the user interface, the application provides a secure network of endpoints that manage essential retail operations, including employee profiles (users), inventory tracking (products and categories), and vendor tracking (suppliers). It fully orchestrates the checkout pipeline by registering consumer data (customers), managing multi-item transactions (sales and sale items), processing structural transactions (payments), and logging permanent financial records (receipts).

Built using Python and the FastAPI framework, the system is optimized for high-speed, asynchronous request handling to manage rapid retail transactions without latency. It utilizes Pydantic to enforce strict data validation guards on all incoming request payloads, while SQLAlchemy serves as the Object-Relational Mapper (ORM) to handle abstract database interactions cleanly. To guarantee enterprise-grade reliability and zero system downtime during operational hours, the architecture integrates a comprehensive automated testing suite executed via pytest, which runs automatically inside an automated GitHub Actions Continuous Integration (CI) pipeline whenever new code is updated.

## Features

- User registration and authentication
- Role-based access control
- Product management
- Category management
- Supplier management
- Customer management
- Sales management
- Sale item management
- Payment management
- Receipt management
- Request validation using Pydantic
- Database interaction using SQLAlchemy
- Automated test suite with pytest
- Continuous integration using GitHub Actions

---

## Technology Stack

| Technology | Purpose |
| :--- | :--- |
| Python | Backend programming language |
| FastAPI | REST API framework |
| SQLAlchemy | ORM and database interaction |
| Pydantic | Request and response validation |
| PostgreSQL | Application database |
| SQLite | Database used during automated tests |
| Pytest | Automated testing |
| GitHub Actions | Continuous integration |

---

## Project Structure

```text
pos/
│
├── .github/
│   └── workflows/
│       └── tests.yml
|
├── app/
│   ├── core/
│   │   └── security.py
│   │
│   ├── models/
│   │   ├── category.py
│   │   ├── customer.py
│   │   ├── payment.py
│   │   ├── product.py
│   │   ├── receipt.py
│   │   ├── sale_item.py
│   │   ├── sale.py
│   │   ├── supplier.py
│   │   └── user.py
│   │
│   ├── repositories/
│   │   └── ...
│   │
│   ├── routers/
│   │   └── ...
│   │
│   ├── schemas/
│   │   └── ...
│   │
│   ├── services/
│   │   └── ...
│   │
│   └── tests/
│       ├── conftest.py
│       ├── test_auth_service.py
|       ├── test_category.py
│       ├── test_customer.py
│       ├── test_main.py
│       ├── test_payment.py
│       ├── test_products.py
│       ├── test_receipt.py
│       ├── test_sale_item.py
│       ├── test_sale.py
│       ├── test_security.py
│       ├── test_supplier.py
│       └── test_user.py
│
│
├── database.py
├── dependencies.py
├── main.py
├── README.md
└── requirements.txt
```

## Running Tests

To run the complete test suite locally, install the project dependencies:

```bash
pip install -r requirements.txt
```
