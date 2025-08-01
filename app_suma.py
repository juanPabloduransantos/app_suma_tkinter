# Se imprta la libreria tkinter con todas sus funciones
from tkinter import *

# -----------------------------
# funciones de la app
# -----------------------------


# -----------------------------
# Ventana principal de la app
# -----------------------------

# Se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto de tipo Tk()

ventana_pricipal = Tk()

# Titulo de la ventana
ventana_pricipal.title("Juan Pablo Duran Santos")

# Tamaño de la ventana
ventana_pricipal.geometry("800x500")

# deshabilitar boton maximizar de la ventana
ventana_pricipal.resizable(0,0)

#color de fondo de la ventana
ventana_pricipal.config(bg="black")

# ------------------------
# Variables globales
#-------------------------
a = StringVar()
b = StringVar()
c = IntVar()

# ------------------
# Frame 1
# ------------------

frame_1 = Frame(ventana_pricipal)
frame_1.config(bg="ivory2", width=780, height=240)
frame_1.place(x=10,y=10)

# Etiqueta para subtitulo 1 de la app
subtitulo1 = Label(frame_1, text="Especialidad en Sistemas")
subtitulo1.config(bg="yellow", fg="blue", font=("Arial",12))
subtitulo1.place(x=390,y=40)

# Etiqueta para subtitulo 2 de la app
subtitulo2 = Label(frame_1, text="SUMA DE DOS ENTEROS")
subtitulo2.config(bg="ivory2", fg="blue", font=("Arial", 15), anchor=CENTER)
subtitulo2.place(x=390,y=70)

# Etiqueta para el valor - a
Label_a = Label(frame_1, text = "a = ")
Label_a.config(bg="ivory2", fg="blue", font=("Arial", 20), anchor=CENTER)
Label_a.place(x=390, y=120)

# Entry para el primer valor - a
entry_a = Entry(frame_1, width=4, textvariable=a)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=487, y= 120)

# Etiqueta para el valor - b
Label_b = Label(frame_1, text = "b = ")
Label_b.config(bg="ivory2", fg="blue", font=("Arial", 20), anchor=CENTER)
Label_b.place(x=585, y=120)

# Entry para el primer valor - b
entry_b = Entry(frame_1, width=4, textvariable=b)
entry_b.config(font=("Arial", 20), justify=CENTER)
entry_b.place(x=682, y= 120)

# imagen - logo de la app
logo = PhotoImage(file="img/btn-suma.png")
label_logo = Label(frame_1, image=logo)
label_logo.place(x=10, y=10)

# Etiqueta para el titulo de la app
titulo = Label(frame_1, text="Colegio san jose delguanenta")
titulo.config(bg="yellow", fg= "blue", font=("Arial", 16))
titulo.place(x=390,y=10)

# ------------------
# Frame 2 - operaciones
# ------------------

frame_2 = Frame(ventana_pricipal)
frame_2.config(bg="ivory2", width=780, height=120)
frame_2.place(x=10,y=260)

# ------------------
# Frame 3 - resultados
# ------------------

frame_3 = Frame(ventana_pricipal)
frame_3.config(bg="ivory2", width=780, height=100)
frame_3.place(x=10,y=390)

# Metodo principal que despliega la ventana en pantalla
ventana_pricipal.mainloop()