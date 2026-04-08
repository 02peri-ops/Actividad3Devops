#Página web con flask
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola! Bienevenido a la app en docker"

app.run(host='0.0.0.0', port=5000)