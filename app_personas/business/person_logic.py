from data_acces.person_data import agregar_persona, eliminar_persona, modificar_persona, obtener_todas
from models.person import Persona

def alta_persona(nombre, apellido, edad):
    persona = Persona(nombre, apellido, edad)
    agregar_persona(persona)

def baja_persona(nombre):
    eliminar_persona(nombre)

def modificar(nombre, nuevo_nombre, nuevo_apellido, nueva_edad):
    nueva_persona = Persona(nuevo_nombre, nuevo_apellido, nueva_edad)
    modificar_persona(nombre, nueva_persona)

def listar_personas():
    return obtener_todas()
