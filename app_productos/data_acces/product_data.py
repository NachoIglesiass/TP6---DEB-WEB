productos = []

def agregar_producto(producto):
    productos.append(producto)

def eliminar_producto(nombre):
    global productos
    productos = [p for p in productos if p.nombre != nombre]

def modificar_producto(nombre, nuevo_producto):
    eliminar_producto(nombre)
    agregar_producto(nuevo_producto)

def obtener_todos():
    return productos
