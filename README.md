# E-commerce API

This project is a RESTful API for an e-commerce platform built with Django and Django Rest Framework. It provides endpoints for managing products, user authentication, and more.

## Features

- User authentication and authorization
- Product management (CRUD operations)
- Advanced filtering and search capabilities for products
- Pagination for efficient data retrieval
- MySQL database integration

## Technologies Used

- Python
- Django
- Django Rest Framework
- SQLlite
- JWT for authentication

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/sacro123/ecommerce-api.git
   cd ecommerce-api
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up the MySQL database:
   - Create a new MySQL database
   - Update the database configuration in `settings.py`

5. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

### Authentication

- `POST /api/token/`: Obtain a JWT token
- `POST /api/token/refresh/`: Refresh a JWT token

### Products

- `GET /api/products/`: List all products (with pagination)
- `POST /api/products/`: Create a new product
- `GET /api/products/{id}/`: Retrieve a specific product
- `PUT /api/products/{id}/`: Update a specific product
- `DELETE /api/products/{id}/`: Delete a specific product
- `GET /api/products/search/`: Search products

### Users

- `POST /api/users/register/`: User registration
- `POST /api/users/login/`: Login a user
- `GET /api/users/profile/`: Get current user profile
- `PUT /api/users/profile/`: Update user profile

## Filtering and Searching

You can filter and search products using query parameters:

- Filter by category: `/api/products/?category=Electronics`
- Search by name or description: `/api/products/search/?search=laptop`
- Filter by price range: `/api/products/?min_price=100&max_price=500`
- Order results: `/api/products/?ordering=-price`

## Pagination

Results are paginated by default. You can specify the page number and page size:

- `/api/products/?page=2&page_size=10`

## Authentication

This API uses JWT Authentication. Include the JWT token in the Authorization header of your requests:

```
Authorization: Bearer <your_token_here>
```
