# Student Management REST API

A portfolio-ready REST API built using Python, FastAPI, and SQLite to manage student records securely.

## Features

- Create a new student
- Retrieve all students
- Retrieve a student by ID
- Update student details
- Delete a student
- HTTP Basic Authentication
- Request validation using Pydantic
- SQLite database integration
- Error handling with appropriate HTTP status codes
- Application logging
- Interactive API documentation using Swagger UI

## Technologies Used

- Python
- FastAPI
- SQLite
- Pydantic
- Uvicorn
- Git and GitHub

## Project Structure

```text
Python-Application-Development/
├── main.py
├── database.py
├── schemas.py
├── README.md
├── .gitignore
└── students.db
```

**Note:** The local `students.db` file is excluded from GitHub through `.gitignore` and is created locally when the application runs.

## Architecture

1. The client sends HTTP requests through Swagger UI or an API client.
2. FastAPI receives requests and handles authentication.
3. Pydantic validates student data.
4. The API communicates with SQLite through `database.py`.
5. The API returns JSON responses and appropriate HTTP status codes.
6. Application logs record important events and database errors.

## Database Schema

The `students` table contains the following fields:

| Column | Data Type | Description |
|---|---|---|
| id | INTEGER | Primary key, auto-incremented |
| name | TEXT | Student name, required |
| email | TEXT | Required and unique email |
| age | INTEGER | Student age, required |
| course | TEXT | Course name, required |

## Installation and Setup

### 1. Install Python

Install Python and verify the installation:

```bash
python --version
```

### 2. Clone the repository

```bash
git clone https://github.com/urvashijain14/Python-Application-Development.git
cd Python-Application-Development
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install fastapi uvicorn
```

### 5. Start the application

```bash
python -m uvicorn main:app --reload
```

### 6. Open Swagger UI

Visit:

http://127.0.0.1:8000/docs

## API Endpoints

All student endpoints require HTTP Basic Authentication.

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| GET | `/students` | Retrieve all students |
| POST | `/students` | Create a student |
| GET | `/students/{student_id}` | Retrieve a student by ID |
| PUT | `/students/{student_id}` | Update a student |
| DELETE | `/students/{student_id}` | Delete a student |

## Authentication

The student endpoints use HTTP Basic Authentication.

For local testing, use the credentials configured in `main.py`. The current demo credentials are `admin` and `python123`.

**Security note:** These credentials are for demonstration only. Production applications should use securely stored credentials and environment-based configuration.

## Error Handling

The API uses appropriate HTTP status codes:

- `200` — Successful request
- `401` — Invalid authentication credentials
- `404` — Student not found
- `409` — Duplicate email
- `422` — Request validation error
- `500` — Database error

## Logging

The application uses Python's logging module to record important events and errors in an application log file.

## Learning Outcomes

This project demonstrates REST API development, CRUD operations, SQLite integration, authentication, Pydantic validation, database error handling, logging, and API documentation.

## Future Improvements

- Deploy the API to a cloud hosting platform
- Add automated tests using Pytest
- Move authentication credentials to environment variables
- Add structured application configuration
- Improve monitoring and deployment workflows

## Author

Urvashi Jain

GitHub: https://github.com/urvashijain14