from tkinter import *
from tkinter import messagebox
from os import path
import vlc
import random
import os
import json

WIDTH = 1280
HEIGHT = 720
BGCOLOR = '#1a1a2e'
FUENTE = 'Minecraft'
NOMBRE = ''
AVATAR = ''
POKEMONES = []

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
    ruta = path.join(f'Media/{carpeta}', png)
    img = PhotoImage(file=ruta)
    return img

def CargarMP3(mp3, carpeta):
    return path.join(f'Media/{carpeta}', mp3 )

def ReproducirSFX(MP3):
    vlc.MediaPlayer(MP3).play()

def ReproducirBeep():
    ReproducirSFX(CargarMP3('SFX_beep.mp3', 'SFX'))

reproductor = vlc.MediaPlayer()
def ReproducirCancion(MP3):
    global reproductor
    DetenerCancion()
    reproductor = vlc.MediaPlayer(MP3)
    reproductor.audio_set_volume(100)
    reproductor.play()

def DetenerCancion():
    if(isinstance(reproductor,vlc.MediaPlayer)):
        reproductor.stop()

def ReproducirCancionLaCobra():
    ReproducirCancion(CargarMP3('LaCobra.mp3', 'Musica'))

def ReproducirCancionMessi():
    ReproducirCancion(CargarMP3('Messi.mp3', 'Musica'))

def ReproducirCancionBadBunny():
    ReproducirCancion(CargarMP3('BadBunny.mp3', 'Musica'))

def ReproducirCancionSpeed():
    ReproducirCancion(CargarMP3('Speed.mp3', 'Musica'))

def ReproducirCancionGoku():
    ReproducirCancion(CargarMP3('Goku.mp3', 'Musica'))


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
    global Pantalla_puntajes
    ReproducirBeep()
    CambiarPantallaPuntajes(Pantalla_puntajes)

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


# Entrada Nombre
Ent_Nombre_Jugador = Entry(Pantalla_nombre_avatar, 
                           width=20,font=(FUENTE, 40), 
                           bg="#131313", border=15,
                           fg="#E7E7E7", )
Ent_Nombre_Jugador.place(x=58,y=448)


def GuardarNombre():
    global NOMBRE
    ReproducirBeep()
    NOMBRE = Ent_Nombre_Jugador.get()
    

Btn_confirmar_nombre = Button(Pantalla_nombre_avatar, text='Confirmar \n Nombre'
                   , width=490, height=62, 
                   bg="#5852CD",image=px, 
                   compound=CENTER, font=(FUENTE, 20), 
                   borderwidth=10, relief="raised", 
                   activebackground='#192301', fg='#f1f1f1', 
                   activeforeground='#f1f1f1', command=GuardarNombre)
Btn_confirmar_nombre.place(x=710,y=448)


def FUNC_Btn_volver_pantalla_principal():
    ReproducirBeep()
    CambiarPantalla(Pantalla_principal)

Btn_volver_pantalla_principal = Button(Pantalla_nombre_avatar, 
                    text='Volver Pantalla Inicial', 
                    width=400, height=47, 
                   bg="#8A3664",image=px, 
                   compound=CENTER, font=(FUENTE, 20), 
                   borderwidth=10, relief="raised", 
                   activebackground='#192301', fg='#f1f1f1', 
                   activeforeground='#f1f1f1', command=FUNC_Btn_volver_pantalla_principal)
Btn_volver_pantalla_principal.place(x=58, y=550)




def FUNC_Btn_ir_a_escoger_pokemones():

    global NOMBRE, AVATAR
    if NOMBRE != '' and AVATAR != '':
        ReproducirBeep()
        CambiarPantalla(Pantalla_escoger_pokemones)
    else:
        if NOMBRE == '':
            messagebox.showwarning("Atención", "DEBES INGRESAR UN NOMBRE")
        elif AVATAR == '':
            messagebox.showwarning("Atención", "DEBES ESCOGER UN AVATAR")

            
Btn_ir_a_escoger_pokemones = Button(Pantalla_nombre_avatar, 
                    text='SIGUIENTE', 
                    width=490, height=47, 
                   bg="#8A363E",image=px, 
                   compound=CENTER, font=(FUENTE, 20), 
                   borderwidth=10, relief="raised", 
                   activebackground='#192301', fg='#f1f1f1', 
                   activeforeground='#f1f1f1', command=FUNC_Btn_ir_a_escoger_pokemones)

Btn_ir_a_escoger_pokemones.place(x=710, y=550)







'''
PANTALLA ESCOGER POKEMONES
'''
PokemonsSeleccionados = []


# Crear Pantalla Escoger Pokemones
Pantalla_escoger_pokemones = Canvas(VENTANA, bg=BGCOLOR, width=WIDTH, height=HEIGHT, highlightthickness=0)

Lbl_Cant_Poke_Info = Label(Pantalla_escoger_pokemones, text='0 / 3  elegidos',
                   font=('Minecraft', 20), bg='#1a1a2e', fg='#7f7fc8')
Lbl_Cant_Poke_Info.place(x=550, y=25)

def ActualizarContador():
    n = len(PokemonsSeleccionados)

    Lbl_Cant_Poke_Info.config(text=f'{n} / 3 elegidos')

    if n == 3:
        Lbl_Cant_Poke_Info.config(fg="#7fc881")
    else:
        Lbl_Cant_Poke_Info.config(fg='#7f7fc8')




# 1r Pokemon (Awachalot)
Seleccionar_Pokemon_Awachalot = Canvas(Pantalla_escoger_pokemones, width=208, height=250 - 20, bg="#29293F")
Seleccionar_Pokemon_Awachalot.place(x=67,y=111 -30)

Seleccionar_Pokemon_Awachalot.img = CargarImagen('Awachaloth_blue_bg.png', 'Pokemones')
Seleccionar_Pokemon_Awachalot.create_image(10, 10, anchor=NW, image=Seleccionar_Pokemon_Awachalot.img)

Lbl_Awachalot = Label(Seleccionar_Pokemon_Awachalot, font=('Minecraft', 10), text='Awachalot', fg='#f1f1f1', bg='#29293F')
Lbl_Awachalot.place(x=75,y=170)


borde_awachalot = None
def FUNC_Btn_seleccionar_Awachalot():
    ReproducirBeep()
    global borde_awachalot
    global PokemonsSeleccionados
    pokemon = 'Awachalot'

    if len(PokemonsSeleccionados) >= 3:
        messagebox.showwarning('ATENCION', 'YA TIENES 3 POKEMONES SELECCIONADOS')
        return 
    if pokemon in PokemonsSeleccionados:
        messagebox.showwarning('ATENCION', 'NO PUEDES ESCOGER AL MISMO POKEMON MAS VECES')
        return 
    else:
        PokemonsSeleccionados.append(pokemon)
        borde_awachalot = Pantalla_escoger_pokemones.create_rectangle(67,111-30, 67+208 +4, 111 - 30 + 250 - 20 + 4, outline="#1fb4ff", width=8)
        ActualizarContador()

Btn_seleccionar_Awachalot = Button(Seleccionar_Pokemon_Awachalot,
                                   font=('Minecraft', 10), 
                                   text='Selecionar', fg='#f1f1f1', 
                                   bg='#29293F', width=84, image=px, height=20,
                                   compound=CENTER, command=FUNC_Btn_seleccionar_Awachalot)
Btn_seleccionar_Awachalot.place(x=10, y=195)

def FUNC_Btn_deseleccionar_Awachalot():
    ReproducirBeep()
    pokemon = 'Awachalot'
    global PokemonsSeleccionados
    global borde_awachalot

    if pokemon in PokemonsSeleccionados:
        PokemonsSeleccionados.remove(pokemon)
        Pantalla_escoger_pokemones.delete(borde_awachalot)
    ActualizarContador()
    return None
