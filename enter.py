from login import login_page
from regester import regester_page


def login():
    l = input("""
    1.Login: 
    2.Regester
    >>>>""")
    if l == "1":
        return login_page()
    elif l == "2":
        return regester_page()
    else:
        print("Error")
        return login()


if __name__ == "__main__":
    login()
