from regester_check import Foydalanuvchi
from login import login_page


def regester_page():
    print("<<<<<Register Page>>>>")
    first_name: str = input("Ismingizni kiriting: ")
    last_name: str = input("Familiyangizni kiriting: ")
    age: str = input("Yoshingizni kiriting: ")
    phone: str = input("Telefon nomer kiriting: ")
    username: str = input("Username kiriting: ")
    password: str = input("Passwordni kiriting: ")
    password1: str = input("Passwordni qaytadan kiriting: ")
    while password != password1:
        print("Password moskelmadi qayta urinib kuring!")
        password: str = input("Passwordni kiriting: ")
        password1: str = input("Passwordni qaytadan kiriting: ")
    print(Foydalanuvchi.regester(first_name, last_name, age, phone, username, password))
    return login_page()
