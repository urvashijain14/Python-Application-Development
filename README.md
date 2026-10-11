# Student Management REST API

A REST API built using Python, FastAPI, and SQLite to manage student records.

## Features

- Create a new student
- Retrieve all students
- Retrieve a student by ID
- Update student details
- Delete a student
- HTTP Basic Authentication
- Request validation using Pydantic
- Interactive API documentation using Swagger UI
- SQLite database integration

## Technologies Used

- Python
- FastAPI
- SQLite
- Pydantic
- Git and GitHub

## Project Structure

- `main.py` — API endpoints and authentication
- `database.py` — SQLite database connection and table creation
- `schemas.py` — Pydantic schema for student data
- `.gitignore` — Excludes temporary files and the local database

## How to Run the Project

1. Install Python.
2. Open a terminal in the project folder.
3. Install the required packages:

   `pip install fastapi uvicorn`

4. Start the application:

   `uvicorn main:app --reload`

5. Open the API documentation:

   `http://127.0.0.1:8000/docs`

## Authentication

The student endpoints require HTTP Basic Authentication.

Use the credentials configured in `main.py` when testing the API locally.

## Learning Outcomes

This project demonstrates REST API development, CRUD operations, SQLite integration, authentication, request validation, error handling, and API documentation.