Btn_deseleccionar_Awachalot = Button(Seleccionar_Pokemon_Awachalot,
                                   font=('Minecraft', 10), 
                                   text='Deseleccionar', fg='#f1f1f1', 
                                   bg='#29293F', width=84, image=px, height=20,
                                   compound=CENTER, command=FUNC_Btn_deseleccionar_Awachalot)
Btn_deseleccionar_Awachalot.place(x=110, y=195)




# 2 Pokemon (Volcafrog)
Seleccionar_Pokemon_Volcafrog = Canvas(Pantalla_escoger_pokemones, width=208, height=250 - 20, bg="#29293F")
Seleccionar_Pokemon_Volcafrog.place(x=67 + 1*(230),y=111 -30)

Seleccionar_Pokemon_Volcafrog.img = CargarImagen('Volcafrog_blue_bg.png', 'Pokemones')
Seleccionar_Pokemon_Volcafrog.create_image(10, 10, anchor=NW, image=Seleccionar_Pokemon_Volcafrog.img)

Lbl_Volcafrog = Label(Seleccionar_Pokemon_Volcafrog, font=('Minecraft', 10), text='Volcafrog', fg='#f1f1f1', bg='#29293F')
Lbl_Volcafrog.place(x=75,y=170)


borde_volcafrog = None
def FUNC_Btn_seleccionar_Volcafrog():
    ReproducirBeep()
    global borde_volcafrog
    global PokemonsSeleccionados
    pokemon = 'Volcafrog'

    if len(PokemonsSeleccionados) >= 3:
        messagebox.showwarning('ATENCION', 'YA TIENES 3 POKEMONES SELECCIONADOS')
        return 
    if pokemon in PokemonsSeleccionados:
        messagebox.showwarning('ATENCION', 'NO PUEDES ESCOGER AL MISMO POKEMON MAS VECES')
        return 
    else:
        PokemonsSeleccionados.append(pokemon)
        borde_volcafrog = Pantalla_escoger_pokemones.create_rectangle(67 + 1*(230),111-30, 67+208 +4 + 1*(230), 111 - 30 + 250 - 20 + 4, outline="#1fb4ff", width=8)
        ActualizarContador()

Btn_seleccionar_Volcafrog = Button(Seleccionar_Pokemon_Volcafrog,
                                   font=('Minecraft', 10), 
                                   text='Selecionar', fg='#f1f1f1', 
                                   bg='#29293F', width=84, image=px, height=20,
                                   compound=CENTER, command=FUNC_Btn_seleccionar_Volcafrog)
Btn_seleccionar_Volcafrog.place(x=10, y=195)

def FUNC_Btn_deseleccionar_Volcafrog():
    ReproducirBeep()
    pokemon = 'Volcafrog'
    global PokemonsSeleccionados
    global borde_volcafrog

    if pokemon in PokemonsSeleccionados:
        PokemonsSeleccionados.remove(pokemon)
        Pantalla_escoger_pokemones.delete(borde_volcafrog)
    ActualizarContador()
    return None
Btn_deseleccionar_Volcafrog = Button(Seleccionar_Pokemon_Volcafrog,
                                   font=('Minecraft', 10), 
                                   text='Deseleccionar', fg='#f1f1f1', 
                                   bg='#29293F', width=84, image=px, height=20,
                                   compound=CENTER, command=FUNC_Btn_deseleccionar_Volcafrog)
Btn_deseleccionar_Volcafrog.place(x=110, y=195)


# 3er pokemon (Nobeltzal)
Seleccionar_Pokemon_Nobeltzal = Canvas(Pantalla_escoger_pokemones, width=208, height=250 - 20, bg="#29293F")
Seleccionar_Pokemon_Nobeltzal.place(x=67 + 2*(230), y=111 - 30)

Seleccionar_Pokemon_Nobeltzal.img = CargarImagen('Nobeltzal_blue_bg.png', 'Pokemones')
Seleccionar_Pokemon_Nobeltzal.create_image(10, 10, anchor=NW, image=Seleccionar_Pokemon_Nobeltzal.img)

Lbl_Nobeltzal = Label(Seleccionar_Pokemon_Nobeltzal, font=('Minecraft', 10), text='Nobeltzal', fg='#f1f1f1', bg='#29293F')
Lbl_Nobeltzal.place(x=75, y=170)

borde_nobeltzal = None
def FUNC_Btn_seleccionar_Nobeltzal():
    ReproducirBeep()
    global borde_nobeltzal
    global PokemonsSeleccionados
    pokemon = 'Nobeltzal'

    if len(PokemonsSeleccionados) >= 3:
        messagebox.showwarning('ATENCION', 'YA TIENES 3 POKEMONES SELECCIONADOS')
        return
    if pokemon in PokemonsSeleccionados:
        messagebox.showwarning('ATENCION', 'NO PUEDES ESCOGER AL MISMO POKEMON MAS VECES')
        return
    else:
        PokemonsSeleccionados.append(pokemon)
        borde_nobeltzal = Pantalla_escoger_pokemones.create_rectangle(67 + 2*(230), 111-30, 67+208+4 + 2*(230), 111-30+250-20+4, outline="#1fb4ff", width=8)
        ActualizarContador()

Btn_seleccionar_Nobeltzal = Button(Seleccionar_Pokemon_Nobeltzal,
                                   font=('Minecraft', 10),
                                   text='Selecionar', fg='#f1f1f1',
                                   bg='#29293F', width=84, image=px, height=20,
                                   compound=CENTER, command=FUNC_Btn_seleccionar_Nobeltzal)
Btn_seleccionar_Nobeltzal.place(x=10, y=195)

def FUNC_Btn_deseleccionar_Nobeltzal():
    ReproducirBeep()
    pokemon = 'Nobeltzal'
    global PokemonsSeleccionados
    global borde_nobeltzal

    if pokemon in PokemonsSeleccionados:
        PokemonsSeleccionados.remove(pokemon)
        Pantalla_escoger_pokemones.delete(borde_nobeltzal)
    ActualizarContador()
    return None

Btn_deseleccionar_Nobeltzal = Button(Seleccionar_Pokemon_Nobeltzal,
                                   font=('Minecraft', 10),
                                   text='Deseleccionar', fg='#f1f1f1',
                                   bg='#29293F', width=84, image=px, height=20,
                                   compound=CENTER, command=FUNC_Btn_deseleccionar_Nobeltzal)
Btn_deseleccionar_Nobeltzal.place(x=110, y=195)


# 4to pokemon (Morphosa)
Seleccionar_Pokemon_Morphosa = Canvas(Pantalla_escoger_pokemones, width=208, height=250 - 20, bg="#29293F")
Seleccionar_Pokemon_Morphosa.place(x=67 + 3*(230), y=111 - 30)

Seleccionar_Pokemon_Morphosa.img = CargarImagen('Morphosa_blue_bg.png', 'Pokemones')
Seleccionar_Pokemon_Morphosa.create_image(10, 10, anchor=NW, image=Seleccionar_Pokemon_Morphosa.img)

Lbl_Morphosa = Label(Seleccionar_Pokemon_Morphosa, font=('Minecraft', 10), text='Morphosa', fg='#f1f1f1', bg='#29293F')
Lbl_Morphosa.place(x=75, y=170)

