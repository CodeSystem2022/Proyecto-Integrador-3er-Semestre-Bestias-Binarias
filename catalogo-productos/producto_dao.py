from tkinter import messagebox

from conexion_db import ConexionDB


def crear_tabla():
    conexion = ConexionDB()
    
    sql = '''
    CREATE TABLE productos (
        id_producto INTEGER, 
        nombre VARCHAR (100),
        precio VARCHAR (10),
        categoria VARCHAR(100),
        PRIMARY KEY (id_producto)
        )
    '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Crear Registro'
        mensaje = 'Se creó la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'La tabla ya esta creada'
        messagebox.showwarning(titulo, mensaje)
        

def borrar_tabla(): 
    conexion = ConexionDB()
    
    sql = 'DROP TABLE productos'
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar Registro'
        mensaje = 'La tabla de la base de datos se borró con éxito'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear Registro'
        mensaje = 'No hay tabla para borrar'
        messagebox.showerror(titulo, mensaje)
        
class Producto:
    def __init__(self, nombre, precio , categoria):
        self.id = None 
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        
    def __str__(self):
        return f'Producto[{self.nombre}, {self.precio}, {self.categoria}]'
    
def guardar(producto):
    conexion = ConexionDB()
    
    sql = f'''
    INSERT INTO productos (nombre, precio, categoria) 
    VALUES ('{producto.nombre}', '${producto.precio}', '{producto.categoria}')
    '''
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'La tabla productos no esta creada en la base de datos'
        messagebox.showerror(titulo, mensaje)
        
