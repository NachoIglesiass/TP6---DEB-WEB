personas = []

def agregar_persona(persona):
    personas.append(persona)

def eliminar_persona(nombre):
    global personas
    personas = [p for p in personas if p.nombre != nombre]

def modificar_persona(nombre, nueva_persona):
    eliminar_persona(nombre)
    agregar_persona(nueva_persona)

def obtener_todas():
    return personas
