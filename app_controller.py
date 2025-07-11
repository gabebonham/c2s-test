from fastapi import APIRouter, FastAPI
from services.service import Service
app = FastAPI()
router = APIRouter()

@router.get("/automoveis")
async def read_users(
    nome:str=None,
    cor:str=None,
    portas:int=None,
    preço:float=None,
    motorista:str=None,
    peso:float=None,
    tamanho:float=None,
    rodas:int=None,
    ano:int=None,
    marca:str=None
):
    filter = {
        'nome':nome,
        'cor':cor,
        'portas':portas,
        'preço':preço,
        'motorista':motorista,
        'peso':peso,
        'tamanho':tamanho,
        'rodas':rodas,
        'ano':ano,
        'marca':marca
    }
    service = Service()
    return service.getResultsApi(filter)


app.include_router(router)