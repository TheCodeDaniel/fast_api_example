from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

students = {
    1: {
        'name' : 'John',
        'age' : '17',
        'class' : 'year 12'
    },
    2: {
        'name' : 'Jane',
        'age' : '15',
        'class' : 'year 10'
    }
}


# default index url
@app.get("/")
def index():
    return({'name' : 'first data'})


# path params
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="Out of range"), gt=0):
    return students[student_id]

# query params
@app.get("/get-by-name")
def get_student(*, name: Optional[str] = None, test : int):
    for student_id in students:
        if students[student_id]['name'] == name:
           return students[student_id]
    return {"Data" : "Data Not found"}

#combining path and query params