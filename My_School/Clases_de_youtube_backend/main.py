from fastapi import FastAPI
#from starlette.responses import HTMLResponse
from routers import products
from routers import users
from fastapi.staticfiles import StaticFiles
from routers import jwt_auth_users

#uvicorn main:app --reload

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(jwt_auth_users.router)
app.mount("/static", StaticFiles(directory="static"), name="static")


# redirecciones


@app.get("/")
async def root():
    return {"message": "Hello World"}



## comentarios ##

# @app.get("/")
# async def root():
#     with open("static/index.html") as f:
#         content = f.read()
#     return HTMLResponse(content)

# documetacion de la api
# http://http://127.0.0.1:8000/docs
# http://http://127.0.0.1:8000/redoc
