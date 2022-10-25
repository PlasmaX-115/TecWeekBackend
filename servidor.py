
import json
from stat import filemode
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from joblib import load
import numpy as np
import os

#Cargar el modelo. Ahora se puede usar en toda la aplicación web
dt = load('modelo.joblib') 

#Generar el servidor en flask (Back-end)

servidorWeb = Flask(__name__) #Flask recibe la conexión

#Anotación

@servidorWeb.route("/test",methods = ['GET'])

def formulario():
    return render_template('pagina.html')

#Procesar datos a través del Form 
@servidorWeb.route('/modeloIA', methods=["POST"])
def modeloForm():
    #Procesar datos de entrada
    contenido = request.form
    print(contenido)

    datosEntrada = npArray ([7.8000, 0.4300, 0.7000, 1.9000, 0.4640, 22.0000, 67.0000, 0.9974,
    contenido['pH'],
    contenido ['sulfatos'],
    contenido ['alcohol']
    ])

    #Utilizar el modelo
    resultado=dt.predict(datosEntrada.reshape(1, -1))

    return jsonify({"Resultado": str(resultado[0])})

    #Convertir un diccionario a json. Será lo que regresaremos
    #return jsonify({"Resultado":"datos recibidos"})


#Procesar datos de un archivo 
@servidorWeb.route('/modeloFile', methods = ['POST'])
def modeloFile():
    f= request.files['file']
    filename= secure_filename(f.filename)
    path=os.path.join(os.getcwd(), filename)
    f.save(path)
    file=open(path,'r') #Se abre un archivo en modo de lectura y lo recorre por cada línea.
    for line in file:
        print(line)
    return jsonify({"Resultado":"datos recibidos"})

@servidorWeb.route('/modelo', methods=["POST"])
def model():
    #Procesar datos de entrada
    contenido = request.json
    print(contenido)
    #Convertir un diccionario a json. Será lo que regresaremos
    return jsonify({"Resultado":"datos recibidos"})




if __name__ == '__main__':
    servidorWeb.run(debug=False, host = '0.0.0.0', port = '8080') # Dirección General