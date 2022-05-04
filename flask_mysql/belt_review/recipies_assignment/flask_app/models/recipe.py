from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import user

import re

from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
TEXT_REGEX = re.compile(r'^[a-zA-Z]+$')


class Recipe:
    database = "recipies_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instruction = data["instruction"]
        self.is_under_30 = data["is_under_30"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all_recipies(cls, data):

        query = "SELECT * from recipies;"

        results = connectToMySQL(Recipe.database).query_db(query, data)

        return results

    @classmethod
    def create_recipe(cls, data):

        query = "INSERT INTO recipies (name, description, instruction, is_under_30, user_id) VALUES (%(name)s, %(description)s, %(instruction)s, %(is_under_30)s, %(user_id)s);"

        results = connectToMySQL(Recipe.database).query_db(query, data)

        return results

    @classmethod
    def get_by_id(cls, data):

        query = "SELECT * FROM recipies where id = %(id)s;"

        result = connectToMySQL(Recipe.database).query_db(query, data)

        return cls(result[0])

    @classmethod
    def edit_recipe(cls, data):

        query = "UPDATE recipies SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, is_under_30 = %(is_under_30)s WHERE id = %(id)s;"
    
        result = connectToMySQL(Recipe.database).query_db(query, data)

        return result

    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data["name"]) < 4:
            flash("Name must be at least 3 characters long.")
            is_valid = False
        if len(data["description"]) < 4:
            flash("Description must be at least 3 characters long.")
            is_valid = False
        if len(data["instruction"]) < 4:
            flash("Instructions must be at least 3 characters long.")
            is_valid = False
        if not data["created_at"]:
            flash("Please enter the date the recipe was created.")
            is_valid = False
        if not data["is_under_30"]:
            flash("Please indicate whether under 30 minutes or not.")   
            is_valid = False
        return is_valid




