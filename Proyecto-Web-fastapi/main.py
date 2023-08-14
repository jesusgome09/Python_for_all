from fastapi import FastAPI, HTTPException, status
from fastapi.staticfiles import StaticFiles
from starlette.responses import HTMLResponse
from routes import home, login

app = FastAPI()
app.include_router(home.router)
app.include_router(login.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def home_page():
    with open("templates/index.html") as f:
        archivo = f.read()
    try:
        return HTMLResponse(archivo)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, headers={"Error":"Pagina no encontrada"})

@app.get("/contact")
async def contac_page():
    with open("templates/contactos.html") as f:
        archivo = f.read()
    try:
        return HTMLResponse(archivo)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, headers={"Error":"Pagina no encontrada"})

@app.get("/login")
async def login_page():
    with open("templates/login.html") as f:
        archivo = f.read()
    try:
        return HTMLResponse(archivo)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, headers={"Error":"Pagina no encontrada"})
