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
        "doorNumber": "numero de portas",
        "price": "preço",
        "driverName": "nome do motorista",
        "weight": "peso",
        "size": "tamanho",
        "wheelNumber": "numero de rodas",
        "year": "ano",
        "brand": "marca",
        "createdAt": "criado"
    }
    return aliases
