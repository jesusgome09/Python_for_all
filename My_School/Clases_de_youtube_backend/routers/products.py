from fastapi import APIRouter

router = APIRouter(
    prefix="/products",
    responses={404: {"descripcion": "No encontrado"}},
    tags=["products"],
    )

lista = ["producto 1", "producto 2", "producto 3", "producto 4", "producto 5"]


@router.get("/")
async def products():
    return lista

@router.get("/{id}")
async def products(id: int):
    return lista[id]
