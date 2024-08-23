from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    add_student,
    delete_student,
    retrieve_student,
    retrieve_students,
    update_student,
)

from app.server.models.student import (
    ErrorResponseModel,
    ResponseModel,
    Student,
    UpdateStudent,
)

router = APIRouter()


@router.post("/", response_description="Student data added into the database")
async def add_student_data(student: Student = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return ResponseModel(new_student, "Student added successfully.")


@router.get("/", response_description="All Students retrieved")
async def get_students():
    students = await retrieve_students()
    if students:
        return ResponseModel(students, "All Students retrieved successfully")
    return ResponseModel(students, "Empty list returned")


@router.get("/{id}", response_description="Single Student data retrieved")
async def get_student_data(id):
    student = await retrieve_student(id)
    if student:
        return ResponseModel(student, "Single Student data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Student doesn't exist.")


@router.put("/{id}", response_description="Student data updated in the database")
async def update_student_data(id: str, body: UpdateStudent = Body(...)):
    body = {k: v for k, v in body.model_dump().items() if v is not None}
    updated_student = await update_student(id, body)
    if updated_student:
        return ResponseModel(
            "Student with ID: {} name update is successful".format(id),
            "Student name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the student data.",
    )


@router.delete("/{id}", response_description="Student data deleted from the database")
async def delete_student_data(id: str):
    deleted_student = await delete_student(id)
    if deleted_student:
        return ResponseModel(
            "Student with ID: {} removed".format(id), "Student deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Student with id {0} doesn't exist".format(id)
    )