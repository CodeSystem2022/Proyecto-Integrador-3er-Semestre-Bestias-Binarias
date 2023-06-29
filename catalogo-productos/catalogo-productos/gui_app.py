import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image

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

def desarolladores():

    ventana = Toplevel()
    ventana.config(bg="sky blue")
    ventana.title('Desarrolladores')
    ventana.iconbitmap('../catalogo-productos/img/bestiasBinarias.ico')

    lbl = Label(ventana, text="***** BESTIAS BINARIAS ***** ", font=("Arial Bold", 20))
    lbl.config(bg="sky blue")
    lbl1 = Label(ventana, text= "Daiana Escudero - Daniel Guerrero", font=("Arial Bold", 15))
    lbl1.config(bg="sky blue")
    lbl2 = Label(ventana, text="Mariana Cervantes - Gabriel Romero", font=("Helvetica Bold", 15))
    lbl2.config(bg="sky blue")
    lbl3 = Label(ventana, text="Fernando Silva - Nahuel Tapia", font=("Helvetica Bold", 15))
    lbl3.config(bg="sky blue")
    lbl4 = Label(ventana, text="Florencia Ortega - Albano Calamara", font=("Helvetica Bold", 15))
    lbl4.config(bg="sky blue")
    lbl5 = Label(ventana, text="Nicolas Muros - David Mato", font=("Helvetica Bold", 15))
    lbl5.config(bg="sky blue")
    imagen = ImageTk.PhotoImage(Image.open('../catalogo-productos/img/LOGO_BB3.png'))
    label = Label(ventana, image = imagen)
    label.config(bg="sky blue")
    lbl.pack()
    lbl1.pack()
    lbl2.pack()
    lbl3.pack()
    lbl4.pack()
    lbl5.pack()
    label.pack()
    ventana.mainloop()