borde_morphosa = None
def FUNC_Btn_seleccionar_Morphosa():
    ReproducirBeep()
    global borde_morphosa
    global PokemonsSeleccionados
    pokemon = 'Morphosa'

    if len(PokemonsSeleccionados) >= 3:
        messagebox.showwarning('ATENCION', 'YA TIENES 3 POKEMONES SELECCIONADOS')
        return
    if pokemon in PokemonsSeleccionados:
        messagebox.showwarning('ATENCION', 'NO PUEDES ESCOGER AL MISMO POKEMON MAS VECES')
        return
    else:
        PokemonsSeleccionados.append(pokemon)
        borde_morphosa = Pantalla_escoger_pokemones.create_rectangle(67 + 3*(230), 111-30, 67+208+4 + 3*(230), 111-30+250-20+4, outline="#1fb4ff", width=8)
        ActualizarContador()

Btn_seleccionar_Morphosa = Button(Seleccionar_Pokemon_Morphosa,
                                   font=('Minecraft', 10),
                                   text='Selecionar', fg='#f1f1f1',
                                   bg='#29293F', width=84, image=px, height=20,
                                   compound=CENTER, command=FUNC_Btn_seleccionar_Morphosa)
Btn_seleccionar_Morphosa.place(x=10, y=195)

def FUNC_Btn_deseleccionar_Morphosa():
    ReproducirBeep()
    pokemon = 'Morphosa'
    global PokemonsSeleccionados
    global borde_morphosa

    if pokemon in PokemonsSeleccionados:
        PokemonsSeleccionados.remove(pokemon)
        Pantalla_escoger_pokemones.delete(borde_morphosa)
    ActualizarContador()
    return None

Btn_deseleccionar_Morphosa = Button(Seleccionar_Pokemon_Morphosa,
                                   font=('Minecraft', 10),
                                   text='Deseleccionar', fg='#f1f1f1',
                                   bg='#29293F', width=84, image=px, height=20,
                                   compound=CENTER, command=FUNC_Btn_deseleccionar_Morphosa)
Btn_deseleccionar_Morphosa.place(x=110, y=195)


# 5to pokemon (Gladhuitl)
Seleccionar_Pokemon_Gladhuitl = Canvas(Pantalla_escoger_pokemones, width=208, height=250 - 20, bg="#29293F")
Seleccionar_Pokemon_Gladhuitl.place(x=67 + 4*(230), y=111 - 30)

Seleccionar_Pokemon_Gladhuitl.img = CargarImagen('Gladhuitl_blue_bg.png', 'Pokemones')
Seleccionar_Pokemon_Gladhuitl.create_image(10, 10, anchor=NW, image=Seleccionar_Pokemon_Gladhuitl.img)

Lbl_Gladhuitl = Label(Seleccionar_Pokemon_Gladhuitl, font=('Minecraft', 10), text='Gladhuitl', fg='#f1f1f1', bg='#29293F')
Lbl_Gladhuitl.place(x=75, y=170)

borde_gladhuitl = None
def FUNC_Btn_seleccionar_Gladhuitl():
    ReproducirBeep()
    global borde_gladhuitl
    global PokemonsSeleccionados
    pokemon = 'Gladhuitl'

    if len(PokemonsSeleccionados) >= 3:
        messagebox.showwarning('ATENCION', 'YA TIENES 3 POKEMONES SELECCIONADOS')
        return
    if pokemon in PokemonsSeleccionados:
        messagebox.showwarning('ATENCION', 'NO PUEDES ESCOGER AL MISMO POKEMON MAS VECES')
        return
    else:
        PokemonsSeleccionados.append(pokemon)
        borde_gladhuitl = Pantalla_escoger_pokemones.create_rectangle(67 + 4*(230), 111-30, 67+208+4 + 4*(230), 111-30+250-20+4, outline="#1fb4ff", width=8)
        ActualizarContador()

Btn_seleccionar_Gladhuitl = Button(Seleccionar_Pokemon_Gladhuitl,
                                   font=('Minecraft', 10),
                                   text='Selecionar', fg='#f1f1f1',
                                   bg='#29293F', width=84, image=px, height=20,
                                   compound=CENTER, command=FUNC_Btn_seleccionar_Gladhuitl)
Btn_seleccionar_Gladhuitl.place(x=10, y=195)

def FUNC_Btn_deseleccionar_Gladhuitl():
    ReproducirBeep()
    pokemon = 'Gladhuitl'
    global PokemonsSeleccionados
    global borde_gladhuitl

    if pokemon in PokemonsSeleccionados:
        PokemonsSeleccionados.remove(pokemon)
        Pantalla_escoger_pokemones.delete(borde_gladhuitl)
    ActualizarContador()
    return None

Btn_deseleccionar_Gladhuitl = Button(Seleccionar_Pokemon_Gladhuitl,
                                   font=('Minecraft', 10),
                                   text='Deseleccionar', fg='#f1f1f1',
                                   bg='#29293F', width=84, image=px, height=20,
                                   compound=CENTER, command=FUNC_Btn_deseleccionar_Gladhuitl)
Btn_deseleccionar_Gladhuitl.place(x=110, y=195)


# 6to pokemon (Elchemy)
Seleccionar_Pokemon_Elchemy = Canvas(Pantalla_escoger_pokemones, width=208, height=250 - 20, bg="#29293F")
Seleccionar_Pokemon_Elchemy.place(x=67, y=386 - 30 - 20)

Seleccionar_Pokemon_Elchemy.img = CargarImagen('Elchemy_blue_bg.png', 'Pokemones')
Seleccionar_Pokemon_Elchemy.create_image(10, 10, anchor=NW, image=Seleccionar_Pokemon_Elchemy.img)

Lbl_Elchemy = Label(Seleccionar_Pokemon_Elchemy, font=('Minecraft', 10), text='Elchemy', fg='#f1f1f1', bg='#29293F')
Lbl_Elchemy.place(x=75, y=170)

borde_elchemy = None
def FUNC_Btn_seleccionar_Elchemy():
    ReproducirBeep()
    global borde_elchemy
    global PokemonsSeleccionados
    pokemon = 'Elchemy'

    if len(PokemonsSeleccionados) >= 3:
        messagebox.showwarning('ATENCION', 'YA TIENES 3 POKEMONES SELECCIONADOS')
        return
    if pokemon in PokemonsSeleccionados:
        messagebox.showwarning('ATENCION', 'NO PUEDES ESCOGER AL MISMO POKEMON MAS VECES')
        return
    else:
        PokemonsSeleccionados.append(pokemon)
        borde_elchemy = Pantalla_escoger_pokemones.create_rectangle(67, 386-30-20, 67+208+4, 386-30-20+250-20+4, outline="#1fb4ff", width=8)
        ActualizarContador()

Btn_seleccionar_Elchemy = Button(Seleccionar_Pokemon_Elchemy,
                                   font=('Minecraft', 10),
                                   text='Selecionar', fg='#f1f1f1',
                                   bg='#29293F', width=84, image=px, height=20,
                                   compound=CENTER, command=FUNC_Btn_seleccionar_Elchemy)
Btn_seleccionar_Elchemy.place(x=10, y=195)

def FUNC_Btn_deseleccionar_Elchemy():
    ReproducirBeep()
    pokemon = 'Elchemy'
    global PokemonsSeleccionados
    global borde_elchemy

    if pokemon in PokemonsSeleccionados:
        PokemonsSeleccionados.remove(pokemon)
        Pantalla_escoger_pokemones.delete(borde_elchemy)
    ActualizarContador()
    return None

Btn_deseleccionar_Elchemy = Button(Seleccionar_Pokemon_Elchemy,
                                   font=('Minecraft', 10),
                                   text='Deseleccionar', fg='#f1f1f1',
                                   bg='#29293F', width=84, image=px, height=20,
                                   compound=CENTER, command=FUNC_Btn_deseleccionar_Elchemy)
Btn_deseleccionar_Elchemy.place(x=110, y=195)


