import sqlite3

con = sqlite3.connect('students.db')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS students(id TEXT PRIMARY KEY, name TEXT, department TEXT, level INTEGER)")
con.commit()
con.close()

class StudentAlreadyExistsError(Exception):
    pass

class StudentNotFoundError(Exception):
    pass

def get_students_db():
    new_con = sqlite3.connect('students.db')
    new_cur = new_con.cursor()
    res = new_cur.execute("SELECT * FROM students")
    result = res.fetchall()
    new_con.close()
    return result

def get_student_db(student_id):
    new_con = sqlite3.connect('students.db')
    new_cur = new_con.cursor()
    res = new_cur.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    result = res.fetchone()
    new_con.close()
    return result

def create_student_db(student_id, student_name, student_department, student_level):
    new_con = sqlite3.connect('students.db')
    new_cur = new_con.cursor()
    try:
        new_cur.execute("INSERT INTO students (id, name, department, level) VALUES (?, ?, ?, ?)", (student_id, student_name, student_department, student_level))
        new_con.commit()
        res = new_cur.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        return res.fetchone()
    except sqlite3.IntegrityError:
        raise StudentAlreadyExistsError
    finally:
        new_con.close()

def update_student_db(student_id, student_name, student_department, student_level):
    new_con = sqlite3.connect('students.db')
    new_cur = new_con.cursor()
    try:
        new_cur.execute("UPDATE students SET name = ?, department = ?, level = ? WHERE id = ?", (student_name, student_department, student_level, student_id))
        count = new_cur.rowcount
        if count == 0:
            raise StudentNotFoundError
        new_con.commit()
        res = new_cur.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        return res.fetchone()
    finally:
        new_con.close()

def delete_student_db(student_id):
    new_con = sqlite3.connect('students.db')
    new_cur = new_con.cursor()
    try:
        new_cur.execute("DELETE FROM students WHERE id = ?", (student_id,))
        if new_cur.rowcount == 0:
            raise StudentNotFoundError
        new_con.commit()
        return True
    finally:
        new_con.close()
