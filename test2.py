from config import *
from utils.ClaseAlbum import *
from utils.ClaseArtista import *
from utils.ClaseCancion import *
from utils.datos import *
import tkinter as tk
from tkinter import messagebox


#------------------ Ventana ------------------#
ventana = tk.Tk()
ventana.title("Biblioteca de Musica")
ventana.geometry("400x700")
ventana.resizable(0,0)
#---------------------------------------------#

#------------------ Boton "agrgar_artistas" ------------------#
def a_c(): #agrgar_artistas()
    subventana = tk.Toplevel(ventana)
    subventana.title("Agregar Artistas")
    subventana.geometry("400x400")

#---------------------------------------------#
    etiqueta_nombre = tk.Label(subventana, text = "Ingresa El Nombre: ")
    etiqueta_nombre.place(relx=0.5, rely=0.1, anchor= "center")
    entrada_nombre = tk.Entry(subventana)
    entrada_nombre.place(relx=0.5, rely=0.15, anchor= "center")
#---------------------------------------------#

#---------------------------------------------#
    etiqueta_edad = tk.Label(subventana, text = "Ingresa La Edad: ")
    etiqueta_edad.place(relx=0.5, rely=0.3, anchor= "center")
    entrada_edad = tk.Entry(subventana)
    entrada_edad.place(relx=0.5, rely=0.35, anchor= "center")
#---------------------------------------------#

#---------------------------------------------# 
    etiqueta_pais = tk.Label(subventana, text = "Ingresa El País: ")
    etiqueta_pais.place(relx=0.5, rely=0.5, anchor= "center")
    entrada_pais = tk.Entry(subventana)
    entrada_pais.place(relx=0.5, rely=0.55, anchor= "center")
#---------------------------------------------#

    def g(): #guadar
        nombre = entrada_nombre.get()
        edad = entrada_edad.get()
        pais = entrada_pais.get()
        try:
            edad = int(entrada_edad.get())
        except ValueError:
            messagebox.showwarning("ValueError", "El valor debe ser númerico")
    
        artista = Artista(nombre, edad, pais)
        global lista_artistas
        lista_artistas.append(artista)
        messagebox.showinfo("Exito", "El Artista ha sido guardado")


    b_g = tk.Button(subventana, text= ("Guardar"), width= 8, height= 2, command= g)
    b_g.place(relx=0.5, rely=0.9, anchor= "center")


boton = tk.Button(ventana, text= ("Agregar Libros"), width= 30, height= 5, command = a_c)
boton.place(relx=0.5, rely=0.1, anchor= "center")
#----------------------------------------------------#

#------------------ Boton "ver_libros" ------------------#
def v_l(): #ver_libros()
    subventana = tk.Toplevel(ventana)
    subventana.title("Ver Libros")
    subventana.geometry("400x400")

    titulodispo = Bibliotec.titulodispo()
    print(titulodispo)
    listbox = tk.Listbox(subventana)
    listbox.insert(0, *titulodispo)
    listbox.place(relx = 0.5, rely = 0.5, anchor= "center")
boton = tk.Button(ventana, text= ("Ver Libros"), width= 30, height= 5, command = v_l)
boton.place(relx=0.5, rely=0.3, anchor= "center")

#----------------------------------------------------#

#------------------ Boton "buscar_libros" ------------------#
def b_l(): #buscar_libros
    subventana = tk.Toplevel(ventana)
    subventana.title("Buscar Libros")
    subventana.geometry("400x300")

#----------------------------------------------------#
    etiqueta_l = tk.Label(subventana, text = "Nombre del libro")
    etiqueta_l.place(relx=0.5, rely=0.2, anchor= "center")
    entrada_l = tk.Entry(subventana)
    entrada_l.place(relx=0.5, rely=0.25, anchor= "center")
#----------------------------------------------------#

    def b(): #buscar
        t = entrada_l.get() #titulo
        nom, aut, gen, año =Bibliotec.buscarLibro(t)

        def m(): 
            subventana = tk.Toplevel(ventana)
            subventana.title("A")
            subventana.geometry("400x300")


        b_g = tk.Button(subventana, text= ("Guardar"), width= 8, height= 2, command= m)
        b_g.place(relx=0.5, rely=0.9, anchor= "center")


    b_g = tk.Button(subventana, text= ("Guardar"), width= 8, height= 2, command= b)
    b_g.place(relx=0.5, rely=0.9, anchor= "center")

boton = tk.Button(ventana, text= ("Buscar Libros"), width= 30, height= 5, command = b_l)
boton.place(relx=0.5, rely=0.5, anchor= "center")

#----------------------------------------------------#

#------------------ Boton "prestar_libros" ------------------#
def p_l(): #prestar_libros
    subventana = tk.Toplevel(ventana)
    subventana.title("Prestar Libro")
    subventana.geometry("400x400")
#---------------------------------------------# 
    etiqueta_t = tk.Label(subventana, text = "Ingresa El Titulo: ")
    etiqueta_t.place(relx=0.5, rely=0.4, anchor= "center")
    entrada_t = tk.Entry(subventana)
    entrada_t.place(relx=0.5, rely=0.45, anchor= "center")
#---------------------------------------------# 
    def p(): #prestar
        t = entrada_t.get() #titulo
        Bibliotec.prestarPorTitulo(t)
        print("libro guardado")

    b_g = tk.Button(subventana, text= ("Guardar"), width= 8, height= 2, command= p)
    b_g.place(relx=0.5, rely=0.9, anchor= "center")

boton = tk.Button(ventana, text= ("Prestar Libros"), width= 30, height= 5, command = p_l)
boton.place(relx=0.5, rely=0.7, anchor= "center")

#----------------------------------------------------#

#------------------ Boton "devoler_libros" ------------------#
def d_l(): #devolver_libros
    subventana = tk.Toplevel(ventana)
    subventana.title("Devolver Libro")
    subventana.geometry("400x400")
#---------------------------------------------# 
    etiqueta_t = tk.Label(subventana, text = "Ingresa El Titulo: ")
    etiqueta_t.place(relx=0.5, rely=0.4, anchor= "center")
    entrada_t = tk.Entry(subventana)
    entrada_t.place(relx=0.5, rely=0.45, anchor= "center")
#---------------------------------------------# 
    def d(): #devolver
        t = entrada_t.get() #titulo
        Bibliotec.devolverPorTitulo(t)
        print("libro devolvido")

    b_g = tk.Button(subventana, text= ("Guardar"), width= 8, height= 2, command= d)
    b_g.place(relx=0.5, rely=0.9, anchor= "center")

boton = tk.Button(ventana, text= ("Devolver Libros"), width= 30, height= 5, command = d_l)
boton.place(relx=0.5, rely=0.9, anchor= "center")

#----------------------------------------------------#

#------------------ Resultado ------------------#
etiqueta_resultado = tk.Label(ventana)
etiqueta_resultado.place(x=500, y=200)
#-----------------------------------------------#

ventana.mainloop() #Permite hacer loop infinito