# 7mo pokemon (Houndsoul)
Seleccionar_Pokemon_Houndsoul = Canvas(Pantalla_escoger_pokemones, width=208, height=250 - 20, bg="#29293F")
Seleccionar_Pokemon_Houndsoul.place(x=67 + 1*(230), y=386 - 30 - 20)

Seleccionar_Pokemon_Houndsoul.img = CargarImagen('Houndsoul_blue_bg.png', 'Pokemones')
Seleccionar_Pokemon_Houndsoul.create_image(10, 10, anchor=NW, image=Seleccionar_Pokemon_Houndsoul.img)

Lbl_Houndsoul = Label(Seleccionar_Pokemon_Houndsoul, font=('Minecraft', 10), text='Houndsoul', fg='#f1f1f1', bg='#29293F')
Lbl_Houndsoul.place(x=75, y=170)

borde_houndsoul = None
def FUNC_Btn_seleccionar_Houndsoul():
    ReproducirBeep()
    global borde_houndsoul
    global PokemonsSeleccionados
    pokemon = 'Houndsoul'

    if len(PokemonsSeleccionados) >= 3:
        messagebox.showwarning('ATENCION', 'YA TIENES 3 POKEMONES SELECCIONADOS')
        return
    if pokemon in PokemonsSeleccionados:
        messagebox.showwarning('ATENCION', 'NO PUEDES ESCOGER AL MISMO POKEMON MAS VECES')
        return
    else:
        PokemonsSeleccionados.append(pokemon)
        borde_houndsoul = Pantalla_escoger_pokemones.create_rectangle(67 + 1*(230), 386-30-20, 67+208+4 + 1*(230), 386-30-20+250-20+4, outline="#1fb4ff", width=8)
        ActualizarContador()

Btn_seleccionar_Houndsoul = Button(Seleccionar_Pokemon_Houndsoul,
                                   font=('Minecraft', 10),
                                   text='Selecionar', fg='#f1f1f1',
                                   bg='#29293F', width=84, image=px, height=20,
                                   compound=CENTER, command=FUNC_Btn_seleccionar_Houndsoul)
Btn_seleccionar_Houndsoul.place(x=10, y=195)

def FUNC_Btn_deseleccionar_Houndsoul():
    ReproducirBeep()
    pokemon = 'Houndsoul'
    global PokemonsSeleccionados
    global borde_houndsoul

    if pokemon in PokemonsSeleccionados:
        PokemonsSeleccionados.remove(pokemon)
        Pantalla_escoger_pokemones.delete(borde_houndsoul)
    ActualizarContador()
    return None

Btn_deseleccionar_Houndsoul = Button(Seleccionar_Pokemon_Houndsoul,
                                   font=('Minecraft', 10),
                                   text='Deseleccionar', fg='#f1f1f1',
                                   bg='#29293F', width=84, image=px, height=20,
                                   compound=CENTER, command=FUNC_Btn_deseleccionar_Houndsoul)
Btn_deseleccionar_Houndsoul.place(x=110, y=195)


# 8vo pokemon (Flamaya)
Seleccionar_Pokemon_Flamaya = Canvas(Pantalla_escoger_pokemones, width=208, height=250 - 20, bg="#29293F")
Seleccionar_Pokemon_Flamaya.place(x=67 + 2*(230), y=386 - 30 - 20)

Seleccionar_Pokemon_Flamaya.img = CargarImagen('Flamaya_blue_bg.png', 'Pokemones')
Seleccionar_Pokemon_Flamaya.create_image(10, 10, anchor=NW, image=Seleccionar_Pokemon_Flamaya.img)

Lbl_Flamaya = Label(Seleccionar_Pokemon_Flamaya, font=('Minecraft', 10), text='Flamaya', fg='#f1f1f1', bg='#29293F')
Lbl_Flamaya.place(x=75, y=170)

borde_flamaya = None
def FUNC_Btn_seleccionar_Flamaya():
    ReproducirBeep()
    global borde_flamaya
    global PokemonsSeleccionados
    pokemon = 'Flamaya'

    if len(PokemonsSeleccionados) >= 3:
        messagebox.showwarning('ATENCION', 'YA TIENES 3 POKEMONES SELECCIONADOS')
        return
    if pokemon in PokemonsSeleccionados:
        messagebox.showwarning('ATENCION', 'NO PUEDES ESCOGER AL MISMO POKEMON MAS VECES')
        return
    else:
        PokemonsSeleccionados.append(pokemon)
        borde_flamaya = Pantalla_escoger_pokemones.create_rectangle(67 + 2*(230), 386-30-20, 67+208+4 + 2*(230), 386-30-20+250-20+4, outline="#1fb4ff", width=8)
        ActualizarContador()

Btn_seleccionar_Flamaya = Button(Seleccionar_Pokemon_Flamaya,
                                   font=('Minecraft', 10),
                                   text='Selecionar', fg='#f1f1f1',
                                   bg='#29293F', width=84, image=px, height=20,
                                   compound=CENTER, command=FUNC_Btn_seleccionar_Flamaya)
Btn_seleccionar_Flamaya.place(x=10, y=195)

def FUNC_Btn_deseleccionar_Flamaya():
    ReproducirBeep()
    pokemon = 'Flamaya'
    global PokemonsSeleccionados
    global borde_flamaya

    if pokemon in PokemonsSeleccionados:
        PokemonsSeleccionados.remove(pokemon)
        Pantalla_escoger_pokemones.delete(borde_flamaya)
    ActualizarContador()
    return None

Btn_deseleccionar_Flamaya = Button(Seleccionar_Pokemon_Flamaya,
                                   font=('Minecraft', 10),
                                   text='Deseleccionar', fg='#f1f1f1',
                                   bg='#29293F', width=84, image=px, height=20,
                                   compound=CENTER, command=FUNC_Btn_deseleccionar_Flamaya)
Btn_deseleccionar_Flamaya.place(x=110, y=195)


# 9vo pokemon (Turplane)
Seleccionar_Pokemon_Turplane = Canvas(Pantalla_escoger_pokemones, width=208, height=250 - 20, bg="#29293F")
Seleccionar_Pokemon_Turplane.place(x=67 + 3*(230), y=386 - 30 - 20)

Seleccionar_Pokemon_Turplane.img = CargarImagen('Turplane_blue_bg.png', 'Pokemones')
Seleccionar_Pokemon_Turplane.create_image(10, 10, anchor=NW, image=Seleccionar_Pokemon_Turplane.img)

Lbl_Turplane = Label(Seleccionar_Pokemon_Turplane, font=('Minecraft', 10), text='Turplane', fg='#f1f1f1', bg='#29293F')
Lbl_Turplane.place(x=75, y=170)

borde_turplane = None
def FUNC_Btn_seleccionar_Turplane():
    ReproducirBeep()
    global borde_turplane
    global PokemonsSeleccionados
    pokemon = 'Turplane'

    if len(PokemonsSeleccionados) >= 3:
        messagebox.showwarning('ATENCION', 'YA TIENES 3 POKEMONES SELECCIONADOS')
        return
    if pokemon in PokemonsSeleccionados:
        messagebox.showwarning('ATENCION', 'NO PUEDES ESCOGER AL MISMO POKEMON MAS VECES')
        return
    else:
        PokemonsSeleccionados.append(pokemon)
        borde_turplane = Pantalla_escoger_pokemones.create_rectangle(67 + 3*(230), 386-30-20, 67+208+4 + 3*(230), 386-30-20+250-20+4, outline="#1fb4ff", width=8)
        ActualizarContador()

