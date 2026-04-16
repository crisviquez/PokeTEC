from tkinter import *
import time
from os import path
import vlc
import random

WIDTH = 1280
HEIGHT = 720
BGCOLOR = '#1B0664'
FUENTE = 'Minecraft'

VENTANA = Tk()
VENTANA.minsize(WIDTH, HEIGHT)
VENTANA.title('PokeTEC')

# Pantalla principal

Pantalla_principal = Canvas(VENTANA, bg=BGCOLOR, width=WIDTH, height=HEIGHT, highlightthickness=0)
Pantalla_principal.place(x=0,y=0)

# Funcion cargar png
def CargarImagen(png, carpeta):
    ruta = path.join(f'Media\{carpeta}', png)
    img = PhotoImage(file=ruta)
    return img

# Cargar fondo
Pantalla_principal.fondo = CargarImagen('PantallaInicial.png', 'Fondos')
Pantalla_principal.create_image(0, 0, anchor=NW, image=Pantalla_principal.fondo) # Mostrar fondo

# Cargar Titutlos
Pantalla_principal.titulo = CargarImagen('PokeTEC_Logo.png', 'Titulos')
Pantalla_principal.create_image(360,20, anchor=NW, image=Pantalla_principal.titulo)


# Boton Jugar
bghovercolor = '#192301'
fontcolor = '#f1f1f1'
px = PhotoImage(width=1, height=1)
Btn_jugar = Button(Pantalla_principal, text='JUGAR'
                   , width=487, height=50, 
                   bg="#4A8ABA",image=px, 
                   compound=CENTER, font=(FUENTE, 20), 
                   borderwidth=10, relief="raised", 
                   activebackground=bghovercolor, fg=fontcolor, 
                   activeforeground=fontcolor)
Btn_jugar.place(x=100, y=480)

Btn_jugar = Button(Pantalla_principal, text='PUNTACIONES'
                   , width=487, height=50, 
                   bg="#964ABA",image=px, 
                   compound=CENTER, font=(FUENTE, 20), 
                   borderwidth=10, relief="raised", 
                   activebackground=bghovercolor, fg=fontcolor, 
                   activeforeground=fontcolor)

Btn_jugar.place(x=690, y=480)


VENTANA.mainloop()