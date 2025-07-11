from models.automobile import Automobile
from datetime import datetime
import random
from db.db import Db
import pandas as pd
ids = ["A001", "A002", "B789", "Z123", "CAR56", "X9Y8"]
names = ["Mustang", "Civic", "Model S", "Corolla", "F-150", "Chiron", "Outback"]
colors = ["Red", "Blue", "Black", "White", "Green", "Yellow", "Silver", "Gray"]
doorNumbers = [2, 3, 4, 5]
prices = [15000.0, 23000.99, 34999.95, 45000.75, 120000.0, 7999.5]
driverNames = ["Alice", "Bob", "Carlos", "Dana", "Eve", "Frank", "Grace"]
sizes = [4.2, 3.8, 5.0, 4.7, 4.0] 
weights = [1200.0, 1350.5, 1500.0, 1800.25, 2000.75, 1100.0] 
wheelNumbers = [3, 4, 6, 8] 
years = [1995, 2002, 2010, 2015, 2020, 2022, 2023, 2024]
brands = ["Ford", "Toyota", "Tesla", "Chevrolet", "BMW", "Audi", "Subaru", "Honda", "Bugatti"]
createdAts = [
    datetime(2023, 5, 10),
    datetime(2022, 3, 1),
    datetime(2020, 7, 15),
    datetime(2021, 12, 25),
    datetime(2024, 1, 1),
    datetime(2025, 6, 20)
]
parameters = {}
parameters['id'] = ids
parameters['name'] = names
parameters['color'] = colors
parameters['doorNumber'] = doorNumbers
parameters['price'] = prices
parameters['driverName'] = driverNames
parameters['size'] = sizes
parameters['weight'] = weights
parameters['wheelNumber'] = wheelNumbers
parameters['year'] = years
parameters['brand'] = brands
parameters['createdAt'] = createdAts

def createAutomobile()->Automobile:
    automobile = Automobile()
    for parameterName, parameterList in parameters.items():
        indx = random.randrange(0,len(parameterList))
        setattr(automobile, parameterName, parameterList[indx])
    return automobile

def createAutomobileList()->list[Automobile]:
    automobileList = []
    for i in range(100):
        automobileList.append(createAutomobile())
    return automobileList

def insertAutomobile(automobile:Automobile,db:Db)->Automobile:
    return db.insertAutomobile(automobile)
    
def insertAutomobileList(automobileList:list[Automobile],db:Db):
    newAutomobileList = []
    for automobile in automobileList:
        newAutomobileList.append(insertAutomobile(automobile, db))
    return newAutomobileList

def getAutomobileList(db:Db)->pd.DataFrame:
    return db.getAllAutomobileDF()

def createMocks():
    db = Db()
    automobileList = createAutomobileList()
    insertAutomobileList(automobileList, db)
    df = getAutomobileList(db)
    print(df.head())

