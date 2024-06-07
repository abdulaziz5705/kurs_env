import os
import psycopg2 as psql
from dotenv import load_dotenv
load_dotenv()


class Database:
    @staticmethod
    def connect(query: str, query_type: str) -> str and list:
        db = psql.connect(
            database=os.getenv("db_database"),
            user=os.getenv("db_user"),
            password=os.getenv("db_password"),
            host=os.getenv("db_host"),
            port=os.getenv("db_port"),
        )
        cursor = db.cursor()

        cursor.execute(query)
        data = ["update",  "insert", "delete", "alter", "create"]
        if query_type in data:
            db.commit()
            return f"  successful"
        else:
            return cursor.fetchall()