Btn_seleccionar_Turplane = Button(Seleccionar_Pokemon_Turplane,
                                   font=('Minecraft', 10),
                                   text='Selecionar', fg='#f1f1f1',
                                   bg='#29293F', width=84, image=px, height=20,
                                   compound=CENTER, command=FUNC_Btn_seleccionar_Turplane)
Btn_seleccionar_Turplane.place(x=10, y=195)

def FUNC_Btn_deseleccionar_Turplane():
    ReproducirBeep()
    pokemon = 'Turplane'
    global PokemonsSeleccionados
    global borde_turplane

    if pokemon in PokemonsSeleccionados:
        PokemonsSeleccionados.remove(pokemon)
        Pantalla_escoger_pokemones.delete(borde_turplane)
    ActualizarContador()
    return None

Btn_deseleccionar_Turplane = Button(Seleccionar_Pokemon_Turplane,
                                   font=('Minecraft', 10),
                                   text='Deseleccionar', fg='#f1f1f1',
                                   bg='#29293F', width=84, image=px, height=20,
                                   compound=CENTER, command=FUNC_Btn_deseleccionar_Turplane)
Btn_deseleccionar_Turplane.place(x=110, y=195)


# 10mo pokemon (Pedri)
Seleccionar_Pokemon_Pedri = Canvas(Pantalla_escoger_pokemones, width=208, height=250 - 20, bg="#29293F")
Seleccionar_Pokemon_Pedri.place(x=67 + 4*(230), y=386 - 30 - 20)

Seleccionar_Pokemon_Pedri.img = CargarImagen('Pedri_blue_bg_2.png', 'Pokemones')
Seleccionar_Pokemon_Pedri.create_image(10, 10, anchor=NW, image=Seleccionar_Pokemon_Pedri.img)

Lbl_Pedri = Label(Seleccionar_Pokemon_Pedri, font=('Minecraft', 10), text='Pedri', fg='#f1f1f1', bg='#29293F')
Lbl_Pedri.place(x=75 + 10, y=170) # Ese +10 es para ajustarlo

borde_pedri = None
def FUNC_Btn_seleccionar_Pedri():
    ReproducirBeep()
    global borde_pedri
    global PokemonsSeleccionados
    pokemon = 'Pedri'

    if len(PokemonsSeleccionados) >= 3:
        messagebox.showwarning('ATENCION', 'YA TIENES 3 POKEMONES SELECCIONADOS')
        return
    if pokemon in PokemonsSeleccionados:
        messagebox.showwarning('ATENCION', 'NO PUEDES ESCOGER AL MISMO POKEMON MAS VECES')
        return
    else:
        PokemonsSeleccionados.append(pokemon)
        borde_pedri = Pantalla_escoger_pokemones.create_rectangle(67 + 4*(230), 386-30-20, 67+208+4 + 4*(230), 386-30-20+250-20+4, outline="#1fb4ff", width=8)
        ActualizarContador()

Btn_seleccionar_Pedri = Button(Seleccionar_Pokemon_Pedri,
                                   font=('Minecraft', 10),
                                   text='Selecionar', fg='#f1f1f1',
                                   bg='#29293F', width=84, image=px, height=20,
                                   compound=CENTER, command=FUNC_Btn_seleccionar_Pedri)
Btn_seleccionar_Pedri.place(x=10, y=195)

def FUNC_Btn_deseleccionar_Pedri():
    ReproducirBeep()
    pokemon = 'Pedri'
    global PokemonsSeleccionados
    global borde_pedri

    if pokemon in PokemonsSeleccionados:
        PokemonsSeleccionados.remove(pokemon)
        Pantalla_escoger_pokemones.delete(borde_pedri)
    ActualizarContador()
    return None

Btn_deseleccionar_Pedri = Button(Seleccionar_Pokemon_Pedri,
                                   font=('Minecraft', 10),
                                   text='Deseleccionar', fg='#f1f1f1',
                                   bg='#29293F', width=84, image=px, height=20,
                                   compound=CENTER, command=FUNC_Btn_deseleccionar_Pedri)
Btn_deseleccionar_Pedri.place(x=110, y=195)


def FUNC_Btn_confirmar_pokemones():
    global PokemonsSeleccionados
    global POKEMONES
    ReproducirBeep()
    if len(PokemonsSeleccionados) == 3:
        # Confirmar Pokemones
        for pokemon in PokemonsSeleccionados:
            POKEMONES.append(pokemon)

        IniciarCombate()
        CambiarPantalla(Pantalla_Combate_Pokemon)
        
    else:
        messagebox.showwarning('ADVERTENCIA', 'DEBES SELECCIONAR 3 POKEMONES')
    
Btn_confirmar_pokemones = Button(Pantalla_escoger_pokemones, 
                    text='CONFIRMAR', 
                    width=490, height=28, 
                   bg="#8A363E",image=px, 
                   compound=CENTER, font=(FUENTE, 20), 
                   borderwidth=10, relief="raised", 
                   activebackground='#192301', fg='#f1f1f1', 
                   activeforeground='#f1f1f1', command=FUNC_Btn_confirmar_pokemones)

Btn_confirmar_pokemones.place(x=378, y=580)

















'''

PANTALLA
LUCHA POKEMON

'''
DATOS_POKEMONES = {
    'Awachalot': {'vida': 120, 'ataque': 60,  'defensa': 40, 'vida_max': 120},
    'Volcafrog':  {'vida': 90,  'ataque': 80,  'defensa': 30, 'vida_max': 90},
    'Nobeltzal':  {'vida': 150, 'ataque': 40,  'defensa': 70, 'vida_max': 150},
    'Morphosa':   {'vida': 100, 'ataque': 70,  'defensa': 50, 'vida_max': 100},
    'Gladhuitl':  {'vida': 110, 'ataque': 65,  'defensa': 55, 'vida_max': 110},
    'Elchemy':    {'vida': 80,  'ataque': 100, 'defensa': 20, 'vida_max': 80},
    'Houndsoul':  {'vida': 130, 'ataque': 55,  'defensa': 60, 'vida_max': 130},
    'Flamaya':    {'vida': 95,  'ataque': 85,  'defensa': 35, 'vida_max': 95},
    'Turplane':   {'vida': 105, 'ataque': 75,  'defensa': 45, 'vida_max': 105},
    'Pedri':      {'vida': 140, 'ataque': 50,  'defensa': 80, 'vida_max': 140},
}

pokemones_jugador = {}
pokemones_rival = {}
pokemon_activo_jugador = None
pokemon_activo_rival = None
puntaje_jugador = 0
puntaje_rival = 0
turno_bloqueado = False

Pantalla_Combate_Pokemon = Canvas(VENTANA, bg="#0d0d1a", width=WIDTH, height=HEIGHT, highlightthickness=0)

def IniciarCombate():
    global pokemon_activo_jugador
    global pokemon_activo_rival
    global pokemon_activo_jugador
    global pokemon_activo_rival
    global DATOS_POKEMONES
    global puntaje_jugador
    global puntaje_rival
    global AVATAR_RIVAL

    pokemones_jugador.clear()
    pokemones_rival.clear()

    puntaje_jugador = 0
    puntaje_rival = 0

    # Pokemones del jugador
    for pokemon in POKEMONES:
        datos_originales = DATOS_POKEMONES[pokemon].copy()
        pokemones_jugador[pokemon] = datos_originales

    # Pokemones del rival
    lista_nombres_pokemones = list(DATOS_POKEMONES.keys())
    escoger_3_pokemones_random = random.sample(lista_nombres_pokemones, 3)

    for pokemon in escoger_3_pokemones_random:
        datos_originales = DATOS_POKEMONES[pokemon].copy()
        pokemones_rival[pokemon] = datos_originales


    pokemon_activo_jugador = list(pokemones_jugador.keys())[0]
    pokemon_activo_rival = list(pokemones_rival.keys())[0]

    ReproducirCancionBatalla()
    ActualizarPantalladeCombate()
    VerificarAvatar()
    MostrarMensaje(f'{NOMBRE} vs {AVATAR_RIVAL}')


