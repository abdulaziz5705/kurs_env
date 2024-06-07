from classes import Country
from classes import Category
from classes import Name
from classes import Course
from classes import City
from classes import Student


def country_table():
    service = input("""
        1.Select
        2.Insert
        3.Update
        4.Delete
        0.Back
        >>>>""")
    if service == "1":
        Country.select()
        back = input("""
        0.Back
    >>>""")
        if back == "0":
            return country_table()
        else:
            print("Error")
            return country_table()

    elif service == "2":
        name = input("Name: ")
        print(Country.insert(name))
        return country_table()
    elif service == "3":
        column = input("Column name: ")
        new_name = input("New name: ")
        old_name = input("Old_name: ")
        print(Country.update(column, new_name, old_name))
        return country_table()
    elif service == "4":
        column = input("Column name: ")
        name = input("Row name: ")
        print(Country.delete(column, name))
        return country_table()
    elif service == "0":
        return section()


def category_table():
    service = input("""
           1.Select
           2.Insert
           3.Update
           4.Delete
           0.Back
           >>>>""")
    if service == "1":
        Category.select()
        back = input("""
              0.Back
          >>>""")
        if back == "0":
            return category_table()
        else:
            print("Error")
            return category_table()
    elif service == "2":
        name = input("Name: ")
        print(Category.insert(name))
        return category_table()
    elif service == "3":
        column = input("Column name: ")
        new_name = input("New name: ")
        old_name = input("Old_name: ")
        print(Category.update(column, new_name, old_name))
        return category_table()
    elif service == "4":
        column = input("Column name: ")
        name = input("Row name: ")
        print(Category.delete(column, name))
        return category_table()
    elif service == "0":
        return section()


def city_table():
    service = input("""
              1.Select
              2.Insert
              3.Update
              4.Delete
              0.Back
              >>>>""")
    if service == "1":
        City.select()
        back = input("""
                 0.Back
             >>>""")
        if back == "0":
            return city_table()
        else:
            print("Error")
            return city_table()
    elif service == "2":
        name = input("Name: ")
        country_id = input("Country_id: ")
        print(City.insert(name, country_id))
        return city_table()
    elif service == "3":
        column = input("Column name: ")
        new_name = input("New name: ")
        old_name = input("Old_name: ")
        print(City.update(column, new_name, old_name))
        return city_table()
    elif service == "4":
        column = input("Column name: ")
        name = input("Row name: ")
        print(City.delete(column, name))
        return city_table()
    elif service == "0":
        return section()


def course_table():
    service = input("""
                      1.Select
                      2.Insert
                      3.Update
                      4.Delete
                      0.Back
                      >>>>""")
    if service == "1":
        Course.select()
        back = input("""
                         0.Back
                     >>>""")
        if back == "0":
            return course_table()
        else:
            print("Error")
            return course_table()
    elif service == "2":
        name = input("Name: ")
        description = input("Description: ")
        modullar = input("Modullar soni: ")
        mavzular = input("Mavzular soni: ")
        darslar = input("Darslar soni: ")
        dars = input("Dars vaqti: ")
        metor = input("Mentor: ")
        price = input("Price: ")
        category_id = input("Category_id: ")
        print(Course.insert(name, description, modullar, mavzular, darslar, dars, metor, price, category_id))
        return course_table()
    elif service == "3":
        column = input("Column name: ")
        new_name = input("New name: ")
        old_name = input("Old_name: ")
        print(Course.update(column, new_name, old_name))
        return course_table()
    elif service == "4":
        column = input("Column name: ")
        name = input("Row name: ")
        print(Course.delete(column, name))
        return course_table()
    elif service == "0":
        return section()


def name_table():
    service = input("""
                  1.Select
                  2.Insert
                  3.Update
                  4.Delete
                  0.Back
                  >>>>""")
    if service == "1":
        Name.select()
        back = input("""
                     0.Back
                 >>>""")
        if back == "0":
            return name_table()
        else:
            print("Error")
            return name_table()
    elif service == "2":
        name = input("Name: ")
        category_id = input("Category_id: ")
        course_id = input("Course_id: ")
        print(Name.insert(name, category_id, course_id))
        return name_table()
    elif service == "3":
        column = input("Column name: ")
        new_name = input("New name: ")
        old_name = input("Old_name: ")
        print(Name.update(column, new_name, old_name))
        return name_table()
    elif service == "4":
        column = input("Column name: ")
        name = input("Row name: ")
        print(Name.delete(column, name))
        return name_table()
    elif service == "0":
        return section()


def student_table():
    service = input("""
                   1.Select
                   2.Insert
                   3.Update
                   4.Delete
                   0.Back
                   >>>>""")
    if service == "1":
        Student.select()
        back = input("""
                      0.Back
                  >>>""")
        if back == "0":
            return student_table()
        else:
            print("Error")
            return student_table()
    elif service == "2":
        name = input("Name: ")
        last_name = input("Last_name: ")
        age = input("Age: ")
        phone_number = input("Phone_number: ")
        username = input("Username: ")
        country_id = input("Country_id: ")
        city_id = input("City_id: ")
        print(Student.insert(name, last_name, age, phone_number, username, country_id, city_id))
        return student_table()
    elif service == "3":
        column = input("Column name: ")
        new_name = input("New name: ")
        old_name = input("Old_name: ")
        print(Student.update(column, new_name, old_name))
        return student_table()
    elif service == "4":
        column = input("Column name: ")
        name = input("Row name: ")
        print(Student.delete(column, name))
        return student_table()
    elif service == "0":
        return section()


def section():
    "Bu bulimda siz ma'lumotlarni o'zgartirishingiz mumkun va foydalanuvchilar sonini kurishingiz mumkun"
    web = input("""
        1.Country
        2.City
        3.Category
        4.Course
        5.Name course
        6.Student
        >>>>""")
    if web == "1":
        return country_table()
    elif web == "2":
        return city_table()
    elif web == "3":
        return category_table()
    elif web == "4":
        return course_table()
    elif web == "5":
        return name_table()
    elif web == "6":
        return student_table()
    else:
        print("Error")
        return section()


if __name__ == "__main__":
    section()
