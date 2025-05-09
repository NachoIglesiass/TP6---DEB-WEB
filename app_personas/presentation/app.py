from flask import Flask, request, jsonify
from business.person_logic import alta_persona, baja_persona, modificar, listar_personas

app = Flask(__name__)

@app.route('/personas', methods=['GET'])
def listar():
    personas = listar_personas()
    return jsonify([vars(p) for p in personas])

@app.route('/personas', methods=['POST'])
def crear():
    data = request.json
    alta_persona(data['nombre'], data['apellido'], data['edad'])
    return 'Persona agregada', 201

@app.route('/personas/<nombre>', methods=['DELETE'])
def eliminar(nombre):
    baja_persona(nombre)
    return 'Persona eliminada'

@app.route('/personas/<nombre>', methods=['PUT'])
def modificar_persona(nombre):
    data = request.json
    modificar(nombre, data['nombre'], data['apellido'], data['edad'])
    return 'Persona modificada'

if __name__ == '__main__':
    app.run(debug=True)
