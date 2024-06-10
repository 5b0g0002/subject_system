from flask import render_template, current_app as app
from .db import mysql

@app.route('/')
def password():
    title = '選課系統-登入'
    return render_template('password.html', title=title)

@app.route('/index.html')
def index():
    title = '最新消息'
    return render_template('index.html', title=title)

@app.route('/selection.html')
def selection():
    title = '選課系統'
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT subject_category, subject, credits, hours, course_code, additional_info FROM semester_112_1")
    data = cursor.fetchall()
    cursor.close()
    return render_template('selection.html', title=title, courses=data)
