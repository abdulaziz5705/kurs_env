from course import course
from classes import Course
from main import Save


def kurs(username, password):
    cource = input("""
    1.Kurslarni ko'rish
    2.Search
    3.Account
    0.Back
    >>>>""")
    if cource == "1":
        return course(username, password)
    elif cource == "2":

        name = input("Search: ")
        data = Course.search(name)
        for i in data:
            print(f"""
                               Id: {i[0]}
                               Name: {i[1]}
                               Price: {i[2]}
                               Count: {i[3]}
                               Start date: {i[4]}
                               End date:  {i[5]}
                               Star count:  {i[6]}
                               Serial number:  {i[7]}
                               Store id:  {i[8]}
                               Category id: {i[9]}
                               """)
            return kurs(username, password)

        return Course.search(name)

    elif cource == "3":
        return account(username, password)
    else:
        print("Error")
        return kurs(username, password)


@staticmethod
def account(username, password):
    web = input("""
    1.My personal info
    2.Update
    3.Log out 
    >>>>>""")
    if web == "1":
        query = f"SELECT * FROM foydalanuvchi WHERE username='{username}' and password='{password}' "
        data = Save.connect(query, "select")
        for i in data:
            print(f"""
                Id: {i[6]}
                Name: {i[0]}
                Last name: {i[1]}
                Age: {i[2]}
                Phone number: {i[3]}
                Username: {i[4]}
                Password: {i[5]}
                """)
        return account(username, password)
    elif web == "2":
        column = input("Column name: ")
        new_name = input("New name: ")
        old_name = input("Old_name: ")
        print(Foydalanuvchi.update(column, new_name, old_name))
        return account(username, password)

    elif web == "3":
        query = f"DELETE FROM foydalanuvchi WHERE username='{username}' and password='{password}'"
        print("Siz  ")
        return Save.connect(query, "delete")

    elif web == "3":
        return kurs(username, password)
    elif web == "0":
        return kurs(username, password)
    else:
        print("Error")
        return account(username, password)


class Foydalanuvchi:


    @staticmethod
    def update(column, new_name, old_name):
        if column == "id":
            query = f"Update foydalanuvchi SET {column} = {new_name} WHERE {column} = {old_name}"
        else:
            query = f"Update foydalanuvchi SET {column} = '{new_name}' WHERE {column} = '{old_name}'"
        return Save.connect(query, "update")