def PokemonesVivos(diccionario):
    lista_vivos = []
    for nombre, stats in diccionario.items():
        if stats['vida'] > 0:
            lista_vivos.append(nombre)

    return lista_vivos


def ColorBarra(porcentaje):
    #Verde > 50%, Amarillo > 25%, Rojo <= 25
    if porcentaje > 0.5:
        return '#55c855'
    elif porcentaje > 0.25:
        return '#c8c855'
    return '#c85555'


def Atacar(atacante, defensor):
    vida_perdida = max(0, atacante['ataque'] - defensor['defensa'])
    defensor['vida'] -= vida_perdida
    if defensor['vida'] < 0:
        defensor['vida'] = 0
    return vida_perdida

def TurnoJugador():
    global turno_bloqueado
    if turno_bloqueado == True:
        return
    turno_bloqueado = True

    atacante = pokemones_jugador[pokemon_activo_jugador]
    defensor = pokemones_rival[pokemon_activo_rival]

    daño = Atacar(atacante, defensor)  # CAMBIO 1: guardar el valor retornado por Atacar()

    MostrarMensaje(f"{pokemon_activo_jugador} ataco a {pokemon_activo_rival} e hizo {daño} de daño")  # CAMBIO 2: mostrar mensaje con el daño
    ActualizarPantalladeCombate()
    VerificarKO()  # CAMBIO 3: verificar si el rival cayó en KO después del ataque del jugador

    # Solo programar turno rival si aún hay pokemones vivos de ambos lados
    if PokemonesVivos(pokemones_rival) != [] and PokemonesVivos(pokemones_jugador) != []:
        VENTANA.after(2000, TurnoRival)

        
def TurnoRival():
    global pokemon_activo_rival, turno_bloqueado

    pokemones_vivos = PokemonesVivos(pokemones_rival)

    # Si hay mas de uno vivo el rival puede cambiar (30% de prob.)
    if len(pokemones_vivos) > 1 and random.random() < 0.30:
        opciones_cambio = []
        for pokemon in pokemones_vivos:
            if pokemon != pokemon_activo_rival:
                opciones_cambio.append(pokemon)

        nuevo = random.choice(opciones_cambio)
        pokemon_activo_rival = nuevo
        MostrarMensaje(f"Rival cambio a {nuevo}")
        ActualizarPantalladeCombate()
        VerificarKO()
    else:
        # Atacar
        atacante = pokemones_rival[pokemon_activo_rival]
        defensor = pokemones_jugador[pokemon_activo_jugador]
        daño = Atacar(atacante, defensor)
        MostrarMensaje(f"{pokemon_activo_rival} ataco a {pokemon_activo_jugador} e hizo {daño} de daño ")
        ActualizarPantalladeCombate()
        VerificarKO()

    turno_bloqueado = False
    
def VerificarKO():
    global pokemon_activo_jugador
    global pokemon_activo_rival
    global puntaje_jugador
    global puntaje_rival

    rival_actual = pokemones_rival.get(pokemon_activo_rival)
    jugador_actual = pokemones_jugador.get(pokemon_activo_jugador)

    # Si rival recive KO
    if rival_actual and rival_actual['vida'] <= 0:
        puntaje_jugador += 1
        pokemon_derrotado = pokemon_activo_rival

        # Transferir pokemon al jugador
        nuevas_estadisticas = DATOS_POKEMONES[pokemon_derrotado].copy()
        pokemones_jugador[pokemon_derrotado] = nuevas_estadisticas
        del pokemones_rival[pokemon_derrotado]

        MostrarMensaje(f'{pokemon_derrotado} fue derrotado, ahora es tuyo')
        ActualizarPantalladeCombate()

        vivos_rival = PokemonesVivos(pokemones_rival)
        if vivos_rival == []:
            VENTANA.after(2000, lambda:FinJuego('jugador'))
            return
        else:
            pokemon_activo_rival = vivos_rival[0]
            MostrarMensaje(f'Rival saca a {pokemon_activo_rival}')
            ActualizarPantalladeCombate()

    # Si jugador recive KO
    if jugador_actual and jugador_actual['vida'] <= 0:
        puntaje_rival += 1
        pokemon_derrotado = pokemon_activo_jugador

        # Transferir pokemon al jugador
        nuevas_estadisticas = DATOS_POKEMONES[pokemon_derrotado].copy()
        pokemones_rival[pokemon_derrotado] = nuevas_estadisticas
        del pokemones_jugador[pokemon_derrotado]

        MostrarMensaje(f'{pokemon_derrotado} fue derrotado, ahora es de tu rival JAJA')
        ActualizarPantalladeCombate()

        vivos_jugador = PokemonesVivos(pokemones_jugador)
        if vivos_jugador == []:
            VENTANA.after(2000, lambda:FinJuego('rival'))
            return
        else:
            MostrarCambioForzado()


def FinJuego(ganador):
    if ganador == 'jugador':
        MostrarMensaje(f'Ganaste, tienes un puntaje de {puntaje_jugador}')
        GuardarPuntaje(NOMBRE, puntaje_jugador, AVATAR)
    else:
        MostrarMensaje('Perdiste...')
    DetenerCancion()
    CambiarPantallaPuntajes(Pantalla_puntajes)


# Cambio de Pokemones
botones_cambio = []

def MostrarOpcionesCambio(forzado=False):
    global botones_cambio

    LimpiarBotonesCambio()

    vivos = []
    for pokemon in PokemonesVivos(pokemones_jugador):
        if pokemon != pokemon_activo_jugador:
            vivos.append(pokemon)

    if vivos == []:
        return # no hay q cambiar nada
    
    Lbl_info_batalla.place_forget()

    Lbl_info_cambio = Label(Frm_info_batalla, text='A cual cambis?',
          font=(FUENTE, 20), bg='#0d0d1a', fg='#aaaaff')
    Lbl_info_cambio.place(x=10, y=8)

    lista_enumerada = enumerate(vivos)
    for i, nombre in lista_enumerada:
        stats = pokemones_jugador[nombre]
        texto = f'{nombre}  HP:{stats["vida"]}/{stats["vida_max"]}'
        Btn_temp = Button(Frm_info_batalla,
            text=texto,
            width=180, height=28,
            bg='#3A368A', image=px,
            compound=CENTER, font=(FUENTE, 11),
            borderwidth=6, relief='raised',
            fg='#f1f1f1', activebackground='#1a1a6a',
            activeforeground='#f1f1f1',
            command=lambda n=nombre, f=forzado: ConfirmarCambio(n, f))
        Btn_temp.place(x=10 + (i * 210), y=40)
        botones_cambio.append(Btn_temp)
    
    # Boton cancelar (SOLO SI NO ES FORZADO)
    if forzado != True:
        Btn_cancelar = Button(
            Frm_info_batalla, text='Cancelar',
            width=100, height=28,
            bg='#5a1a1a', image=px,
            compound=CENTER, font=(FUENTE, 11),
            borderwidth=6, relief='raised',
            fg='#f1f1f1', activebackground='#3a0a0a',
            activeforeground='#f1f1f1',
            command=CancelarCambio
        )
        Btn_cancelar.place(x=10, y=100)
        botones_cambio.append(Btn_cancelar)

def MostrarCambioForzado():
    MostrarOpcionesCambio(forzado=True)

