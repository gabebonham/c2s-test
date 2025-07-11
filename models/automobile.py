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
    def to_dict_pt(self)->dict:
        return {
            'id': self.id,
            'nome': self.name,
            'cor': self.color,
            'portas': self.doorNumber,
            'preço': str(self.price),
            'motorista': self.driverName,
            'tamanho': str(self.size),
            'peso': str(self.weight),
            'rodas': self.wheelNumber,
            'ano': self.year,
            'marca': self.brand,
            'criado': self.createdAt.isoformat() if hasattr(self.createdAt, 'isoformat') else str(self.createdAt)
        }