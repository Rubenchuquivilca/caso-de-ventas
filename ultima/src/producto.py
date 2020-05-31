
from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from json import dumps
from ProductoDAO import Producto
prod = Producto()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def listar():
    return jsonify({'mensaje': 'Bienvenidos a Producto'})

@app.route('/producto/listar', methods=['GET'])
def produ():
    try:
        rows = prod.readAll()
        respuesta = jsonify(rows)
        respuesta.status_code = 200
        return respuesta
    except Exception as e:
        print(e)

@app.route('/producto/buscar/<int:id>')
def buscarproducto(id):
    try:
        prod.idproducto = id
        row = prod.buscarproducto()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)

@app.route('/producto/create', methods=['POST'])
def agregarproducto():
    try:
        _json = request.json
        prod.nomproducto=_json['nomproducto']
        prod.precio=_json['precio']
        prod.cantidad=_json['cantidad']
        if request.method=='POST':
            resp=prod.agregarproducto()
            resp=jsonify('PRODUCTO')
            resp.status_code=200
        return resp
    except Exception as e:
        print(e)

@app.route('/producto/eliminar/<int:id>', methods=['GET'])
def eliminarproducto(id):
    try:
        prod.idproducto=id
        resp=prod.delete()
        resp=jsonify('Producto Eliminado')
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)

@app.route('/producto/modificar', methods=['PUT'])
def modificarproducto():
    try:
        _json=request.json
        prod.nomproducto=_json['nomproducto'] 
        prod.precio=_json['precio']
        prod.cantidad=_json['cantidad']  
        prod.idproducto=_json['idprod']   
        if request.method == 'PUT':
            resp = prod.modificarproducto()
            resp = jsonify('Producto Modificada')     
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)


            