class Frame(tk.Frame):

    def __init__(self, root=None):
        super().__init__(root)

        self.root = root
        self.pack()
        self.id_producto = None
        self.tabla_productos()
        
        # Agregar el botón para cambiar el fondo
        img = PhotoImage(file='img/config.png')
        img = img.subsample(15)
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
    
        # Agregamos boton para buscar dentro de la tabla
        self.boton_buscar = tk.Button(self, text='Buscar', command=self.ventana_buscar)
        self.boton_buscar.config(width=20, font=('Arial', 12, 'bold'),
                                 fg='#2C2C2E', bg='#8F00FF',
                                 cursor='hand2', activebackground='#35BD6F')
        self.boton_buscar.grid(row=1, column=1, padx=10, pady=10)
        # Agregamos label para mostrar titulo de la tabla
        self.titulo_tabla = tk.Label(self, text='Lista de Productos',width=20, font=('Comic Sans MS', 16, 'bold'),
                                fg='#2C2C2E', bg='#ffffff')
        self.titulo_tabla.grid(row=3, column=0, padx=10, pady=10, columnspan=4)

        # Agregamos label para mostrar mensajes
        self.mensaje = tk.Label(self, text='',width=50, font=('Comic Sans MS', 12, 'bold'),fg='#000000', bg='#87CEEB')
        self.mensaje.grid(row=2, column=0, padx=10, pady=10, columnspan=4)


    def cambiar_fondo(self):
        color_fondo = tk.colorchooser.askcolor(title="Seleccionar color de fondo")[1]
        self.config(bg=color_fondo)
        self.master.config(bg=color_fondo)
    
     def ventana_buscar(self):
        try:
            self.search = Toplevel()
            self.search.title("Buscar Producto")

            Label(self.search, text="Buscar por Nombre: ").grid(row=0, column=0)

            self.mi_busqueda = tk.StringVar()
            Entry(self.search, textvariable=self.mi_busqueda).grid(
                row=0, column=1)
            self.mensaje1 = tk.Label(self.search, text='', width=50, font=('Comic Sans MS', 12, 'bold'),fg='#000000', bg='#87CEEB')
            self.mensaje1.grid(row=1, column=0, padx=10, pady=10, columnspan=4)

            search_button = tk.Button(self.search, text='Buscar', command=self.buscar_datos)
            search_button.config(width=10, font=('Arial', 12, 'bold'), fg='#ffffff', bg='#5a0173',
                                 cursor='hand2', activebackground='#35B6DF')
            search_button.grid(row=2, column=0, padx=10, pady=10)

            B_cancelar = tk.Button(self.search, text='Cancelar', command= self.search.destroy)
            B_cancelar.config(width=10, font=('Arial', 12, 'bold'), fg='#e9e9f0', bg='#DD1D17',
                              cursor='hand2', activebackground='#35B6DF')
            B_cancelar.grid(row=2, column=1, padx=10, pady=10)
        except:
            title = 'Busqueda de datos'
            message = 'Ocurrió un error'
            messagebox.showerror(title, message)


    
    def buscar_datos(self):
        try:
            # Crear un objeto ttk.Treeview en la ventana emergente (self.search)
            # con tres columnas: 'Nombre', 'precio' y 'Categoria'
            self.ts = ttk.Treeview(self.search, columns=('Nombre', 'Precio', 'Categoria'))
            self.ts.grid(row=3, column=0, columnspan=4, sticky='nsew')

            # Configurar los encabezados del ttk.Treeview con las etiquetas correspondientes
            self.ts.heading('#0', text='ID')
            self.ts.heading('#1', text='NOMBRE')
            self.ts.heading('#2', text='PRECIO')
            self.ts.heading('#3', text='CATEGORIA')

            # Inicializar un contador para llevar la cuenta de los resultados encontrados
            contador = 0
            for p in self.lista_productos:
                # Verificar si el texto de búsqueda (self.mi_busqueda.get()) está presente en el nombre del producto (p[1])
                if self.mi_busqueda.get() in p[1]:
                    # Insertar una nueva fila en el ttk.Treeview con los valores del producto
                    self.ts.insert('', 0, text=p[0], values=(p[1], p[2], p[3]))
                    contador += 1

            # Actualizar el mensaje de resultado según el contador
            if contador == 0:
                self.mensaje1['text'] = 'No se encontraron resultados'
            elif contador == 1:
                self.mensaje1['text'] = 'Se encontró ' + str(contador) + ' resultado'
            elif contador > 1:
                self.mensaje1['text'] = 'Se encontraron ' + str(contador) + ' resultados'

        except:
            # Mostrar un mensaje de error en caso de excepción
            title = 'Búsqueda de datos'
            message = 'Ocurrió un error'
            messagebox.showerror(title, message)

     def abrir_ventana_nuevo(self):

        try:
            self.ventana_nuevo = tk.Toplevel()
            self.ventana_nuevo.title("Nuevo Producto")

            self.ventana_nuevo.geometry("800x200")
            self.ventana_nuevo.iconbitmap('./img/bestiasbinarias.ico')

            self.nombre = tk.Label(self.ventana_nuevo, text="Ingrese nombre de Producto:")
            self.nombre.config(font=('Arial', 12, 'bold'))
            self.nombre.grid(row=0, column=0)

            self.mi_nombre = tk.StringVar()
            self.entry_nombre = tk.Entry(self.ventana_nuevo, textvariable=self.mi_nombre)
            self.entry_nombre.config(width=50, font=('Arial', 12))
            self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

            self.precio = tk.Label(self.ventana_nuevo, text="Ingrese el Precio:")
            self.precio.config(font=('Arial', 12, 'bold'))
            self.precio.grid(row=1, column=0)

            self.mi_precio = tk.StringVar()
            self.entry_precio = tk.Entry(self.ventana_nuevo, textvariable=self.mi_precio)
            self.entry_precio.config(width=50, font=('Arial', 12))
            self.entry_precio.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

            self.mi_categoria = tk.StringVar()
            self.categoria = tk.Label(self.ventana_nuevo, text="Ingrese la Categoría:")
            self.categoria.config(font=('Arial', 12, 'bold'))
            self.categoria.grid(row=2, column=0)

            self.combobox_categoria1 = ttk.Combobox(self.ventana_nuevo, textvariable=self.mi_categoria, state='normal',
                                                    values=self.combobox_categoria['values'])
            self.combobox_categoria1.config(width=47, font=('Arial', 12))
            self.combobox_categoria1.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

            self.B_guardar = tk.Button(self.ventana_nuevo, text="Guardar datos", command=self.guardar_datos)
            self.B_guardar.grid(row=4, column=1)
            self.B_guardar.config(width=20, font=('Arial', 12, 'bold'), fg='#e9e9f0', bg='#1528CC', cursor='hand2',
                                  activebackground='#35B6DF')

            self.B_cerrar = tk.Button(self.ventana_nuevo, text="Cancelar", command=self.ventana_nuevo.destroy)
            self.B_cerrar.grid(row=4, column=2)
            self.B_cerrar.config(width=20, font=('Arial', 12, 'bold'), fg='#e9e9f0', bg='#DD1D17', cursor='hand2',
                                 activebackground='#35B6DF')
        except:
            titulo = 'Agregar datos'
            mensaje = 'No has colocado ningún producto'
            messagebox.showerror(titulo, mensaje)

