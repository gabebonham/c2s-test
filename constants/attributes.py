def getAttributes()->list[str]:
    attributes = []
    attributes.append('id')
    attributes.append('name')
    attributes.append('color')
    attributes.append('doorNumber')
    attributes.append('price')
    attributes.append('driverName')
    attributes.append('size')
    attributes.append('weight')
    attributes.append('wheelNumber')
    attributes.append('year')
    attributes.append('brand')
    attributes.append('createdAt')
    return attributes
def getAlias()->dict:
    aliases = {
        'id':'id',
        "name": "nome",
        "color": "cor",
        "door_number": "portas",
        "price": "preço",
        "driver_name": "motorista",
        "weight": "peso",
        "size": "tamanho",
        "wheel_number": "rodas",
        "year": "ano",
        "brand": "marca",
        "created_at": "criado"
    }
    return aliases
