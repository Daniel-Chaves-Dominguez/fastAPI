from fastapi import APIRouter, HTTPException

from models.perro import Perro

router = APIRouter(
    prefix='/perros',
    tags=['Perros']
)

lista_perros: list[Perro] = []


@router.get('/')
def listar_perros():
    return lista_perros


@router.post('/', status_code=201)
def crear_perro(perro: Perro):
    if perro.edad > 80:
        raise HTTPException(status_code=400, detail='El perro es demasiado viejo')
    lista_perros.append(perro)
    return {
        'mensaje': 'El perro se guardó correctamente',
        'datos_perro': {
            'nombre': perro.nombre,
            'raza': perro.raza
        }
    }
