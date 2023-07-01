import tkinter as tk
from gui_app import Frame, barra_menu
from PIL import ImageTk, Image
from tkinter import Label

def main():
    root = tk.Tk()
    root.title('Catalogo de Productos - Bestias Binarias')
    root.iconbitmap('img/bestiasBinarias.ico')    
    barra_menu(root)
    
    imagen = ImageTk.PhotoImage(Image.open('../catalogo-productos/img/bestiasBinarias.gif'))
    label = Label(image = imagen)
    label.pack()
    
    app = Frame(root = root) 
    app.mainloop()

if __name__ == '__main__' :
    main()