from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.department import Department

class Employee():

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.middle_name = data['middle_name']
        self.last_name = data['last_name']
        self.salary = data['salary']
        self.department_id = data['department_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.department = None

    @property
    def full_name(self):
        if self.middle_name != None:
            return f"{self.first_name} {self.middle_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.last_name}"

    # before we had departments involved:
    # @classmethod
    # def get_all_employees(cls):
    #     query = "SELECT * FROM employees;"

    #     results = connectToMySQL("apr_employees").query_db(query)

    #     print(results)

    #     employees = []

    #     for row in results:
    #         employees.append(Employee(row))

    #     return employees

    @classmethod
    def get_all_employees(cls):
        query = "SELECT * FROM employees JOIN departments ON employees.department_id = departments.id;"

        results = connectToMySQL("apr_employees").query_db(query)

        employees = []

        for row in results:

            new_employee = Employee(row)

            department_data = {
                'id': row['departments.id'],
                'name': row['name'],
                'location': row['location'],
                'created_at': row['departments.created_at'],
                'updated_at': row['departments.updated_at']
            }

            new_department = Department(department_data)

            new_employee.department = new_department

            employees.append(new_employee)

        return employees

    @classmethod
    def create_employee(cls, data):
        query = "INSERT INTO employees (first_name, middle_name, last_name, salary, department_id) VALUES (%(first_name)s, %(middle_name)s, %(last_name)s, %(salary)s, %(department_id)s);"

        result = connectToMySQL("apr_employees").query_db(query, data)

        return result


    @classmethod
    def delete_employee(cls, data):
        query = 'DELETE FROM employees WHERE id = %(employee_id)s;'

        connectToMySQL("apr_employees").query_db(query, data)

    @classmethod
    def get_employee_by_id(cls, data):
        query = 'SELECT * FROM employees WHERE id = %(employee_id)s;'

        results = connectToMySQL("apr_employees").query_db(query, data)

        employee = Employee(results[0])

        return employee

    @classmethod
    def update_employee(cls, data):

        query = "UPDATE employees SET first_name = %(first_name)s, middle_name = %(middle_name)s, last_name = %(last_name)s, salary = %(salary)s WHERE id = %(employee_id)s;"

        result = connectToMySQL("apr_employees").query_db(query, data)

        return result