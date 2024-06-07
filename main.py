import os
import psycopg2 as psql
from dotenv import load_dotenv
load_dotenv()

class Save:
    @staticmethod
    def connect(query: str, query_type: str) -> str and list:
        db = psql.connect(
            database=os.getenv("db_database"),
            user=os.getenv("db_user"),
            password=os.getenv("db_password"),
            host=os.getenv("db_host"),
            port=os.getenv("db_port")
        )
        cursor = db.cursor()

        cursor.execute(query)
        data = ["update", "insert", "delete", "alter", "create"]
        if query_type in data:
            db.commit()
            return """  
                     sizning ma'lumotlaringiz muvofaqiyatli saqlandi 
                      """
        else:
            return cursor.fetchall()


class Check:
    @staticmethod
    def login_check(username: str, password: str):
        query = f"SELECT * FROM foydalanuvchi WHERE username = '{username}' and password = '{password}'"
        data = Save.connect(query, "select")
        if len(data) == 1:
            return True
        else:
            return False
