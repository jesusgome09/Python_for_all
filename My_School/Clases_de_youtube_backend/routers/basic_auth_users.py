from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

# uvicorn basic_auth_users:app --reload

aoauth2 = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(BaseModel):
    password: str


users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "jhondoe@gmail.com",
        "disabled": False,
        "password": "123456",
    },
    "pedrocampos": {
        "username": "pedrocampos",
        "full_name": "Pedro Campos",
        "email": "pedrocampo@hotmail.com",
        "disabled": True,
        "password": "654321",
    },
}


def search_user(username: str):
    if username in users_db.keys():
        return User(**users_db[username])

def search_user_db(username: str):
    if username in users_db.keys():
        return UserDB(**users_db[username])


# Creamos un criterio de dependencia
async def current_user(token: str = Depends(aoauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticacion invalidas",
            headers={"WWW-Authenticate": "Bearer"})
    if user.disabled:
        raise HTTPException(status_code=400,
         detail="Usuario inactivo", headers={"state": "inactive"})

    return user


@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)

    if not user_db:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")

    user = search_user(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrecta")

    return {"acecess_token": form.username, "token_type": "bearer"}


@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user

#Se llama de la siguiente manera:
# post -> body -> form-data -> username: johndoe, password: 123456
