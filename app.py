from flask import Flask, render_template, request, redirect, url_for, session
from database import init_db, get_db_connection
import models

app = Flask(__name__)
app.secret_key = 'your_secret_key'

init_db()

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            session['admin'] = True
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect('/login')

@app.route('/dashboard')
def dashboard():
    if 'admin' not in session:
        return redirect('/login')
    students = models.get_all_students()
    return render_template('dashboard.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        course = request.form['course']
        models.add_student(name, age, course)
        return redirect('/dashboard')
    return render_template('add_student.html')

@app.route('/delete/<int:id>')
def delete_student(id):
    models.delete_student(id)
    return redirect('/dashboard')

if __name__ == '__main__':
    app.run(debug=True)
