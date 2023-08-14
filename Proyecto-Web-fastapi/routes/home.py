from fastapi import APIRouter


router = APIRouter(
    prefix="/ahome",
    responses={404: {"descripcion": "No encontrado"}},
    tags=["ahome"],
)

home_json = {
    "titulo": "La pagina del programador",
    "mensaje": "Bienvenido a la pagina del programador",
    "creador": "Crada por: Jesus Gomez",
}


@router.get("/")
async def ahome_page():
    return home_json
