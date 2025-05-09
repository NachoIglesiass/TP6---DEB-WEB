from flask import Flask, request, jsonify
from app_productos.business.product_logic import alta_producto, baja_producto, modificar, listar_productos

app = Flask(__name__)

@app.route('/productos', methods=['GET'])
def listar():
    productos = listar_productos()
    return jsonify([vars(p) for p in productos])

@app.route('/productos', methods=['POST'])
def crear():
    data = request.json
    alta_producto(data['nombre'], data['descripcion'], data['precio'])
    return 'Producto agregado', 201

@app.route('/productos/<nombre>', methods=['DELETE'])
def eliminar(nombre):
    baja_producto(nombre)
    return 'Producto eliminado'

@app.route('/producto/<nombre>', methods=['PUT'])
def modificar_persona(nombre):
    data = request.json
    modificar(nombre, data['nombre'], data['descripcion'], data['precio'])
    return 'Producto modificada'

if __name__ == '__main__':
    app.run(debug=True)
