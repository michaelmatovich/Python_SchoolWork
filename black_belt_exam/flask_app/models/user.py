from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

import re

from flask_app.models import band

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    schema_name = "band_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.bands_joined = []

    def get_bands_joined(self):
        query = "SELECT *, band_members.user_id AS bandmember from bands LEFT JOIN band_members ON bands.id = band_id LEFT JOIN users ON band_members.user_id = users.id;"

        records = connectToMySQL("band_schema").query_db(query)

        for record in records:
            band_joined = band.Band(record)

            if(record["bandmember"] == self.id):
                self.bands_joined.append(band_joined)

        return

    @classmethod
    def register_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"

        result = connectToMySQL(cls.schema_name).query_db(query, data)

        return result
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"

        result = connectToMySQL(cls.schema_name).query_db(query,data)

        if len(result) < 1:
            return False

        return cls(result[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"

        result = connectToMySQL(cls.schema_name).query_db(query,data)

        return cls(result[0])

    @classmethod
    def does_exist(cls,data):
        does_exist = True

        query = "SELECT * FROM users WHERE email = %(email)s;"

        result = connectToMySQL(cls.schema_name).query_db(query,data)

        if not result:
            does_exist = False

        return does_exist

    @classmethod
    def quit_band(cls, data):

        query = "DELETE FROM band_members WHERE user_id = %(user_id)s AND band_id = %(band_id)s;"

        result = connectToMySQL(cls.schema_name).query_db(query,data)

        return

    @classmethod
    def join_band(cls, data):

        query = "INSERT INTO band_members (user_id, band_id) VALUES (%(user_id)s, %(band_id)s);"

        result = connectToMySQL(cls.schema_name).query_db(query,data)

        return

    @staticmethod
    def validate_register(data):
        is_valid = True
        if len(data["first_name"]) < 2:
            flash("First name must be at least 2 characters long.")
            is_valid = False
        if len(data["last_name"]) < 2:
            flash("Last name must be at least 2 characters long.")
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
        if len(data["password"]) < 8:
            flash("Password must be at least 8 characters long.")
            is_valid = False
        if data["password"] != data["confirm_password"]:
            flash("Password must match Confirmation Password.")   
            is_valid = False
        return is_valid




