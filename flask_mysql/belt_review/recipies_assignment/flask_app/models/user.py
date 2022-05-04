from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

from flask_app.models import recipe

import re



EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
TEXT_REGEX = re.compile(r'^[a-zA-Z]+$')


class User:
    database = "recipies_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.recipies = []

    def get_user_recipies(self,data):
        query = "SELECT * FROM recipies WHERE user_id = %(user_id)s;"

        results = connectToMySQL(User.database).query_db(query,data)

        for result in results:
            self.recipies.append(result)

        if not results:
            return False
        return True 

    @classmethod
    def register_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"

        result = connectToMySQL(User.database).query_db(query, data)

        return result
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"

        result = connectToMySQL(User.database).query_db(query,data)

        if len(result) < 1:
            return False
        
        return cls(result[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"

        result = connectToMySQL(User.database).query_db(query,data)

        return cls(result[0])

    @classmethod
    def does_exist(cls,data):
        does_exist = True

        query = "SELECT * FROM users WHERE email = %(email)s;"

        result = connectToMySQL(User.database).query_db(query,data)

        if not result:
            does_exist = False

        return does_exist

    @staticmethod
    def validate_register(data):
        is_valid = True
        if len(data["first_name"]) < 2:
            flash("First name must be at least 2 characters long.")
            is_valid = False
        elif not TEXT_REGEX.match(data["first_name"]):
            flash("First name must be letters only.")
            is_valid = False
        if len(data["last_name"]) < 2:
            flash("Last name must be at least 2 characters long.")
            is_valid = False
        elif not TEXT_REGEX.match(data["first_name"]):
            flash("Last name must be letters only.")
            is_valid = False
        if len(data["email"]) < 1:
            flash("Email address must be present.")
            is_valid = False
        elif not EMAIL_REGEX.match(data["email"]):
            flash("Please enter a valid email address.")
            is_valid = False
        if User.does_exist({"email": data["email"]}) == True:
            flash("This email address is already registered.")
            is_valid = False 
        if len(data["password"]) < 9:
            flash("Password must be at least 8 characters long.")
            is_valid = False
        if data["password"] != data["confirm_password"]:
            flash("Password must match Confirmation Password.")   
            is_valid = False
        return is_valid
