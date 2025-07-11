import psycopg2
from datetime import datetime
from models.automobile import Automobile
import pandas as pd

class Db:
    def __init__(self):
        self.DB_HOST = "localhost"
        self.DB_PORT = "5432"
        self.DB_NAME = "c2sdb"
        self.DB_USER = "automobile_user"
        self.DB_PASS = "TaEaDWkczafQT@SG"
        self.insert_query = """
            INSERT INTO automobile (
                id, name, color, door_number, price, driver_name,
                size, weight, wheel_number, year, brand, created_at
            )
            VALUES (
                uuid_generate_v4(), %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s
            )
        """
        self.select_query = "SELECT * FROM automobile;"
        pass
    
    def getAllAutomobileDF(self) -> pd.DataFrame:
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(self.select_query)

        columns = [desc[0] for desc in cursor.description]

        rows = cursor.fetchall()

        df = pd.DataFrame(rows, columns=columns)

        cursor.close()
        connection.close()
        return df
    
    def connect(self):
        return psycopg2.connect(
            host=self.DB_HOST,
            port=self.DB_PORT,
            dbname=self.DB_NAME,
            user=self.DB_USER,
            password=self.DB_PASS
        )
        
    def insertAutomobile(self,automobile:Automobile)->Automobile:
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute(self.insert_query, (
            automobile.name,
            automobile.color,
            automobile.doorNumber,
            automobile.price,
            automobile.driverName,
            automobile.size,
            automobile.weight,
            automobile.wheelNumber,
            automobile.year,
            automobile.brand,
            automobile.createdAt
        ))
        connection.commit()
        cursor.close()
        connection.close()
        return automobile