# Creamos la función para guardar los datos
    def guardar_datos(self):
        producto = Producto(
            self.mi_nombre.get(),
            self.mi_precio.get(),
            self.mi_categoria.get(),
        )
        if self.id_producto is None:
            guardar(producto)
            # Agrega la nueva opción a los valores del combobox
            self.combobox_categoria['values'] = tuple(
                list(self.combobox_categoria['values']) + [self.mi_categoria.get()]
            )
        else:
            pass
        self.tabla_productos()
        self.ventana_nuevo.destroy()
        self.mensaje['text'] = '¡¡¡ Producto:  {}  agregado satisfactoriamente !!!'.format(self.mi_nombre.get())

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
    def ventana_editar(self):
        try:
            self.id_producto = self.tabla.item(self.tabla.selection())['text']
            self.mi_nombre.set(self.tabla.item(self.tabla.selection())['values'][0])
            self.mi_precio.set(self.tabla.item(self.tabla.selection())['values'][1])
            self.mi_categoria.set(self.tabla.item(self.tabla.selection())['values'][2])
            # Creamos una nueva ventana que se abrira al presionar el boton editar
            self.ventana = Toplevel()
            self.ventana.title("Editar Producto" )
            self.ventana.iconbitmap('./img/bestiasbinarias.ico')
            self.ventana.geometry("500x150")

            # Nombre nuevo del producto a editar, se crea un label y un entry para ingresar el nuevo nombre
            self.nuevo_nombre = tk.Label(self.ventana, text="Nombre Nuevo: ",width=20, font=('Arial', 12, 'bold'))
            self.nuevo_nombre.grid(row=1, column=0)
            Entry(self.ventana, textvariable=self.mi_nombre,width=20, font=('Arial', 12, 'bold'), fg='#2C2C2E').grid(
                row=1, column=1, sticky='wsen', columnspan=3)
            # Precio nuevo del producto a editar, se crea un label y un entry para ingresar el nuevo precio
            self.nuevo_precio = tk.Label(self.ventana, text="Precio Nuevo: ",width=20, font=('Arial', 12, 'bold'))
            self.nuevo_precio.grid(row=2, column=0)
            Entry(self.ventana, textvariable=self.mi_precio, width=20, font=('Arial', 12, 'bold'), fg='#2C2C2E' ).grid(
                row=2, column=1, sticky='wsen', columnspan=3)

            # Categoria nueva del producto a editar, se crea un label y un combobox para ingresar la nueva categoria
            Label(self.ventana, text="Categoria Nueva: ",width=20, font=('Arial', 12, 'bold'), fg='#2C2C2E').grid(row=3, column=0)
            ttk.Combobox(self.ventana, textvariable=self.mi_categoria, state='normal',width=20, font=('Arial', 12, 'bold'),
                         values=self.combobox_categoria['values']).grid(
                row=3, column=1, sticky='wsen', columnspan=3)
            # Creamos el boton para actualizar los valores ingresados en la ventana de editar
            B_editar = tk.Button(self.ventana, text='Actualizar', command=self.actualizar_datos)
            B_editar.config(width=10, font=('Arial', 12, 'bold'), fg='#e9e9f0', bg='#1528CC',
                            cursor='hand2', activebackground='#35B6DF')
            B_editar.grid(row=4, column=3, padx=10, pady=10)
            # Creamos el boton para cancelar y llamamos a la funcion cancelar_ventana
            B_cancelar = tk.Button(self.ventana, text='Cancelar', command=self.ventana.destroy)
            B_cancelar.config(width=10, font=('Arial', 12, 'bold'), fg='#e9e9f0', bg='#DD1D17',
                              cursor='hand2', activebackground='#35B6DF')
            B_cancelar.grid(row=4, column=2, padx=10, pady=10)

        except:
            titulo = 'Edición de datos'
            mensaje = 'No has seleccionado ningún registro'
            messagebox.showerror(titulo, mensaje)

    #Funcion para actualizar los datos
    def actualizar_datos(self):
        #Leemos el contenido de la tabla
        producto = Producto(
            self.mi_nombre.get(),
            self.mi_precio.get(),
            self.mi_categoria.get(),
        )
        try:
            #Llamos a la funcion editar que se encuentra en producto_dao y contiene el query necesario
            editar(producto, self.id_producto)
            self.tabla_productos()
            #Una vez actualizados los datos se cierra la ventana al dar clic en el boton Actualizar
            self.ventana.destroy()
        except:
            titulo = 'Error al actualizar'
            mensaje = 'No se pudo actualizar el registro'
            messagebox.showerror(titulo, mensaje)
        self.mensaje['text'] = '¡¡¡ Producto:  {}  actualizado satisfactoriamente !!!'.format(self.mi_nombre.get())
