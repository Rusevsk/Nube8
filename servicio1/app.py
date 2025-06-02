from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Hola desde Servicio 1! --actualizado en el servicio 1"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)