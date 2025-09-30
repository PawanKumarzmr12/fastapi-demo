from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.student_schema import Student, StudentCreate
from app.crud import student_crud

router = APIRouter()

@router.post("/", response_model=Student)
async def create_student(student: StudentCreate):
    return await student_crud.create_student(student)

@router.get("/", response_model=List[Student])
async def get_all_students():
    return await student_crud.get_students()

@router.get("/{student_id}", response_model=Student)
async def get_student(student_id: int):
    student = await student_crud.get_student_by_id(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.delete("/{student_id}")
async def delete_student(student_id: int):
    success = await student_crud.delete_student(student_id)
    if not success:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
