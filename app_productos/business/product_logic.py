from data_acces.product_data import agregar_producto, eliminar_producto, modificar_producto, obtener_todos
from models.product import Producto

def alta_producto(nombre, descripcion, precio):
    producto = Producto(nombre, descripcion, precio)
    agregar_producto(producto)

def baja_producto(nombre):
    eliminar_producto(nombre)

def modificar(nombre, nuevo_nombre, nueva_descripcion, nuevo_precio):
    nuevo_producto = Producto(nuevo_nombre, nueva_descripcion, nuevo_precio)
    modificar_producto(nombre, nuevo_producto)

def listar_productos():
    return obtener_todos()
