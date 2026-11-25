# Product Catalog API

- This is a product management catalog API built with Django and Django REST Framework, providing main endpoints to manipulate and manage simple stores as well as nested endpoints (`stats`) for showing calculated results.

## Tools and Frameworks Required

- Python = '3.12+'
- Django = '4.0+'
- Pillow = '*'
- Django REST Framework = '*'
- drf-nested-routers = '*'
- django-filter = '*'
- Git

## Core Features

- Allows admins to create categories and organize products per category.
- Allows clients to see a list of paginated products (10 products per page) and categories, and also filter products per category.
- Access stats publicly as well, using:
  - `/store/stats/total_products/` to see the total amount of products across all categories.
  - `/store/stats/products_per_category/` for total products per category.
  - `/store/stats/avg_price_per_category/` for the average price across every category's products.

### Setup and Installation

#### Clone Repository

```bash
git clone https://github.com/Amlakyalew/ProductCatalogAPI.git
cd ProductCatalogAPI
```

#### Install Required Tools

```bash
pipenv install
```

#### Activate the Virtual Environment and Run the Program

```bash
pipenv shell
python manage.py migrate
python manage.py runserver
```

### Main Endpoints

| Method | Endpoint | Description | Authentication Required (Admin Only) |
| :--- | :--- | :--- | :--- |
| `GET` | `/store/categories/` | List all categories | No |
| `POST` | `/store/categories/` | Create a category | Yes |
| `GET` | `/store/categories/{id}/` | Retrieve category with products | No |
| `PUT` | `/store/categories/{id}/` | Update category | Yes |
| `DELETE` | `/store/categories/{id}/` | Delete category | Yes |
| `GET` | `/store/products/` | List products (paginated) | No |
| `POST` | `/store/products/` | Create a product | Yes |
| `GET` | `/store/products/{id}/` | Retrieve product with images | No |
| `PUT` | `/store/products/{id}/` | Update product | Yes |
| `DELETE` | `/store/products/{id}/` | Delete product | Yes |
| `GET` | `/store/products/?category={id}` | Filter products by category | No |
| `POST` | `/store/products/{id}/images/` | Upload image for product | Yes |
| `GET` | `/store/products/{id}/images/` | List images for product | No |
| `DELETE` | `/store/images/{id}/` | Delete product image | Yes |
| `GET` | `/store/stats/total_products/` | Total product count | No |
| `GET` | `/store/stats/products_per_category/` | Products count per category | No |
| `GET` | `/store/stats/avg_price_per_category/` | Average price per category | No |

# I would like to say thanks for my teams and GORP_Community.
