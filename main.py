from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import get_student_db, get_students_db, create_student_db, StudentAlreadyExistsError, update_student_db, \
	StudentNotFoundError, delete_student_db

'''
	This is a Student Management API framework that assesses the student database to:
	- get either all the students or a particular student information through the endpoint where the id is passed in as a path parameter,
	- add and update the students information using their specific id passed in as a path parameter through the endpoint,
	- and finally it can delete a student through their id passed into the endpoint as a path parameter
	
	It previously used the students dictionary below as a temporal storage unit but got upgraded to a database that is persistent
'''
# students = {
# 		'2298334' :
# 			{
# 			'id': '2298334',
# 		    'name': 'Sarah Michel',
# 		    'department': 'Computer Science',
# 		    'level': 300
# 			},
# 		'2222134' :
# 			{
# 			'id': '2222134',
# 			'name': 'Chidera Ugwu',
# 			'department': 'Computer Science',
# 			'level': 300
# 			},
# 		'3112334' :
# 			{
# 			'id': '3112334',
# 			'name': 'Ogbonna Madu',
# 			'department': 'Economics',
# 			'level': 400
# 		},
# 			'2998763' :
# 			{
# 			'id': '2998763',
# 			'name': 'Nneoma Uju',
# 			'department': 'Medical Laboratory Science',
# 			'level': 500
# 			},
# 		}

app = FastAPI()

class Student(BaseModel):
	id: str
	name: str
	department: str
	level: int

class StudentCreate(BaseModel):
	id: str
	name: str
	department: str
	level: int

class StudentUpdate(BaseModel):
	name: str
	department: str
	level: int

@app.get("/students")
def get_students():
	students = get_students_db()
	all_students = []
	for student in students:
		each_student = Student(
			id = student[0],
			name = student[1],
			department = student[2],
			level = student[3]
		)
		all_students.append(each_student)
	return all_students

@app.get("/students/{student_id}")
def get_student(student_id: str):
	result1 = get_student_db(student_id)
	if result1 is not None:
		student = Student(
			id = result1[0],
			name = result1[1],
			department = result1[2],
			level = result1[3]
		)
		return student
	else:
		raise HTTPException(status_code=404, detail="Student not found")

@app.post("/students", status_code=201, response_model=Student)
def create_student(student : StudentCreate):
	try:
		new_student = create_student_db(student.id, student.name, student.department, student.level)
		student = Student(
			id = new_student[0],
			name = new_student[1],
			department = new_student[2],
			level = new_student[3]
		)
		return student
	except StudentAlreadyExistsError:
		raise HTTPException(status_code=409, detail="Conflict")


@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id : str, student : StudentUpdate):
	try:
		changed_student = update_student_db(student_id, student.name, student.department, student.level)
		student = Student(
			id=changed_student[0],
			name=changed_student[1],
			department=changed_student[2],
			level=changed_student[3]
		)
		return student
	except StudentNotFoundError:
		raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}")
def delete_student(student_id : str):
	try:
		delete_student_db(student_id)
		return {"message": "Student successfully deleted"}
	except StudentNotFoundError:
		raise HTTPException(status_code=404, detail="Student not found")

