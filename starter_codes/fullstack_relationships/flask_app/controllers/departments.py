from flask_app import app

from flask import render_template, redirect, request

from flask_app.models.department import Department

@app.route('/departments')
def department_index():

    all_departments = Department.get_all_departments()

    return render_template("departments.html", all_departments = all_departments)

@app.route('/departments/new')
def new_department():
    return render_template("new_department.html")

@app.route('/departments/create', methods=['POST'])
def create_department():

    data = {
        'name': request.form['department_name'],
        'location': request.form['department_location']
    }

    Department.create_department(data)

    return redirect('/departments')
