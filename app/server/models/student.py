from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class Student(BaseModel):
    fullname: str = Field(..., min_length=1, max_length=100)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=5)
    gpa: float = Field(..., le=4.0)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Toni Kroos",
                "email": "kroos@x.edu",
                "course_of_study": "API Engineering",
                "year": 3,
                "gpa": "3.0",
            }
        }


class UpdateStudent(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Erling Haaland",
                "email": "haaland@x.edu",
                "course_of_study": "Software Engineering",
                "year": 2,
                "gpa": "3.75",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}