import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox


def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)
    menu_inicio.add_command(label='Crear Registro en DB')
    menu_inicio.add_command(label='Eliminar Registro en DB')
    menu_inicio.add_command(label='Salir', command=root.destroy)

    heramientas = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Herramientas', menu=heramientas)
 
    configuracion = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Configuración', menu=configuracion) 

    ayuda = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Ayuda', menu=ayuda)



class Frame(tk.Frame):

    def __init__(self, root=None):
        super().__init__(root)

        self.root = root
        self.pack()
        # self.config(bg = '#EAEDED')
        self.id_producto = None
        self.campos_producto()
        #self.deshabilitar_campos()
        #self.tabla_productos()

    def campos_producto(self):
        # Labels de cada campo
        self.label_nombre = tk.Label(self, text='Nombre: ')
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        self.label_precio = tk.Label(self, text='Precio: ')
        self.label_precio.config(font=('Arial', 12, 'bold'))
        self.label_precio.grid(row=1, column=0, padx=10, pady=10)

        self.label_categoria = tk.Label(self, text='Categoria: ')
        self.label_categoria.config(font=('Arial', 12, 'bold'))
        self.label_categoria.grid(row=2, column=0, padx=10, pady=10)

        # Entrys(inputs) de cada campo
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50, font=('Arial', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        self.mi_precio = tk.StringVar()
        self.entry_precio = tk.Entry(self, textvariable=self.mi_precio)
        self.entry_precio.config(width=50, font=('Arial', 12))
        self.entry_precio.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        self.mi_categoria = tk.StringVar()
        self.combobox_categoria = ttk.Combobox(self, textvariable=self.mi_categoria, state='readonly')
        self.combobox_categoria.config(width=47, font=('Arial', 12))
        self.combobox_categoria.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        

     