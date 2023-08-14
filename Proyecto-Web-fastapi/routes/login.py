from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/alogin")

usuarios = {
    "jesus": "admin"  # Cambia esto a un hash seguro de la contraseña
}

@router.post("/")
async def login_verificacion(user: str, password: str):
    if user in usuarios and usuarios[user] == password:
        return {"message": "Inicio de sesión exitoso"}
    else:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
