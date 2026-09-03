# Student Management API

A RESTful Student Management API built with Python, FastAPI, and SQLite. The project manages student records through CRUD operations and uses a persistent SQLite database for data storage.

## Features

* Retrieve all students
* Retrieve a student by ID
* Create new student records
* Update existing student records
* Delete student records
* Persistent data storage using SQLite
* Request and response validation using Pydantic
* HTTP status codes for successful and failed operations
* Custom exceptions for duplicate and missing students
* Automatic API documentation with Swagger/OpenAPI

## Technologies

* Python
* FastAPI
* Pydantic
* SQLite
* Uvicorn

## API Endpoints

| Method | Endpoint                 | Description                |
| ------ | ------------------------ | -------------------------- |
| GET    | `/students`              | Retrieve all students      |
| GET    | `/students/{student_id}` | Retrieve a student by ID   |
| POST   | `/students`              | Create a new student       |
| PUT    | `/students/{student_id}` | Update an existing student |
| DELETE | `/students/{student_id}` | Delete a student           |

## Example Student

```json
{
    "id": "2298334",
    "name": "Sarah Michel",
    "department": "Computer Science",
    "level": 300
}
```

## Project Structure

```text
Student-Management-API/
│
├── main.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
└── students.db
```

> `students.db` is generated locally by the application and should be excluded from Git using `.gitignore`.

## How It Works

The application separates API operations from database operations.

```text
Client
   ↓
FastAPI
   ↓
Pydantic Validation
   ↓
Database Functions
   ↓
SQLite Database
   ↓
JSON Response
```

`main.py` handles the API endpoints and HTTP responses, while `database.py` handles SQLite operations such as creating, retrieving, updating, and deleting student records.

## Installation

Clone the repository and navigate into the project directory.

```bash
git clone <repository-url>
cd Student-Management-API
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the API

Start the FastAPI application with Uvicorn:

```bash
python -m uvicorn main:app --reload
```

The API will be available locally at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides interactive API documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

You can use the Swagger interface to send requests to each endpoint and test the API.

## Database

The application uses SQLite for persistent student data storage.

The database and `students` table are created automatically when `database.py` is initialized.

The table contains:

| Column       | Type    | Description              |
| ------------ | ------- | ------------------------ |
| `id`         | TEXT    | Unique student ID        |
| `name`       | TEXT    | Student's name           |
| `department` | TEXT    | Student's department     |
| `level`      | INTEGER | Student's academic level |

## Error Handling

The API handles common errors using appropriate HTTP responses:

* `404 Not Found` when a requested student does not exist
* `409 Conflict` when attempting to create a student with an existing ID
* `201 Created` when a student is successfully created

## Development Progress

This project evolved from an earlier command-line Student Management System that used in-memory Python dictionaries.

The project was upgraded to:

1. FastAPI for REST API development
2. Pydantic for request and response validation
3. SQLite for persistent data storage
4. CRUD operations through HTTP endpoints
5. Custom exception handling and HTTP status codes

## Future Improvements

Planned improvements include:

* Stronger request validation
* Improved database connection management
* Automated tests
* Better separation of application layers
* More detailed API documentation
* Additional student management features
* Migration to a larger relational database such as MySQL or PostgreSQL

## Author

**Chidera Ugwu Valentine**

Computer Science Student | Python & Software Development | Exploring AI, APIs & Backend Engineering
