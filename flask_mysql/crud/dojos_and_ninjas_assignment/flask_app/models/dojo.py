from flask_app.config.mysqlconnection import connectToMySQL

class Dojo():

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"

        records = connectToMySQL("dojos_and_ninjas_schema").query_db(query)

        dojos = []

        for record in records:
            dojos.append(Dojo(record))

        return dojos

    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"

        result = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

        return result

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(dojos_id)s;"

        result = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

        dojo = result[0]

        return dojo

    @classmethod
    def get_dojo_ninjas(cls,data):
        query = "SELECT * FROM ninjas where dojos_id = %(dojos_id)s;"

        result = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

        return result

class Ninja():

    def __init__(self,date):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojos_id = data['dojos_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojos_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojos_id)s);"

        result = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

        return result

