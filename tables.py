from manager import Database


def create_table():
    country = f"""
         CREATE TABLE  country(
            id SERIAL PRIMARY KEY,
            name VARCHAR(100));
             """
    city = f"""
        CREATE TABLE city(
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            country_id INT REFERENCES country(id));"""
    category = f"""
        CREATE TABLE category(
            id SERIAL PRIMARY KEY,
            name VARCHAR(100));
    """
    student = f"""
        CREATE TABLE student(
          id SERIAL PRIMARY KEY,
          name VARCHAR(100),
          last_name VARCHAR(50),
          age INT,
          phone_number BIGINT,
          username VARCHAR,
          country_id INT REFERENCES country(id),
          city_id INT REFERENCES city(id),
          create_date TIMESTAMP DEFAULT now());
    """
    name_course = f"""
        CREATE TABLE name_cource(
            id SERIAL PRIMARY KEY,
            category_id INT REFERENCES category(id),
            course_id INT REFERENCES course(id),
            create_date TIMESTAMP DEFAULT now());
    """
    course = f"""
        CREATE TABLE course(
             id SERIAL PRIMARY KEY,
             name VARCHAR(100),
             description VARCHAR,
             modullar_soni INT,
             mavzular_soni INT,
             darslar_soni INT,
             dars_vaqti VARCHAR(50),
             mentor VARCHAR(100),
             price FLOAT,
             category_id INT REFERENCES category(id),
             name_cource_id INT REFERENCES name_cource(id),
             craete_date TIMESTAMP DEFAULT now());
    """

    data = {"country": country, "city": city, "category": category, "student": student, "name_course": name_course,
            "course": course}
    for i in data:
        print(f"{i} {Database.connect(data[i], "create")}")


if __name__ == '__main__':
    create_table()
