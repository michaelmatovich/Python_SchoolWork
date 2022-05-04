from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Show:
    schema_name = "tv_shows_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.network = data["network"]
        self.release_date = data["date"]
        self.description = data["description"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.posted_by = {}

    @staticmethod
    def validate_show(data):
        is_valid = True
        if len(data["title"]) < 3:
            flash("Title must be at least 3 characters long.")
            is_valid = False
        if len(data["network"]) < 3:
            flash("Network must be at least 3 characters long.")
            is_valid = False
        if not data["release_date"]:
            flash("Please enter the release date.")
            is_valid = False
        if len(data["description"]) < 4:
            flash("Description must be ast least 3 characters long.")   
            is_valid = False
        return is_valid

    @classmethod
    def new_show(cls, data):
        query = "INSERT INTO tv_shows (title, network, release_date, description, user_id) VALUES (%(title)s, %(network)s, %(release_date)s, %(description)s, %(user_id)s);"

        result = connectToMySQL(cls.schema_name).query_db(query, data)

        return result

    @classmethod
    def get_all_shows(cls):
        # query = "SELECT * from tv_shows LEFT JOIN users ON user_id = users.id;"
        query = "SELECT *, DATE_FORMAT(release_date, '%M %d %Y') AS date from tv_shows LEFT JOIN users ON user_id = users.id;"

        result = connectToMySQL(cls.schema_name).query_db(query)

        return result

    @classmethod
    def get_one_show(cls, data):
        query = "SELECT *, release_date AS date from tv_shows LEFT JOIN users ON user_id = users.id WHERE tv_shows.id = %(id)s;"

        result = connectToMySQL(cls.schema_name).query_db(query, data)

        return result

    @classmethod
    def edit_show(cls, data):
        query = "UPDATE tv_shows SET title = %(title)s, network = %(network)s, release_date = %(release_date)s, description = %(description)s WHERE id = %(id)s;"

        result = connectToMySQL(cls.schema_name).query_db(query, data)
        
        return

    @classmethod
    def delete_show(cls, data):
        query = "DELETE FROM tv_shows WHERE id = %(id)s;"

        result = connectToMySQL(cls.schema_name).query_db(query, data)

        return