from tkinter import *
from tkinter import messagebox
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
    if len(PokemonsSeleccionados) == 3:
        # Confirmar Pokemones
        for pokemon in PokemonsSeleccionados:
            POKEMONES.append(pokemon)

        CambiarPantalla(Pantalla_Combate_Pokemon)
        ReproducirBeep()
        print(POKEMONES, AVATAR, NOMBRE)
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
Pantalla_Combate_Pokemon = Canvas(VENTANA, bg=BGCOLOR, width=WIDTH, height=HEIGHT, highlightthickness=0)

VENTANA.mainloop()