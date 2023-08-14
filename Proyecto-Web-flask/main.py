from flask import Flask, render_template
from static.recursos import conjunto as c


app = Flask(__name__)


@app.route('/')
async def home():
    return render_template('home.html', valor = c.home_json)

@app.route('/login/<user> <password>')
async def login(user, password):
    if user == "jesus" and password == "gomez":
        return {"mensajes":"Bienvenido"}
    else:
        return {"mensaje":"User and password incorrect"}


@app.get('/login2/<user>')
async def login2(user: str):
    return user


app.run(port=9999, debug=True)