def ConfirmarCambio(nombre, forzado):
    global pokemon_activo_jugador
    global turno_bloqueado
    pokemon_activo_jugador = nombre

    LimpiarBotonesCambio()

    Lbl_info_batalla.place(x=10, y=10)
    MostrarMensaje(f'Cambiaste a {nombre}')
    ActualizarPantalladeCombate()

    
    # Si no fue forzado el rival ataca despues del cambio
    if forzado != True:
        turno_bloqueado = True
        VENTANA.after(2000, TurnoRival)

def CancelarCambio():
    LimpiarBotonesCambio()
    Lbl_info_batalla.place(x=10, y=10)

def LimpiarBotonesCambio():
    global botones_cambio

    for boton in botones_cambio:
        boton.destroy()
    botones_cambio = []

    # Limpiar el label de "A cual Cambias?"
    for widget in Frm_info_batalla.winfo_children(): #Lista de widgets hijos de un frame
        if isinstance(widget, Label) and widget != Lbl_info_batalla:
            widget.destroy()


# ACTUALIZAR PANTALLA

def ActualizarInfoFrame(frame, nombre_entrenador, nombre_pokemon, stats, es_jugador):
    # Actualiza el Frm_info con los datos actuales de el que combate

    # Limpiar widgets
    for widget in frame.winfo_children():
        widget.destroy()

    width_frame = 640
    height_frame = 186


    # Seccion superior
    alto_superior = int(height_frame * 0.8)
    Frm_superior = Frame(frame, bg='#1a2a4a', width=width_frame, height=alto_superior)
    Frm_superior.place(x=0, y=0)
    Frm_superior.pack_propagate(False) # Que no se adapte

    # Nombre entrenador
    Lbl_entrenador_nombre = Label(Frm_superior, text=nombre_entrenador,
          font=(FUENTE, 11), bg='#1a2a4a', fg='#aaaaee')
    Lbl_entrenador_nombre.place(x=10, y=8)

    # Nombre pokemon
    color_nombre_pokemon = ''
    if es_jugador == True:
        color_nombre_pokemon = '#6bff6b'
    else:
        color_nombre_pokemon = '#ff6b6b'

    Lbl_nombre_pokemon = Label(Frm_superior, text=nombre_pokemon,
          font=(FUENTE, 22), bg='#1a2a4a', fg=color_nombre_pokemon)
    Lbl_nombre_pokemon.place(x=10, y=32)

    # Hp text
    vida_actual = stats['vida']
    vida_max = stats['vida_max']
    Lbl_vida = Label(Frm_superior, text=f'HP: {vida_actual} / {vida_max}',
          font=(FUENTE, 12), bg='#1a2a4a', fg='#e8e8ff')
    Lbl_vida.place(x=10, y=68)

    # Barra vida
    barra_total = 400
    porcentaje = vida_actual / vida_max if vida_max > 0 else 0  # CAMBIO 4: evitar division por cero
    barra_llena = int(barra_total * porcentaje)

    Cnv_barra = Canvas(Frm_superior, width=barra_total + 4, height=18,
                       bg='#333355', highlightthickness=1, highlightbackground='#555577')
    Cnv_barra.place(x=10, y=95)
    
    if barra_llena > 0:
        Cnv_barra.create_rectangle(0,0, barra_llena, 18, fill=ColorBarra(porcentaje), outline='')

    # Ataque y defensa
    Lbl_atk_def = Label(Frm_superior, text=f'ATK {stats["ataque"]}   DEF {stats["defensa"]}',
          font=(FUENTE, 9), bg='#1a2a4a', fg='#7777aa')
    Lbl_atk_def.place(x=10, y=118)



    # Seccion Inferior (pokemones disponibles)
    alto_inferior = height_frame - alto_superior
    Frm_inferior = Frame(frame, bg='#111133', width=width_frame, height=alto_inferior)
    Frm_inferior.place(x=0, y=alto_superior)

    dict_pokemones = []
    if es_jugador == True:
        dict_pokemones = pokemones_jugador
    else:
        dict_pokemones = pokemones_rival
    
    # Bolitas
    Cnv_bolitas = Canvas(Frm_inferior, width=300, height=alto_inferior, 
                         bg='#111133', highlightthickness=0)
    Cnv_bolitas.place(x=10, y=2)

    i=0
    for nombre_pokemon in dict_pokemones:
        stat = dict_pokemones[nombre_pokemon]

        x = 14 + (i * 30)
        y = 18

        if stat['vida'] > 0:
            color = '#55c855'
            borde = '#aaffaa'
        else:
            color = '#444444'
            borde = '#333333'
        
        if es_jugador == True:
            pokemon_activo = pokemon_activo_jugador
        else:
            pokemon_activo = pokemon_activo_rival
        
        if nombre_pokemon == pokemon_activo:
            activo = True
        else:
            activo = False

        # grosor
        if activo == True:
            grosor = 3
        else:
            grosor = 1

        # dibujar en pantalla
        Cnv_bolitas.create_oval(x-12, y-12, x+12, y+12, fill=color,
        outline=borde,
        width=grosor)

        i += 1

def ActualizarPantalladeCombate():
    global AVATAR_RIVAL
    DibujarPokemon()
    # Info Jugador
    if pokemon_activo_jugador in pokemones_jugador:
        ActualizarInfoFrame(Frm_info_jugador, f'{NOMBRE}  score: {puntaje_jugador}',
            pokemon_activo_jugador,
            pokemones_jugador[pokemon_activo_jugador],
            es_jugador=True)
        
    if pokemon_activo_rival in pokemones_rival:
        ActualizarInfoFrame(Frm_info_rival, f'{AVATAR_RIVAL}  score: {puntaje_rival}',
            pokemon_activo_rival,
            pokemones_rival[pokemon_activo_rival],
            es_jugador=False)
    
def MostrarMensaje(texto):
    Lbl_info_batalla.config(text=texto, font=(FUENTE, 30), bg="#0d0d1a")



# -76 height
# Frame para poner botones atacar y cambiar pokemon
frm_atacar_y_cambiarpok = Frame(Pantalla_Combate_Pokemon, width=463, height=174, bg='#0d0d1a')
frm_atacar_y_cambiarpok.place(x=817,y=471)

def FUNC_Btn_atacar():
    ReproducirBeep()
    TurnoJugador()

Btn_atacar = Button(frm_atacar_y_cambiarpok, text='Atacar'
                   , width=410 + 5, height=87- 35, 
                   bg="#8A3636",image=px, 
                   compound=CENTER, font=(FUENTE, 20), 
                   borderwidth=10, relief="raised", 
                   activebackground='#192301', fg='#f1f1f1', 
                   activeforeground='#f1f1f1', command=FUNC_Btn_atacar)
Btn_atacar.place(x=10, y=10)

def FUNC_Btn_cambiar_pokemon():
    ReproducirBeep()
    MostrarOpcionesCambio(forzado=False)

Btn_cambiar_pokemon = Button(frm_atacar_y_cambiarpok, text='Cambiar Pokemon'
                   , width=410 + 5, height=87- 35, 
                   bg="#368A37",image=px, 
                   compound=CENTER, font=(FUENTE, 20), 
                   borderwidth=10, relief="raised", 
                   activebackground='#192301', fg='#f1f1f1', 
                   activeforeground='#f1f1f1', command=FUNC_Btn_cambiar_pokemon)
Btn_cambiar_pokemon.place(x=10, y=87)

#Frame info
Frm_info_batalla = Frame(Pantalla_Combate_Pokemon, bg="#0d0d1a", width=817, height=174)
Frm_info_batalla.place(x=0, y=471)

Lbl_info_batalla = Label(Frm_info_batalla,
    text='',
    font=(FUENTE, 14),
    bg='#0d0d1a', fg='#e8e8ff',
    wraplength=790 , justify=LEFT
)
Lbl_info_batalla.place(x=14, y=14)


