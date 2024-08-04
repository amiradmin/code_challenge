# Library API Code Test

This is a Django REST framework-based API for managing a library system. It includes functionality for user registration and authentication, book management, and categorization.

## Features

- User Registration and Authentication (using JWT)
- Book Management (CRUD operations)
- Category Management (CRUD operations)
- Profile Management
- Book Availability Status

## Endpoints Overview

### User Endpoints

- **POST /api/users/register/**: Register a new user.
- **POST /api/token/**: Obtain JWT token.
- **POST /api/token/refresh/**: Refresh JWT token.
- **GET /api/users/profile/**: Retrieve the authenticated user's profile.
- **PUT /api/users/profile/**: Update the authenticated user's profile.

### Book Endpoints

- **GET /api/books/**: List all books.
- **POST /api/books/**: Create a new book (admin only).
- **GET /api/books/{id}/**: Retrieve a specific book by ID.
- **PUT /api/books/{id}/**: Update a book by ID (admin only).
- **DELETE /api/books/{id}/**: Delete a book by ID (admin only).

### Category Endpoints

- **GET /api/categories/**: List all categories.
- **POST /api/categories/**: Create a new category.
- **GET /api/categories/{id}/**: Retrieve a specific category by ID.
- **PUT /api/categories/{id}/**: Update a category by ID.
- **DELETE /api/categories/{id}/**: Delete a category by ID.

## Request and Response Formats

### User Registration

**Request:**
```json
{
    "username": "john_doe",
    "password": "securepassword123",
    "email": "john@example.com",
    "profile": {
        "bio": "Software developer"
    }
}
Response (201 Created):

{
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "profile": {
        "bio": "Software developer"
    }
}






Obtain JWT Token
Request:
{
    "username": "john_doe",
    "password": "securepassword123"
}
Response (200 OK):


{
    "access": "eyJ0eXAiOiJKV1QiLCJh...<access_token>...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJh...<refresh_token>..."
}




Refresh JWT Token
Request:
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJh...<refresh_token>..."
}
Response (200 OK):
{
    "access": "eyJ0eXAiOiJKV1QiLCJh...<new_access_token>..."
}





Book Creation
Request:


{
    "title": "New Book",
    "author": "Author Name",
    "published_date": "2024-08-04",
    "isbn": "1234567890123",
    "category": 1
}
Response (201 Created):


Result:
{
    "id": 1,
    "title": "New Book",
    "author": "Author Name",
    "published_date": "2024-08-04",
    "isbn": "1234567890123",
    "category": {
        "id": 1,
        "name": "Category Name"
    },
    "status": "available",
    "created_at": "2024-08-04T12:34:56Z"
}
Book Retrieval
Response (200 OK):

{
    "id": 1,
    "title": "New Book",
    "author": "Author Name",
    "published_date": "2024-08-04",
    "isbn": "1234567890123",
    "category": {
        "id": 1,
        "name": "Category Name"
    },
    "status": "available",
    "created_at": "2024-08-04T12:34:56Z"
}
Error Responses
400 Bad Request
For invalid data input, such as when a book with the same ISBN already exists:


{
    "isbn": ["book with this isbn already exists."]
}
401 Unauthorized
When authentication fails:


{
    "detail": "No active account found with the given credentials"
}
403 Forbidden
When a user tries to access a resource they don’t have permission for:


{
    "detail": "You do not have permission to perform this action."
}
404 Not Found
When a resource is not found:


{
    "detail": "Not found."
}



Authentication
The API uses JWT (JSON Web Tokens) for authentication.

POST /api/token/: Obtain JWT token.
POST /api/token/refresh/: Refresh JWT token.
Data Validation and Error Handling
Data Validation: Ensured through Django and DRF serializers.
Example: Ensuring unique ISBNs for books.
Error Handling: Standardized error responses with appropriate HTTP status codes.
Setup and Deployment
Clone the Repository


## Setup and Deployment

### Prerequisites

- Docker
- Docker Compose

### Environment Variables

Create a `.env` file in the root directory with the following content:

```env
POSTGRES_DB=yourdbname
POSTGRES_USER=yourdbuser
POSTGRES_PASSWORD=yourdbpassword
DATABASE_URL=postgres://yourdbuser:yourdbpassword@db:5432/yourdbname
SECRET_KEY=your-secret-key
DEBUG=1
Docker Deployment
Build and start the containers:

sh
Copy code
docker-compose up --build
**Run Django migrations
127.0.0.1:8000/admin/ and log in with the superuser credentials.