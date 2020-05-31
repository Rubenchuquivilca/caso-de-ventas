from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from json import dumps
from UsuarioDAO import Usuario
user = Usuario()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def listar():
    return jsonify({'mensaje': 'Bienvenidos a Flaskas'})


@app.route('/usuario/listar', methods=['GET'])
def users():
    try:
        rows = user.readAll()
        respuesta = jsonify(rows)
        respuesta.status_code = 200
        return respuesta
    except Exception as e:
        print(e)


@app.route('/usuario/buscar/<int:id>')
def buscarescuela(id):
	try:
		user.idusuario = id
		row = user.buscarusuario()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)


@app.route('/usuario/create', methods=['POST'])
def agregarusuario():
    try:
        _json = request.json                   
        user.nomuser=_json['nomuser']
        user.clave=_json['pass']
        if request.method=='POST':
            resp=user.agregarusuario()
            resp=jsonify('USUARIO')
            resp.status_code=200
        return resp
    except Exception as e:
        print(e)

@app.route('/usuario/eliminar/<int:id>', methods=['GET'])
def eliminarusuario(id):
    try:
        user.idusuario=id
        resp=user.delete()
        resp=jsonify('Usuario Elimindado')
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)    
@app.route('/usuario/modificar', methods=['PUT'])
def modificarusuario():
    try:
        _json=request.json
        user.nomuser=_json['nomuser']
        user.clave=_json['pass']
        user.idusuario=_json['iduser']
        if request.method == 'PUT':
            resp = user.modificarusuario()
            resp = jsonify('Usuario Modificada')
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)  
    
      
