from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import employee

class Department():

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.employees = []

    def calculate_total_employee_salary(self):
        total_salary = 0
        for employee in self.employees:
            total_salary += employee.salary
        return total_salary

    @classmethod
    def create_department(cls, data):
        query = "INSERT INTO departments (name, location) VALUES (%(name)s, %(location)s);"

        result = connectToMySQL("apr_employees").query_db(query, data)

        return result

    @classmethod
    def get_all_departments(cls):
        query = "SELECT * FROM departments LEFT JOIN employees ON departments.id = employees.department_id;"

        results = connectToMySQL("apr_employees").query_db(query)

        departments = []

        new_department = Department(results[0])

        departments.append(new_department)

        for result in results:
            print(result)
            if result['id'] != departments[-1].id:
                new_department = Department(result)
                departments.append(new_department)
            employee_data = {
                'id': result['employees.id'],
                'first_name': result['first_name'],
                'middle_name': result['middle_name'],
                'last_name': result['last_name'],
                'salary': result['salary'],
                'department_id': result['department_id'],
                'created_at': result['employees.created_at'],
                'updated_at': result['employees.updated_at']
            }
            if result['employees.id'] != None:
                new_employee = employee.Employee(employee_data)
                new_employee.department = new_department
                new_department.employees.append(new_employee)

        return departments