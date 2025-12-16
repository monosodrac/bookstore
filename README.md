[PYTHON_BADGE]:https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[DJANGO_BADGE]:https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[DRF_BADGE]:https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray
[DOCKER_BADGE]:https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[POETRY_BADGE]:https://img.shields.io/badge/Poetry-%233B82F6.svg?style=for-the-badge&logo=poetry&logoColor=0B3D8D
[PRS_BADGE]:https://img.shields.io/badge/PRs-welcome-green?style=for-the-badge

<h1 align="center" style="font-weight: bold;">Bookstore API 📚</h1>

![python][PYTHON_BADGE]
![django][DJANGO_BADGE]
![drf][DRF_BADGE]
![docker][DOCKER_BADGE]
![poetry][POETRY_BADGE]
![prs][PRS_BADGE]

<details open="open">
<summary>Table of Contents</summary>

- [🚀 Getting Started](#started)
  - [Prerequisites](#prerequisites)
  - [Cloning](#cloning)
  - [Environment Setup](#environment)
  - [Running the Application](#running)
- [📍 How It Works](#how-it-works)
- [🔌 API Endpoints](#endpoints)
- [🧰 Files Overview](#files)
- [⚙️ Technologies Used](#tech)
- [🧪 Testing](#testing)
- [🤝 How to Reach Me](#reach)
- [📫 Contribute](#contribute)
- [📌 Notes](#notes)

</details>

<p align="center">
  <b>A RESTful API built with Django REST Framework for managing a bookstore, including products, categories, and orders with authentication.</b>
</p>

---

<h2 id="started">🚀 Getting Started</h2>

<h3 id="prerequisites">Prerequisites</h3>

- [Python 3.10+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started) & [Docker Compose](https://docs.docker.com/compose/install/) (recommended)
- [Poetry](https://python-poetry.org/docs/#installation) (for local development)
- [PostgreSQL 15](https://www.postgresql.org/download/) (or use Docker Compose)

<h3 id="cloning">Cloning</h3>

```bash
git clone https://github.com/monosodrac/bookstore.git
cd bookstore
```

<h3 id="environment">Environment Setup</h3>

**Create Virtual Environment:**

```bash
python -m venv .env
```

**Enter Virtual Environment:**

***Windows CMD***
```bash
.env\scripts\activate
```

***Linux/MacOS***
```bash
source .env/bin/activate
```

**Install Poetry:**
```bash
pip install poetry
```

**Using Poetry:**

```bash
poetry install
poetry shell
```

**Using Docker Compose (Recommended):**

```bash
docker-compose up --build
```

This will start both the Django application and PostgreSQL database.

**Using Docker (without compose):**

```bash
docker build -t bookstore-api .
docker run -p 8000:8000 bookstore-api
```

<h3 id="running">Running the Application</h3>

**With Docker Compose:**

The application will automatically start on `http://localhost:8000/` after running `docker-compose up`.

To run migrations inside the container:

```bash
docker-compose exec web python manage.py migrate
```

To create a superuser:

```bash
docker-compose exec web python manage.py createsuperuser
```

**Without Docker:**

Apply migrations:

```bash
python manage.py migrate
```

**Create a superuser (for admin access):**

```bash
python manage.py createsuperuser
```

**Start the development server:**

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

<h2 id="how-it-works">📍 How It Works</h2>

The Bookstore API provides a complete backend solution for managing an online bookstore:

1. **Products & Categories**: Create and manage products with multiple categories using a many-to-many relationship.
2. **Orders**: Users can create orders with multiple products, with automatic total calculation.
3. **Authentication**: Supports SessionAuthentication, BasicAuthentication, and TokenAuthentication.
4. **Permissions**: Order endpoints require authentication to access.
5. **Serialization**: Uses nested serializers to display related category and product data.

<h2 id="endpoints">🔌 API Endpoints</h2>

### Products

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/products/` | List all products | No |
| POST | `/products/` | Create a new product | No |
| GET | `/products/{id}/` | Retrieve a specific product | No |
| PUT | `/products/{id}/` | Update a product | No |
| DELETE | `/products/{id}/` | Delete a product | No |

**Product Request Example:**

```json
{
  "title": "The Great Gatsby",
  "description": "A classic American novel",
  "price": 50,
  "active": true,
  "categories_id": [1, 2]
}
```

### Categories

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/categories/` | List all categories | No |
| POST | `/categories/` | Create a new category | No |
| GET | `/categories/{id}/` | Retrieve a specific category | No |
| PUT | `/categories/{id}/` | Update a category | No |
| DELETE | `/categories/{id}/` | Delete a category | No |

### Orders

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/orders/` | List all orders | Yes |
| POST | `/orders/` | Create a new order | Yes |
| GET | `/orders/{id}/` | Retrieve a specific order | Yes |
| PUT | `/orders/{id}/` | Update an order | Yes |
| DELETE | `/orders/{id}/` | Delete an order | Yes |

**Order Request Example:**

```json
{
  "user": 1,
  "product": [1, 2, 3]
}
```

<h2 id="files">🧰 Files Overview</h2>

### Product App

| File | Description |
|------|-------------|
| `product/models/product.py` | Product model with title, description, price, and category relationship |
| `product/models/category.py` | Category model for organizing products |
| `product/serializers/product_serializer.py` | Serializer with nested category data and create logic |
| `product/serializers/category_serializer.py` | Category serializer |
| `product/views/product_viewset.py` | ViewSet for product CRUD operations |
| `product/views/category_viewset.py` | ViewSet for category CRUD operations |
| `product/tests.py` | Unit tests for product functionality |

### Order App

| File | Description |
|------|-------------|
| `order/models.py` | Order model linking users and products |
| `order/serializers/order_serializer.py` | Order serializer with automatic total calculation |
| `order/views/order_viewset.py` | ViewSet with authentication and permissions |
| `order/tests.py` | Unit tests for order functionality |

### Docker & Dependencies

| File | Description |
|------|-------------|
| `Dockerfile` | Multi-stage Docker configuration |
| `poetry.lock` | Locked dependency versions |
| `pyproject.toml` | Poetry configuration and dependencies |

<h2 id="tech">⚙️ Technologies Used</h2>

- 🐍 **Python 3.10+** – Modern Python with type hints support
- 🎯 **Django** – High-level web framework
- 🔌 **Django REST Framework** – Powerful toolkit for building Web APIs
- 🐳 **Docker** – Containerization for consistent environments
- 📦 **Poetry** – Dependency management and packaging
- 🗄️ **PostgreSQL** – Production-ready relational database (optional)
- 🔐 **Token Authentication** – Secure API access control

<h2 id="testing">🧪 Testing</h2>

Run the test suite:

**With Docker Compose:**

```bash
docker-compose exec web python manage.py test
```

**Without Docker:**

```bash
python manage.py test
```

**Test Coverage:**

- ✅ Product creation with categories
- ✅ Product serialization with nested category data
- ✅ Order creation with multiple products
- ✅ Automatic order total calculation
- ✅ Authentication and permissions

<h2 id="reach">🤝 How to reach me</h2>

<table>
  <tr>
    <td align="center">
      <a href="https://linktr.ee/monosodrac">
        <img src="https://avatars.githubusercontent.com/u/141099551?v=4" width="100px;" alt="Mono Cardoso Profile Picture"/><br>
        <sub>
          <b>Mono</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

<h2 id="contribute">📫 Contribute</h2>

Contributions are welcome! 🧩
If you'd like to improve this API or add new features, follow these steps:

1. Clone the repository
```bash
git clone https://github.com/monosodrac/bookstore.git
```
2. Create a new branch for your feature or fix
```bash
git checkout -b feature/your-feature-name
```
3. Follow good commit practices
4. After implementing your changes, open a Pull Request including:
    - Description of what was improved or added
    - How to test the update
    - (Optional) example of API request/response or screenshots

Once submitted, your PR will be reviewed and merged if approved 🚀

<h2 id="notes">📌 Notes</h2>

- This project uses **Docker Compose** to orchestrate the Django application and PostgreSQL database
- The database uses **PostgreSQL 15 Alpine** for a lightweight production-ready setup
- Environment variables are managed through the `env.dev` file
- The project uses **Poetry** for dependency management instead of traditional `requirements.txt`
- The API follows **RESTful** principles and uses **ViewSets** for cleaner code
- **Authentication** is required only for order-related endpoints
- Prices are stored as positive integers (in cents) to avoid floating-point issues
- The **ManyToMany** relationship allows products to belong to multiple categories
- Tests are included to ensure core functionality works correctly
- Docker volumes persist PostgreSQL data across container restarts
- The application runs on port **8000** by default