#Frame info jugador
Frm_info_jugador = Frame(Pantalla_Combate_Pokemon, bg="#2B71B7", width=640, height=190 - 4)
Frm_info_jugador.place(x=640, y=285)

#Frame info rival
Frm_info_rival = Frame(Pantalla_Combate_Pokemon, bg="#2B71B7", width=640, height=190 - 4)
Frm_info_rival.place(x=0, y=0)


# Placeholder avatares / pokemones
AVATAR_RIVAL = ''
def VerificarAvatar():
    global AVATAR, AVATAR_RIVAL
    if AVATAR == 'LaCobra':
        AVATAR_RIVAL = 'Davo'
    if AVATAR == 'Messi':
        AVATAR_RIVAL = 'CR7'
    if AVATAR == 'BadBunny':
        AVATAR_RIVAL = 'Anuel'
    if AVATAR == 'Speed':
        AVATAR_RIVAL = 'Ibai'
    if AVATAR == 'Goku':
        AVATAR_RIVAL = 'Vegetta'
    
    Pantalla_Combate_Pokemon.AVT_jugador_dibujar = CargarImagen(f'COMB_{AVATAR}.png', 'Avatares')
    Pantalla_Combate_Pokemon.create_image(18, 200, anchor=NW, image=Pantalla_Combate_Pokemon.AVT_jugador_dibujar)

    Pantalla_Combate_Pokemon.AVT_rival_dibujar = CargarImagen(f'COMB_{AVATAR_RIVAL}.png', 'Avatares')
    Pantalla_Combate_Pokemon.create_image(1048, 10, anchor=NW, image=Pantalla_Combate_Pokemon.AVT_rival_dibujar)

def ReproducirCancionBatalla():
    global AVATAR
    if AVATAR == 'LaCobra':
        ReproducirCancionLaCobra()
    if AVATAR == 'Messi':
        ReproducirCancionMessi()
    if AVATAR == 'BadBunny':
        ReproducirCancionBadBunny()
    if AVATAR == 'Speed':
        ReproducirCancionSpeed()
    if AVATAR == 'Goku':
        ReproducirCancionGoku()

def DibujarPokemon():
    global pokemon_activo_jugador
    global pokemon_activo_rival
    
    Pantalla_Combate_Pokemon.POK_jugador_dijubar = CargarImagen(f'{pokemon_activo_jugador}_darkblue_bg.png', 'Pokemones')
    Pantalla_Combate_Pokemon.create_image(237, 225, anchor=NW, image=Pantalla_Combate_Pokemon.POK_jugador_dijubar)

    Pantalla_Combate_Pokemon.POK_rival_dijubar = CargarImagen(f'{pokemon_activo_rival}_darkblue_bg.png', 'Pokemones')
    Pantalla_Combate_Pokemon.create_image(757, 35, anchor=NW, image=Pantalla_Combate_Pokemon.POK_rival_dijubar)
    


'''
GUARDAR PUNTAJEEEEES   !!!
'''

ARCHIVO_PUNTAJES = 'puntajes.json'

def CargarPuntajes():
    if os.path.exists(ARCHIVO_PUNTAJES):
        with open(ARCHIVO_PUNTAJES, 'r') as f:
            return json.load(f)
    return []

def ObtenerPuntaje(x):
    return x['puntaje']

def GuardarPuntaje(nombre, puntaje, avatar):
    lista = CargarPuntajes()
    lista.append({'nombre': nombre, 'puntaje' : puntaje, 'avatar': avatar})
    # Ordenar descendente y guarda solo top 10
    lista.sort(key=ObtenerPuntaje, reverse=True)
    lista = lista [:10]
    with open(ARCHIVO_PUNTAJES, 'w') as f:
        json.dump(lista, f)


Pantalla_puntajes = Canvas(VENTANA, bg=BGCOLOR, width=WIDTH, height=HEIGHT, highlightthickness=0)

Lbl_titulo_puntajes = Label(Pantalla_puntajes, text='MEJORES PUNTAJES',
    font=(FUENTE, 30), bg=BGCOLOR, fg='#FFD700')
Lbl_titulo_puntajes.place(x=WIDTH//2, y=40, anchor=CENTER)

Frm_tabla_puntajes = Frame(Pantalla_puntajes, bg='#16213e', width=700, height=400)
Frm_tabla_puntajes.place(x=WIDTH//2 - 350, y=100)



def ActualizarPantallaPuntajes():
    # Limpiar tabla
    for widget in Frm_tabla_puntajes.winfo_children():
        widget.destroy()

    lista = CargarPuntajes()

    Label(Frm_tabla_puntajes, text='#',
      font=(FUENTE, 14), bg='#16213e', fg='#aaaaee', width=4).place(x=20, y=10)
    Label(Frm_tabla_puntajes, text='Nombre',
      font=(FUENTE, 14), bg='#16213e', fg='#aaaaee', width=18).place(x=70, y=10)
    Label(Frm_tabla_puntajes, text='Avatar',
      font=(FUENTE, 14), bg='#16213e', fg='#aaaaee', width=14).place(x=290, y=10)
    Label(Frm_tabla_puntajes, text='Puntaje',
      font=(FUENTE, 14), bg='#16213e', fg='#aaaaee', width=10).place(x=500, y=10)
    
    Frame(Frm_tabla_puntajes, bg='#3a3a6a', width=620, height=2).place(x=20, y=45)

    # Si no hay datos
    if not lista:
        Label(Frm_tabla_puntajes,
          text='Aún no hay puntajes guardados.',
          font=(FUENTE, 13),
          bg='#16213e',
          fg='#555577').place(x=190, y=90)
    else:
        colores_podio = ['#FFD700', '#C0C0C0', '#CD7F32']

        for i, entrada in enumerate(lista):

            y = 60 + (i * 35)

            if i < 3:
                color_texto = colores_podio[i]
            else:
                color_texto = '#e8e8ff'
            
            if i % 2 == 0:
                bg_fila = '#1a1a3e'
            else:
                bg_fila = '#16213e'

            Label(Frm_tabla_puntajes, text=f'{i+1}',
              font=(FUENTE, 13),
              bg=bg_fila,
              fg=color_texto,
              width=4).place(x=20, y=y)

            Label(Frm_tabla_puntajes, text=entrada['nombre'],
              font=(FUENTE, 13),
              bg=bg_fila,
              fg=color_texto,
              width=18).place(x=70, y=y)

            Label(Frm_tabla_puntajes, text=entrada.get('avatar', '?'),
              font=(FUENTE, 13),
              bg=bg_fila,
              fg=color_texto,
              width=14).place(x=290, y=y)

            Label(Frm_tabla_puntajes, text=str(entrada['puntaje']),
              font=(FUENTE, 13),
              bg=bg_fila,
              fg=color_texto,
              width=10).place(x=500, y=y)

def FUNC_Btn_volver_desde_puntajes():
    ReproducirBeep()
    CambiarPantalla(Pantalla_principal)

Btn_volver_puntajes = Button(Pantalla_puntajes, text='VOLVER AL INICIO',
    width=400, height=47,
    bg="#8A3664", image=px,
    compound=CENTER, font=(FUENTE, 20),
    borderwidth=10, relief="raised",
    activebackground='#192301', fg='#f1f1f1',
    activeforeground='#f1f1f1', command=FUNC_Btn_volver_desde_puntajes)
Btn_volver_puntajes.place(x=WIDTH//2 - 200, y=530)

def CambiarPantallaPuntajes(pantalla):
    CambiarPantalla(pantalla)
    ActualizarPantallaPuntajes()
    
    
VENTANA.mainloop()
