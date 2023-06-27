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
    heramientas.add_command(label='Celulares')
    heramientas.add_command(label='Notebooks')
    heramientas.add_command(label='Tablets')

    configuracion = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Configuración', menu=configuracion)
    configuracion.add_command(label='Preferencias')
    configuracion.add_command(label='Administrar cuenta')

    ayuda = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Ayuda', menu=ayuda)
    ayuda.add_command(label='Preguntas frecuentes')
    ayuda.add_command(label='Contacto servicio tecnico')

    acerca = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Acerca de', menu=acerca)
    acerca.add_command(label='Desarrolladores')
    acerca.add_command(label='Login')



class Frame(tk.Frame):

    def __init__(self, root=None):
        super().__init__(root)

        self.root = root
        self.pack()
        self.id_producto = None
        self.tabla_productos()

        img = PhotoImage(file='img/config.png')
        img = img.subsample(15)
        # Agregar el botón para cambiar el fondo
        self.boton_cambiar_fondo = tk.Button(self,text='Color fondo' ,image=img)
        self.boton_cambiar_fondo.config(width=40, font=('Arial', 12, 'bold'),
                                        fg='#2C2C2E', relief= 'raised',
                                        cursor='hand2', activebackground='#ffffff')
        self.boton_cambiar_fondo.place(x=775, y=5)
        self.boton_cambiar_fondo.image = img

        self.mi_nombre = tk.StringVar()
        self.mi_precio = tk.StringVar()
        self.mi_categoria = tk.StringVar()

        self.boton_nuevo = tk.Button(self, text='Ingreso nuevo')
        self.boton_nuevo.config(width=20, font=('Arial', 12, 'bold'),
                                fg='#2C2C2E', bg='#3CF90D',
                                cursor='hand2', activebackground='#35BD6F')
        self.boton_nuevo.grid(row=1, column=0, padx=10, pady=10)

        self.boton_buscar = tk.Button(self, text='Buscar')
        self.boton_buscar.config(width=20, font=('Arial', 12, 'bold'),
                                 fg='#2C2C2E', bg='#66aa11',
                                 cursor='hand2', activebackground='#35BD6F')
        self.boton_buscar.grid(row=1, column=1, padx=10, pady=10)

        self.titulo_tabla = tk.Label(self, text='Lista de Productos',width=20, font=('Comic Sans MS', 14, 'bold'),
                                fg='#2C2C2E', bg='#ffffff')
        self.titulo_tabla.grid(row=3, column=0, padx=10, pady=10, columnspan=4)
        

    def tabla_productos(self):
        
        self.mi_categoria = tk.StringVar()
        self.combobox_categoria = ttk.Combobox(self, textvariable=self.mi_categoria, state='readonly')
  

        self.tabla = ttk.Treeview(self, columns=('Nombre', 'precio', 'Categoria'))
        self.tabla.grid(row=4, column=0, columnspan=4, sticky='nsew')

        # Scrollbar para la tabla si excede 10 registros
        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=4, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='PRECIO')
        self.tabla.heading('#3', text='CATEGORIA')

  
        # Boton Editar
        self.boton_editar = tk.Button(self, text='Editar')
        self.boton_editar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='#2C2C2E', bg='#77dd77',
                                cursor='hand2', activebackground='#35BD6F')
        self.boton_editar.grid(row=5, column=0, padx=10, pady=10)

        # Boton Eliminar
        self.boton_eliminar = tk.Button(self, text='Eliminar')
        self.boton_eliminar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='#2C2C2E', bg='#ff8097',
                                cursor='hand2', activebackground='#E15370')
        self.boton_eliminar.grid(row=5, column=1, padx=10, pady=10)