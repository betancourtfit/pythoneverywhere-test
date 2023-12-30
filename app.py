# Importamos la clase Flask
from flask import Flask

# Creamos una instancia de la clase Flask
app = Flask(__name__)

# Definimos la ruta raíz '/'
@app.route('/')
def hello_world():
    return '¡Hola, mundo!'

# Verificamos si el archivo es el programa principal
if __name__ == '__main__':
    # Ejecutamos la aplicación
    app.run(debug=True)
