from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
import sqlite3
from database import create_table, get_connection
from schemas import StudentCreate
app = FastAPI(
    title="Student Management API",
    description="A REST API to create, view, update, and delete student records with authentication and validation.",
    version="1.0.0"
)
create_table()
security = HTTPBasic()


def verify_credentials(
    credentials: HTTPBasicCredentials = Depends(security)
):
    correct_username = secrets.compare_digest(
        credentials.username, "admin"
    )

    correct_password = secrets.compare_digest(
        credentials.password, "python123"
    )

    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Basic"}
        )

    return credentials.username

students = [
    {
        "id": 1,
        "name": "Amit",
        "age": 21,
        "course": "Python"
    },
    {
        "id": 2,
        "name": "Priya",
        "age": 22,
        "course": "Django"
    },
    {
        "id": 3,
        "name": "Rahul",
        "age": 20,
        "course": "FastAPI"
    }
]


@app.get(
    "/",
    summary="Home",
    description="Check whether the Student Management API is running."
)
def home():
    return {"message": "Student Management API is running!"}

@app.get(
    "/students",
    summary="Get All Students",
    description="Retrieve all student records from the database. Authentication is required.",
    dependencies=[Depends(verify_credentials)]
)
def get_students():
    connection = get_connection()

    rows = connection.execute(
        "SELECT * FROM students"
    ).fetchall()

    connection.close()

    return {
        "students": [dict(row) for row in rows]
    }

@app.get(
    "/students/{student_id}",
    summary="Get Student by ID",
    description="Retrieve a single student using their ID. Returns 404 if the student does not exist.",
    dependencies=[Depends(verify_credentials)]
)

def get_student(student_id: int):
    connection = get_connection()

    row = connection.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    ).fetchone()

    connection.close()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return dict(row)
@app.put(
    "/students/{student_id}",
    summary="Update Student",
    description="Update an existing student's name, email, age, and course using their ID.",
    dependencies=[Depends(verify_credentials)]
)

def update_student(
    student_id: int,
    name: str,
    email: str,
    age: int,
    course: str
):
    connection = get_connection()

    cursor = connection.execute(
        """
        UPDATE students
        SET name = ?, email = ?, age = ?, course = ?
        WHERE id = ?
        """,
        (name, email, age, course, student_id)
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    connection.close()

    return {
        "message": "Student updated successfully"
    }
@app.delete(
    "/students/{student_id}",
    summary="Delete Student",
    description="Delete an existing student using their ID. Returns 404 if the student does not exist.",
    dependencies=[Depends(verify_credentials)]
)
def delete_student(student_id: int):
    connection = get_connection()

    cursor = connection.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    connection.commit()

    if cursor.rowcount == 0:
        connection.close()
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    connection.close()

    return {
        "message": "Student deleted successfully"
    }
@app.post(
    "/students",
    summary="Create Student",
    description="Create a new student record. Name, email, age, and course are required. Authentication is required.",
    dependencies=[Depends(verify_credentials)]
)
def create_student(student: StudentCreate):
    connection = get_connection()

    try:
        cursor = connection.execute(
            """
            INSERT INTO students (name, email, age, course)
            VALUES (?, ?, ?, ?)
            """,
            (student.name, student.email, student.age, student.course)
        )

        connection.commit()

        return {
            "message": "Student created successfully",
            "student_id": cursor.lastrowid
        }

    except sqlite3.IntegrityError:
      connection.rollback()
      raise HTTPException(
        status_code=409,
        detail="A student with this email already exists"
    )
    except sqlite3.Error:
      connection.rollback()
      raise HTTPException(
        status_code=500,
        detail="A database error occurred"
    )
    finally:
        connection.close()
      

