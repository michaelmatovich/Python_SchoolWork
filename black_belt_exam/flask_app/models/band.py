from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

from flask_app.models import user

class Band:
    schema_name = "band_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.genre = data["genre"]
        self.city = data["city"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.founder = {}
        self.members = []


    @staticmethod
    def validate_band(data):
        is_valid = True
        if len(data["name"]) < 2:
            flash("Name must be at least 2 characters long.")
            is_valid = False
        if len(data["genre"]) < 2:
            flash("Music genre must be at least 2 characters long.")
            is_valid = False
        if len(data["city"]) < 1:
            flash("Please enter a home city.")   
            is_valid = False
        return is_valid

    @classmethod
    def new_band(cls, data):
        query = "INSERT INTO bands (name, genre, city, user_id) VALUES (%(name)s, %(genre)s, %(city)s, %(user_id)s);"

        result = connectToMySQL(cls.schema_name).query_db(query, data)

        return result

    @classmethod
    def get_bandmembers(cls, data):

        query = "SELECT * from bands LEFT JOIN band_members ON bands.id = band_id LEFT JOIN users ON band_members.user_id = users.id;"
        
        records = connectToMySQL(cls.schema_name).query_db(query)

        all_bands = []
    
        logged_user_id = data["user_id"]

        for record in records:
            band = Band(record)
            
            user_data = {
                "id": record["users.id"],
                "first_name": record["first_name"],
                "last_name": record["last_name"],
                "email": record["email"],
                "password": record["password"],
                "created_at": record["users.created_at"],
                "updated_at": record["users.updated_at"]            
            }
            band_member_data = {
                "user_id": record["band_members.user_id"],
                "band_id": record["band_id"]
            }

            band.founder = user.User(user_data)

            if(logged_user_id == band_member_data["user_id"]):

                band.members.append(logged_user_id)            

            all_bands.append(band)

        return all_bands
    
    @classmethod
    def get_all_bands(cls):
        query = "SELECT * FROM bands LEFT JOIN users ON user_id = users.id;"
        
        records = connectToMySQL(cls.schema_name).query_db(query)

        all_bands = []
    
        for record in records:
            band = Band(record)
            
            user_data = {
                "id": record["users.id"],
                "first_name": record["first_name"],
                "last_name": record["last_name"],
                "email": record["email"],
                "password": record["password"],
                "created_at": record["users.created_at"],
                "updated_at": record["users.updated_at"]            
            }

            band.founder = user.User(user_data)

            all_bands.append(band)

        return all_bands

    @classmethod
    def get_my_bands(cls, data):
        query = "SELECT * FROM bands WHERE user_id = %(user_id)s;"

        records = connectToMySQL(cls.schema_name).query_db(query, data)

        return records

    @classmethod
    def get_one_band(cls, data):
        query = "SELECT * FROM bands WHERE id = %(id)s"

        record = connectToMySQL(cls.schema_name).query_db(query, data)

        return cls(record[0])

    @classmethod
    def edit_band(cls, data):
        query = "UPDATE bands SET name = %(name)s, genre = %(genre)s, city = %(city)s WHERE id = %(id)s;"

        result = connectToMySQL(cls.schema_name).query_db(query, data)
        
        return

    @classmethod
    def delete_band(cls, data):
        query = "DELETE FROM band_members WHERE band_id = %(id)s;"
        
        result = connectToMySQL(cls.schema_name).query_db(query, data)

        query = "DELETE FROM bands WHERE id = %(id)s;"

        result = connectToMySQL(cls.schema_name).query_db(query, data)

        return
    
    @classmethod
    def get_bands_joined(cls):
        query = "SELECT * from bands LEFT JOIN band_members ON bands.id = band_id LEFT JOIN users ON band_members.user_id = users.id;"

        records = connectToMySQL(cls.schema_name).query_db(query, data)

        user = user.User({"user_id": session["user_id"]})
        
        for record in records:
            band = Band(record)

            if(band_members.user_id == user.id):
                user.bands_joined.append(band)

        return user


