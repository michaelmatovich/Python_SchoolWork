from flask_app.config.mysqlconnection import connectToMySQL

class User():

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"

        records = connectToMySQL("users_schema").query_db(query)

        users = []

        for record in records:
            users.append(User(record))

        return users

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"

        result = connectToMySQL("users_schema").query_db(query, data)

        return result

    @classmethod
    def delete_user(cls, data):
        query = 'DELETE FROM users WHERE id = %(user_id)s;'

        connectToMySQL("users_schema").query_db(query, data)

    @classmethod
    def get_one_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        user = []
        result = connectToMySQL("users_schema").query_db(query, data)
        user.append(User(result[0]))
        return user

    @classmethod
    def edit_user(cls, data):
        
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(user_id)s;"
        # query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        
        result = connectToMySQL("users_schema").query_db(query, data)

        return result





