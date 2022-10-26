from crypt import methods
from curses.ascii import isalnum
from fileinput import filename

from flask import Flask, request, jsonify, render_template
# Sirve para trabajar con los archivos que nos llegan de internet
from werkzeug.utils import secure_filename
# Sirve para la inteligencia artificial
from joblib import load
import numpy as np
import os

# Cargar el modelo
dt = load('modelo.joblib')

# Generar el servidor en Flask (Back-end)

servidorWeb = Flask(__name__)

# Anotación, define la ruta. Después se pone una función


@servidorWeb.route("/test", methods=['GET'])
def formulario():
    return render_template('pagina.html')

# Agregar otro servicio. Procesar datos a través del Form


@servidorWeb.route('/modeloIA', methods=["POST"])
def modeloForm():
    # Procesar datos de entrada
    contenido = request.form
    print(contenido)

    datosEntrada = np.array([
        7.7000, 0.5600, 0.0800, 2.5000, 0.1140, 14.0000, 46.0000, 0.9971,
        contenido['pH'],
        contenido['sulfatos'],
        contenido['alcohol']
    ])

    # Usar el modelo
    resultado = dt.predict(datosEntrada.reshape(1, -1))

    return jsonify({"Resultado": str(resultado[0])})

# Procesar datos de un archivo


@servidorWeb.route('/modeloFile', methods=["POST"])
def modeloFile():
    f = request.files['file']
    # PAra poder trabajr con el filename
    filename = secure_filename(f.filename)
    path = os.path.join(os.getcwd(), filename)
    f.save(path)
    file = open(path, 'r')
    datos = []
    # while file.isalnum():
    for line in file:
        datos.append(float(line[:-1]))
    print(datos)
    datosEntrada = np.array(datos)
    resultado = dt.predict(datosEntrada.reshape(1, -1))
    return jsonify({"Resultado": str(resultado[0])})

# Para probar con Postman


@servidorWeb.route('/modelo', methods=["POST"])
def model():
    # Procesar datos de entrada (request)
    contenido = request.json
    print(contenido)
    return jsonify({"Resultado": "datos recibidos Postman"})


if __name__ == '__main__':
    servidorWeb.run(debug=False, host='0.0.0.0', port='8080')
