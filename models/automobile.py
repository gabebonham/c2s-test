from datetime import datetime
class Automobile:
    def __init__(self,
                id: str = None,
                 name: str = None,
                 color: str = None,
                 doorNumber: int = None,
                 price: float = None,
                 driverName: str = None,
                 size: float = None,
                 weight: float = None,
                 wheelNumber: int = None,
                 year: int = None,
                 brand: str = None,
                 createdAt: datetime = None):
        self.id = id
        self.name = name
        self.color = color
        self.doorNumber = doorNumber
        self.price = price
        self.driverName = driverName
        self.size = size
        self.weight = weight
        self.wheelNumber = wheelNumber
        self.year = year
        self.brand = brand
        self.createdAt = createdAt
        pass