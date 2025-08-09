from database import get_db_connection

def get_all_students():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return students

def add_student(name, age, course):
    conn = get_db_connection()
    conn.execute('INSERT INTO students (name, age, course) VALUES (?, ?, ?)', (name, age, course))
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()
