from tkinter import *
import time
from os import path
import vlc
import random

WIDTH = 1280
HEIGHT = 720
BGCOLOR = '#1a1a2e'
FUENTE = 'Minecraft'
NOMBRE = ''
AVATAR = ''

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


# Cargar avatares
Pantalla_nombre_avatar.AVT_LaCobra = CargarImagen('AVT_LaCobra.png', 'Avatares')
Pantalla_nombre_avatar.AVT_Messi = CargarImagen('AVT_Messi.png', 'Avatares')
Pantalla_nombre_avatar.AVT_BadBunny = CargarImagen('AVT_BadBunny.png', 'Avatares')
Pantalla_nombre_avatar.AVT_Speed = CargarImagen('AVT_Speed.png', 'Avatares')
Pantalla_nombre_avatar.AVT_Goku = CargarImagen('AVT_Goku.png', 'Avatares')

# Poner avatares
Pantalla_nombre_avatar.create_image(59,72, anchor=NW, image=Pantalla_nombre_avatar.AVT_LaCobra, )
Pantalla_nombre_avatar.create_image(298,72, anchor=NW, image=Pantalla_nombre_avatar.AVT_Messi)
Pantalla_nombre_avatar.create_image(537,72, anchor=NW, image=Pantalla_nombre_avatar.AVT_BadBunny)
Pantalla_nombre_avatar.create_image(776,72, anchor=NW, image=Pantalla_nombre_avatar.AVT_Speed)
Pantalla_nombre_avatar.create_image(1015,72, anchor=NW, image=Pantalla_nombre_avatar.AVT_Goku)


# FUNCIONES BOTONES CONFIRMAR

borde_activo = None


def FUNC_Btn_confirmar_lacobra():
    global AVATAR
    global borde_activo

    AVATAR = 'LaCobra'

    ReproducirBeep()

    if borde_activo != None:
        Pantalla_nombre_avatar.delete(borde_activo)

    borde_activo = Pantalla_nombre_avatar.create_rectangle(
    59-2, 72-2, 59+206+2, 72+262+2,
    outline="#1fb4ff", width=4
)
    
def FUNC_Btn_confirmar_messi():
    global AVATAR
    global borde_activo

    AVATAR = 'Messi'

    ReproducirBeep()

    if borde_activo != None:
        Pantalla_nombre_avatar.delete(borde_activo)

    borde_activo = Pantalla_nombre_avatar.create_rectangle(
    298-2, 72-2, 298+206+2, 72+262+2,
    outline="#1fb4ff", width=4
)
    
def FUNC_Btn_confirmar_badbunny():
    global AVATAR
    global borde_activo

    AVATAR = 'BadBunny'

    ReproducirBeep()

    if borde_activo != None:
        Pantalla_nombre_avatar.delete(borde_activo)

    borde_activo = Pantalla_nombre_avatar.create_rectangle(
    537-2, 72-2, 537+206+2, 72+262+2,
    outline="#1fb4ff", width=4
)

    
def FUNC_Btn_confirmar_speed():
    global AVATAR
    global borde_activo

    AVATAR = 'Speed'

    ReproducirBeep()

    if borde_activo != None:
        Pantalla_nombre_avatar.delete(borde_activo)

    borde_activo = Pantalla_nombre_avatar.create_rectangle(
    776-2, 72-2, 776+206+2, 72+262+2,
    outline="#1fb4ff", width=4
)
    
def FUNC_Btn_confirmar_goku():
    global AVATAR
    global borde_activo

    AVATAR = 'Goku'

    ReproducirBeep()

    if borde_activo != None:
        Pantalla_nombre_avatar.delete(borde_activo)

    borde_activo = Pantalla_nombre_avatar.create_rectangle(
    1015-2, 72-2, 1015+206+2, 72+262+2,
    outline="#1fb4ff", width=4
)
    
# Botones Confirmar

# Boton Confirmar La Cobra
Btn_confirmar_lacobra = Button(Pantalla_nombre_avatar, text='Confirmar'
                   , width=206 - 20, height=47, 
                   bg="#3A368A",image=px, 
                   compound=CENTER, font=(FUENTE, 20), 
                   borderwidth=10, relief="raised", 
                   activebackground='#192301', fg='#f1f1f1', 
                   activeforeground='#f1f1f1', command=FUNC_Btn_confirmar_lacobra)
Btn_confirmar_lacobra.place(x=59,y=360)

# Boton Confirmar Messi
Btn_confirmar_messi = Button(Pantalla_nombre_avatar, text='Confirmar'
                   , width=206 - 20, height=47, 
                   bg="#3A368A",image=px, 
                   compound=CENTER, font=(FUENTE, 20), 
                   borderwidth=10, relief="raised", 
                   activebackground='#192301', fg='#f1f1f1', 
                   activeforeground='#f1f1f1', command=FUNC_Btn_confirmar_messi)
Btn_confirmar_messi.place(x=298,y=360)

Btn_confirmar_badbunny = Button(Pantalla_nombre_avatar, text='Confirmar'
                   , width=206 - 20, height=47, 
                   bg="#3A368A",image=px, 
                   compound=CENTER, font=(FUENTE, 20), 
                   borderwidth=10, relief="raised", 
                   activebackground='#192301', fg='#f1f1f1', 
                   activeforeground='#f1f1f1', command=FUNC_Btn_confirmar_badbunny)
Btn_confirmar_badbunny.place(x=537,y=360)

Btn_confirmar_speed = Button(Pantalla_nombre_avatar, text='Confirmar'
                   , width=206 - 20, height=47, 
                   bg="#3A368A",image=px, 
                   compound=CENTER, font=(FUENTE, 20), 
                   borderwidth=10, relief="raised", 
                   activebackground='#192301', fg='#f1f1f1', 
                   activeforeground='#f1f1f1', command=FUNC_Btn_confirmar_speed)
Btn_confirmar_speed.place(x=776,y=360)

Btn_confirmar_goku = Button(Pantalla_nombre_avatar, text='Confirmar'
                   , width=206 - 20, height=47, 
                   bg="#3A368A",image=px, 
                   compound=CENTER, font=(FUENTE, 20), 
                   borderwidth=10, relief="raised", 
                   activebackground='#192301', fg='#f1f1f1', 
                   activeforeground='#f1f1f1', command=FUNC_Btn_confirmar_goku)
Btn_confirmar_goku.place(x=1015,y=360)

VENTANA.mainloop()