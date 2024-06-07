from main import Check
from online_kurs import kurs


def login_page():
    username = input("Username: ")
    password = input("Password: ")
    if Check.login_check(username, password):
        return kurs(username, password)
    else:
        print("<<<Login or password Error Please replay >>>")

        return login_page()

