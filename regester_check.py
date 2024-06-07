from main import Save


class Foydalanuvchi:

    def __init__(self, first_name, last_name, age, phone_number, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.username = username
        self.password = password

    @staticmethod
    def regester(first_name, last_name, age, phone_number, username, password):
        query = f"INSERT INTO foydalanuvchi(first_name, last_name, age, phone_number, username, password) VALUES ('{first_name}', '{last_name}',{age}, {phone_number}, '{username}','{password}')"
        return Save.connect(query, "insert")
