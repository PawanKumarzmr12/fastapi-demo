import sys
import os

# Ensure app module is found
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_student():
    response = client.post(
        "/students/",  # route path as per your students.py
        json={"name": "John", "age": 22, "grade": "A"}  # grade is required
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John"
    assert data["age"] == 22
    assert data["grade"] == "A"
    assert "id" in data

def test_get_students():
    # Create a student first
    client.post("/students/", json={"name": "Alice", "age": 25, "grade": "B"})

    response = client.get("/students/")  # get all students
    assert response.status_code == 200
    students = response.json()
    assert len(students) > 0
    assert any(s["name"] == "Alice" for s in students)

def test_get_student_not_found():
    response = client.get("/students/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found"

def test_delete_student():
    # create student
    res = client.post("/students/", json={"name": "Charlie", "age": 22, "grade": "C"})
    student_id = res.json()["id"]

    delete_response = client.delete(f"/students/{student_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Student deleted successfully"

def test_delete_student_not_found():
    response = client.delete("/students/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found"
