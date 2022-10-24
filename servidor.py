from flask import Flask, request, jsonify, render_template

#Generar el servidor en flask (Back-end)

servidorWeb = Flask(__name__) #Flask recibe la conexión

#Anotación

@servidorWeb.route("/test",methods = ['GET'])

def formulario():
    return render_template('pagina.html')

if __name__ == '__main__':
    servidorWeb.run(debug=False, host = '0.0.0.0', port = '8080') # Dirección General