import online_kurs
from manager import Database


def marketing(username, password):
    web = input("""
    1.SMM
    2.Monilografiya
    0.Back
    >>>""")
    if web == "1":
        query = f"SELECT * FROM course WHERE id=8"
        data = Database.connect(query, "select")
        for i in data:
            print(f"""
                          Id: {i[0]}
                          Name: {i[1]}
                          Description: {i[2]}
                          Modullar soni: {i[3]} ta
                          Mavzular soni: {i[4]} ta
                          Darslar soni: {i[5]} ta
                          Dars vaqti: {i[6]} soat 
                          Mentor: {i[7]}
                          Price: {i[8]} sum 
                          """)
        return marketing(username, password)
    elif web == "2":
        query = f"SELECT * FROM course WHERE id=9"
        data = Database.connect(query, "select")
        for i in data:
            print(f"""
                          Id: {i[0]}
                          Name: {i[1]}
                          Description: {i[2]}
                          Modullar soni: {i[3]} ta
                          Mavzular soni: {i[4]} ta
                          Darslar soni: {i[5]} ta
                          Dars vaqti: {i[6]} soat 
                          Mentor: {i[7]}
                          Price: {i[8]} sum 
                          """)
        return marketing(username, password)
    elif web == "0":
        return dasturlash(username, password)
    else:
        print("Error")
        return marketing(username, password)


def dizayn(username, password):
    web = input("""
    1.SMD
    0.Back
     >>>""")
    if web == "1":
        query = f"SELECT * FROM course WHERE id=7"
        data = Database.connect(query, "select")
        for i in data:
            print(f"""
                  Id: {i[0]}
                  Name: {i[1]}
                  Description: {i[2]}
                  Modullar soni: {i[3]} ta
                  Mavzular soni: {i[4]} ta
                  Darslar soni: {i[5]} ta
                  Dars vaqti: {i[6]} soat 
                  Mentor: {i[7]}
                  Price: {i[8]} sum 
                  """)
        return dizayn(username, password)
    elif web == "0":
        return dasturlash(username, password)
    else:
        print("Error")
        return course(username, password)


def dasturlash(username, password):
    web = input("""
    1.Python
    2.Note JS
    3.Flutter
    0.Back
    >>>>>""")
    if web == "1":
        query = f"SELECT * FROM course WHERE id=4"
        data = Database.connect(query, "select")
        for i in data:
            print(f"""
            Id: {i[0]}
            Name: {i[1]}
            Description: {i[2]}
            Modullar soni: {i[3]} ta
            Mavzular soni: {i[4]} ta
            Darslar soni: {i[5]} ta
            Dars vaqti: {i[6]} soat 
            Mentor: {i[7]}
            Price: {i[8]} sum 
            """)
        return dasturlash(username, password)
    elif web == "2":
        query = f"SELECT * FROM course WHERE id=5"
        data = Database.connect(query, "select")
        for i in data:
            print(f"""
                    Id: {i[0]}
                    Name: {i[1]}
                    Description: {i[2]}
                    Modullar soni: {i[3]} ta
                    Mavzular soni: {i[4]} ta
                    Darslar soni: {i[5]} ta
                    Dars vaqti: {i[6]} soat 
                    Mentor: {i[7]}
                    Price: {i[8]} sum 
                    """)
        return dasturlash(username, password)

    elif web == "3":
        query = f"SELECT * FROM course WHERE id=6"
        data = Database.connect(query, "select")
        for i in data:
            print(f"""
                          Id: {i[0]}
                          Name: {i[1]}
                          Description: {i[2]}
                          Modullar soni: {i[3]} ta
                          Mavzular soni: {i[4]} ta
                          Darslar soni: {i[5]} ta
                          Dars vaqti: {i[6]} soat 
                          Mentor: {i[7]}
                          Price: {i[8]} sum 
                          """)
        return dasturlash(username, password)
    elif web == "0":
        return course(username, password)


def course(username, password):
    kurs = input("""
    1.Dasturlash
    2.Dizayn
    3.Marketing
    0.Back
    >>>>""")
    if kurs == "1":
        return dasturlash(username, password)
    elif kurs == "2":
        return dizayn(username, password)
    elif kurs == "3":
        return marketing(username, password)
    elif kurs == "0":
        return online_kurs.kurs(username, password)
    else:
        print("Error")
        return course(username, password)
