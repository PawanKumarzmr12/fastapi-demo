from typing import List, Optional
from app.schemas.student_schema import Student, StudentCreate

students_db: List[Student] = []
counter = 1

async def create_student(student: StudentCreate) -> Student:
    global counter
    new_student = Student(id=counter, **student.dict())
    students_db.append(new_student)
    counter += 1
    return new_student

async def get_students() -> List[Student]:
    return students_db

async def get_student_by_id(student_id: int) -> Optional[Student]:
    for student in students_db:
        if student.id == student_id:
            return student
    return None

async def delete_student(student_id: int) -> bool:
    global students_db
    for student in students_db:
        if student.id == student_id:
            students_db.remove(student)
            return True
    return False
