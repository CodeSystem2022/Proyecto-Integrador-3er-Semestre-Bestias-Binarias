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
        
def listar():
    conexion = ConexionDB()
    
    lista_productos = []
    
    sql = 'SELECT * FROM productos'
    
    try:
        conexion.cursor.execute(sql)
        lista_productos = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'Crea la tabla en la base de datos'
        messagebox.showerror(titulo, mensaje)
        
    return lista_productos

def editar(producto, id_producto):
    conexion = ConexionDB()
    
    sql = f'''
    UPDATE productos 
    SET nombre = '{producto.nombre}', precio = '${producto.precio}',
    categoria = '{producto.categoria}' WHERE id_producto = {id_producto} 
    '''
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Edición de datos'
        mensaje = 'No se ha podido editar este registro'
        messagebox.showerror(titulo, mensaje)
        
def eliminar(id_producto):
    conexion = ConexionDB()
    
    sql = f'DELETE FROM productos WHERE id_producto = {id_producto}'
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Eliminar datos'
        mensaje = 'No se puedo eliminar el registro'
        messagebox.showerror(titulo, mensaje)
        


def reiniciar_id():
    conexion = ConexionDB()

    sql = f'UPDATE sqlite_sequence set seq=0 where name=`productos`;'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Eliminar id'
        mensaje = 'No se puedo eliminar el id'
        messagebox.showerror(titulo, mensaje)
