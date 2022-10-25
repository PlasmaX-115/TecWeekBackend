from stat import filemode
from flask import Flask, request, jsonify, render_template
from werkzug.utils import secure_filename
from joblib import load
import numpy as np
import os

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

    contenido = request.Form
    print(contenido)
    #Convertir un diccionario a json. Será lo que regresaremos
    return jsonify({"Resultado":"datos recibidos"})


#Procesar datos de un archivo 
@servidorWeb.route('/modeloFile', methods = ['POST'])
def modeloFile():
    f= request.files['file']
    filename= secure_filename(f.filename)
    path=os.path.join(os.getcwd, 'files', filename)
    f.save(path)
    file=open(path,'r') #Se abre un archivo en modo de lectura y lo recorre por cada línea.
    for line in file:
        print(line)
    return jsonify({"Resultado":"datos recibidos"})



if __name__ == '__main__':
    servidorWeb.run(debug=False, host = '0.0.0.0', port = '8080') # Dirección General