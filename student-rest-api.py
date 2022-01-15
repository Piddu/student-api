
from urllib import request
from student import Student, Grade
from uuid import UUID, uuid4
from fastapi import FastAPI, Request
from fastapi.openapi.utils import get_openapi
from fastapi import applications
from fastapi.openapi.docs import get_swagger_ui_html
from typing import List



db: List[Student]  = [
    Student(
            id = uuid4(),
            firstname = "Marco",
            lastname = "Canedoli",
            birthdate = "1984-09-08T00:00:00.000",
            grades  = [Grade(subject = "Math", grade = 25), Grade(subject = "Chemistry", grade = 27)]
        )
]


app = FastAPI(prefix='/api')


#router = APIRouter(prefix='/users')

@app.get("/")
async def root():
    return{"Home":"Home"}

@app.get("/api/v1/students")
async def fetch_students():
    return db


@app.get("/api/v1/student/{student_id}")
async def fetch_student(student_id: UUID):
    if student_id:
        for student in db:
            if student.id == student_id:
                return student

@app.get("/api/v1/student/{student_id}/age")
async def fetch_student_age(student_id: UUID):
    if student_id:
        for student in db:
            if student.id == student_id:
                age = student.calculateAge()
                return {"age" : age}

@app.get("/api/v1/student/{student_id}/avg-grade")
async def fetch_student_avg_grade(student_id: UUID):
    if student_id:
        for student in db:
            if student.id == student_id:
                avg_grade = student.calculateAvgGrade()
                return {"avgGrade" : avg_grade}

@app.post("/api/v1/students")
async def register_student(student: Request):
    req_student = await student.json()
    student = Student(
                     firstname= req_student['firstname'], 
                     lastname = req_student['lastname'], 
                     birthdate = req_student['birthdate'], 
                     grades = req_student['grades']
                     )
    student.id = uuid4()
    db.append(student)
    return student
 
#non usato, /docs non funziona con questo metodos
"""
@app.post("/api/v1/students")
async def register_student(student: Student):
    student.id = uuid4()
    db.append(student)
    return student
 
"""
