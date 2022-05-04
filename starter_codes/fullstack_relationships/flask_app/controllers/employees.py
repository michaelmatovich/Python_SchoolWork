from flask_app import app

from flask import render_template, redirect, request

from flask_app.models.employee import Employee

from flask_app.models.department import Department


@app.route('/')
def index():
    # returns list of all employees from the DB
    all_employees = Employee.get_all_employees()
    all_departments = Department.get_all_departments()
    return render_template("employees.html", all_employees = all_employees, all_departments = all_departments)

@app.route('/employees/new', methods=["POST"])
def new_employee():

    if request.form['department_id'] == '-1':
        return redirect('/')

    new_employee_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'salary': request.form['salary'],
        'department_id': request.form['department_id']
    }

    if request.form['middle_name'] == '':
        new_employee_data['middle_name'] = None
    else:
        new_employee_data['middle_name'] = request.form['middle_name']

    Employee.create_employee(new_employee_data)
    return redirect('/')

@app.route('/employees/<int:employee_id>/delete')
def delete_employee(employee_id):
    # data = {'id': employee_id}
    # Employee.delete_employee(data)
    
    Employee.delete_employee({'employee_id': employee_id})
    return redirect('/')

@app.route('/employees/<int:employee_id>/edit')
def edit_employee(employee_id):

    employee = Employee.get_employee_by_id({'employee_id': employee_id})

    return render_template("edit_employee.html", employee = employee)

@app.route('/employees/<int:employee_id>/update', methods=['POST'])
def update_employee(employee_id):
    edited_employee_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'salary': request.form['salary'],
        'employee_id': employee_id
    }

    if request.form['middle_name'] == '':
        edited_employee_data['middle_name'] = None
    else:
        edited_employee_data['middle_name'] = request.form['middle_name']

    Employee.update_employee(edited_employee_data)

    return redirect('/')
