from fastapi import APIRouter, HTTPException
from pydantic import BaseModel  # nos brinda la capacidad de crear un item

# Inciar el server: uvicorn users:router --reload

router = APIRouter(
    responses={404: {"descripcion": "No encontrado"}},
    tags=["users"],
    )


# entidad user
class User(BaseModel):
    id: int
    name: str
    lastname: str


users_list = [
    User(id=1234, name="Jesus", lastname="Garcia"),
    User(id=4567, name="Maria", lastname="Garcia"),
    User(id=7891, name="Jose", lastname="Garcia"),
]


@router.get("/userjason")
async def usersjson():
    return [{"name": "Jesus"}, {"name": "Maria"}, {"name": "Jose"}]


@router.get("/user")
async def usersclass():
    return users_list


@router.get("/userid/{id}")
async def userid(id: int):  # http://name/value
    return search_user(id)


@router.get("/userquery/")  # http://name/?variable=value
async def userquery(id: int):
    return search_user(id)


@router.post("/user")  # agregar un nuevo usuario
async def userpost(user: User):
    if search_user_v(user.id):
        users_list.append(user)
        return {"message": "User created successfully"}
    else:
        return {"message": "User already exists"}


@router.put("/user")  # actualizar un usuario
async def userput(user: User):
    fount = False
    for index, user_saved in enumerate(users_list):
        if user_saved.id == user.id:
            users_list[index] = user
            fount = True

    if not fount:
        return {"message": "User not found"}
    else:
        return {"message": "User updated successfully"}, search_user(user.id)


@router.delete("/userdel/{id}")  # eliminar un usuario
async def userdelete(id: int):
    fount = False
    for index, user_saved in enumerate(users_list):
        if user_saved.id == id:
            del users_list[index]
            fount = True

    if not fount:
        return {"message": "User not found"}
    else:
        return {"message": f"User {id} deleted successfully"}


###  funciones  ###


def search_user_v(id: int):
    user = next((u for u in users_list if u.id == id), None)
    if user is None:
        return True
    return False


def search_user(id: int, status_code=200):
    user = next((u for u in users_list if u.id == id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        raise HTTPException(status_code=250, detail="User found", headers={"MSG": "Si se encuetra"})

    return user
