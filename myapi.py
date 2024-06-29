from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        'name' : 'John',
        'age' : '17',
        'year' : 'year 12'
    },
    2: {
        'name' : 'Jane',
        'age' : '15',
        'year' : 'year 10'
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None   


# default index url
@app.get("/")
def index():
    return({'name' : 'first data'})


# using path params
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="Out of range"), gt=0):
    return students[student_id]

# using query params
@app.get("/get-by-name")
def get_student(*, name: Optional[str] = None, test : int):
    for student_id in students:
        if students[student_id]['name'] == name:
           return students[student_id]
    return {"Data" : "Data Not found"}


#combining path and query params
@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, name: Optional[str] = None, test : int):
    for student_id in students:
        if students[student_id]['name'] == name:
           return students[student_id]
    return {"Data" : "Data Not found"}


#POST request
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"error" : "student exists"}
    
    students[student_id] = student
    return students

#PUT request
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
       return {"Error" : "mo student found"}
    
    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year       
    
    students[students] = student
    return students[student_id]

#DELETE request
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {'Error': 'student does not exist'}
    
    del students[student_id]
    return {"message" : "student deleted succesfully"}