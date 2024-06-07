from manager import Database


class Country:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def select():
        query = "SELECT * FROM country ORDER BY id"
        data = (Database.connect(query, "select"))
        for i in data:
            print(f"""
            Id: {i[0]}
            Name: {i[1]}
            """)

    @staticmethod
    def insert(name):
        query = f"INSERT INTO country(name) VALUES ('{name}')"
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_name, old_name):
        if column == "id":
            query = f"Update country SET {column} = {new_name} WHERE {column} = {old_name}"
        else:
            query = f"Update country SET {column} = '{new_name}' WHERE {column} = '{old_name}'"
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, name):
        if column == "id":
            query = f"DELETE FROM country WHERE {column} = {name} "
        else:
            query = f"DELETE FROM country WHERE {column} = '{name}' "
        return Database.connect(query, "delete")


class City:
    def __init__(self, name, country_id):
        self.name = name
        self.country_id = country_id

    @staticmethod
    def select():
        query = f"SELECT c.name, k.name as CountryId FROM  city c INNER JOIN  country k ON c.country_id=k.id"
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    @staticmethod
    def insert(name, country_id):
        query = f"INSERT INTO city(name, country_id) VALUES ('{name}',{country_id})"
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_name, old_name):
        if column == "id":
            query = f"Update city SET {column} = {new_name} WHERE {column} = {old_name}"
        else:
            query = f"Update city SET {column} = '{new_name}' WHERE {column} = '{old_name}'"
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, name):
        if column == "id":
            query = f"DELETE FROM city WHERE {column} = {name} "

        else:
            query = f"DELETE FROM city WHERE {column} = '{name}' "
        return Database.connect(query, "delete")


class Category:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def select():
        query = "SELECT * FROM category ORDER BY id"
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    @staticmethod
    def insert(name):
        query = f"INSERT INTO category (name) VALUES ('{name}')"
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_name, old_name):
        if column == "id":
            query = f"Update category SET {column} = {new_name} WHERE {column} = {old_name}"
        else:
            query = f"Update category SET {column} = '{new_name}' WHERE {column} = '{old_name}'"
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, name):
        if column == "id":
            query = f"DELETE FROM category WHERE {column} = {name} "
        else:
            query = f"DELETE FROM category WHERE {column} = '{name}' "
        return Database.connect(query, "delete")


class Course:
    def __init__(self, name, description, modullar_soni, mavzular_soni, darslar_soni, dars_vaqti, mentor, price,
                 category_id):
        self.name = name
        self.description = description
        self.madullar = modullar_soni
        self.mavzular = mavzular_soni
        self.darslar = darslar_soni
        self.dars = dars_vaqti
        self.menthor = mentor
        self.price = price
        self.category_id = category_id

    @staticmethod
    def select():
        query = "SELECT c.name, c.description, c.modullar_soni, c.mavzular_soni, c.darslar_soni, c.dars_vaqti, c.mentor, c.price, c.category_id, s.name as CategoryId FROM course c INNER JOIN category s ON c.category_id=s.id "
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    @staticmethod
    def insert(name, description, modullar_soni, mavzular_soni, darslar_soni, dars_vaqti, mentor, price, category_id):
        query = f"INSERT INTO course (name, description, modullar_soni, mavzular_soni, darslar_soni, dars_vaqti, mentor, price, category_id) VALUES ('{name}', '{description}', {modullar_soni}, {mavzular_soni}, {darslar_soni}, {dars_vaqti}, '{mentor}', {price}, {category_id})"
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_name, old_name):
        if column == "id":
            query = f"Update course SET {column} = {new_name} WHERE {column} = {old_name}"
        else:
            query = f"Update course SET {column} = '{new_name}' WHERE {column} = '{old_name}'"
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, name):
        if column == "id":
            query = f"DELETE FROM cource WHERE {column} = {name} "

        else:
            query = f"DELETE FROM course WHERE {column} = '{name}' "
        return Database.connect(query, "delete")

    @staticmethod
    def search(name):
        query = (
            f" SELECT * FROM course WHERE name LIKE '%{name}%'")
        return Database.connect(query, "select")


class Name:
    def __init__(self, name, category_id, course_id):
        self.name = name
        self.category_id = category_id
        self.course_id = course_id

    @staticmethod
    def select():
        query = "SELECT n.name, c.name as CategoryId, s.name as CourceId FROM name_cource n INNER JOIN  category c ON n.category_id=c.id INNER JOIN course s ON n.course_id=s.id"
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    @staticmethod
    def insert(name, category_id, course_id):
        query = f"INSERT INTO name_cource(name, category_id, course_id) VALUES ('{name}', {category_id}, {course_id})"
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_name, old_name):
        if column == "id":
            query = f"Update name_cource SET {column} = {new_name} WHERE {column} = {old_name}"
        else:
            query = f"Update name_cource SET {column} = '{new_name}' WHERE {column} = '{old_name}'"
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, name):
        if column == "id":
            query = f"DELETE FROM name_cource WHERE {column} = {name} "

        else:
            query = f"DELETE FROM name_cource WHERE {column} = '{name}' "
        return Database.connect(query, "delete")


class Student:
    def __init__(self, name, last_name, age, phone_number, username, country_id, city_id):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.phone_number = phone_number
        self.username = username
        self.country_id = country_id
        self.city_id = city_id

    @staticmethod
    def select():
        query = "SELECT s.name, s.last_name, s.age, s.phone_number, s.username, c.name, t.name FROM student s INNER JOIN country c ON s.country_id=c.id INNER JOIN city t ON s.city_id=t.id"
        data = Database.connect(query, "select")
        for i in data:
            print(f"""
            Name: {i[0]}
            Last name: {i[1]}
            Age: {i[2]}
            Phone number: {i[3]}
            Username: {i[4]}
            Country : {i[5]}
            City : {i[6]}
           
            """)

    @staticmethod
    def insert(name, last_name, age, phone_number, username, country_id, city_id):
        query = f"INSERT INTO student(name, last_name, age, phone_number, username, country_id, city_id) VALUES ('{name}','{last_name}', {age}, {phone_number}, '{username}', {country_id}, {city_id})"
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_name, old_name):
        if column == "id":
            query = f"Update student SET {column} = {new_name} WHERE {column} = {old_name}"
        else:
            query = f"Update student SET {column} = '{new_name}' WHERE {column} = '{old_name}'"
        return Database.connect(query, "update")

    @staticmethod
    def delete(column, name):
        if column == "id":
            query = f"DELETE FROM student WHERE {column} = {name} "

        else:
            query = f"DELETE FROM student WHERE {column} = '{name}' "
        return Database.connect(query, "delete")

