from tkinter import *
import time
from os import path
import vlc
import random

WIDTH = 1280
HEIGHT = 720
BGCOLOR = '#1a1a2e'
FUENTE = 'Minecraft'

VENTANA = Tk()
VENTANA.minsize(WIDTH, HEIGHT)
VENTANA.title('PokeTEC')

# Pantalla principal

Pantalla_principal = Canvas(VENTANA, bg=BGCOLOR, width=WIDTH, height=HEIGHT, highlightthickness=0)
Pantalla_principal.place(x=0,y=0)

'''
FUNCIONES PRINCIPALES
---------------------------------------------------------------------
'''

# Funcion cargar png
def CargarImagen(png, carpeta):
    ruta = path.join(f'Media\{carpeta}', png)
    img = PhotoImage(file=ruta)
    return img

def CargarMP3(mp3, carpeta):
    return path.join(f'Media/{carpeta}', mp3 )

def ReproducirSFX(MP3):
    vlc.MediaPlayer(MP3).play()

def ReproducirBeep():
    ReproducirSFX(CargarMP3('SFX_beep.mp3', 'SFX'))

pantalla_actual = Pantalla_principal
def CambiarPantalla(nueva):
    global pantalla_actual

    pantalla_actual.place_forget()

    nueva.place(x=0,y=0)
    pantalla_actual = nueva 

# Cargar fondo
Pantalla_principal.fondo = CargarImagen('PantallaInicial.png', 'Fondos')
Pantalla_principal.create_image(0, 0, anchor=NW, image=Pantalla_principal.fondo) # Mostrar fondo


# Cargar Titutlos
Pantalla_principal.titulo = CargarImagen('PokeTEC_Logo.png', 'Titulos')
Pantalla_principal.create_image(360,20, anchor=NW, image=Pantalla_principal.titulo)


px = PhotoImage(width=1, height=1) # Pixeles para tamano de botones


# Boton Jugar
def FUNC_Btn_jugar():
    ReproducirBeep()
    CambiarPantalla(Pantalla_nombre_avatar)

Btn_jugar = Button(Pantalla_principal, text='JUGAR'
                   , width=487, height=50, 
                   bg="#4A8ABA",image=px, 
                   compound=CENTER, font=(FUENTE, 20), 
                   borderwidth=10, relief="raised", 
                   activebackground='#192301', fg='#f1f1f1', 
                   activeforeground='#f1f1f1', command=FUNC_Btn_jugar)
Btn_jugar.place(x=100, y=480)




# Boton Puntuaciones

def FUNC_Btn_puntuaciones():
    ReproducirBeep()

Btn_puntuaciones = Button(Pantalla_principal, text='PUNTACIONES'
                   , width=487, height=50, 
                   bg="#964ABA",image=px, 
                   compound=CENTER, font=(FUENTE, 20), 
                   borderwidth=10, relief="raised", 
                   activebackground='#192301', fg='#f1f1f1', 
                   activeforeground='#f1f1f1', command=FUNC_Btn_puntuaciones)
Btn_puntuaciones.place(x=690, y=480)


# PANTALLA NOMBRE Y AVATAR
Pantalla_nombre_avatar = Canvas(VENTANA, bg=BGCOLOR, width=WIDTH, height=HEIGHT, highlightthickness=0)



VENTANA.mainloop()