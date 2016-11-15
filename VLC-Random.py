import random
## Autores: Alberto Garcia y Marc Hernandez
# Programa que genera una lista aleatoria de canciones a partir de una diccionario ya creado
# y reproduce la lista aleatoria lanzando el programa VLC


## UTILIDADES DE DEPURACION ## 


'''def checkSeleccionaCancionRandom(cancion, libreria):


def checkPlaySuffle(playListInicial):
'''



## RUTINAS DE UTILIDADES ## 


def seleccionaCancionRandom(libreria):
    assert isinstance (libreria,dict) #precondicion
    numeroCanciones=len(libreria) #necesario para el assert (postcondicion)
    cancionRandom = random.choice(list(libreria.keys()))


    assert cancionRandom in (libreria.keys()) #postcondicion
    assert len(libreria) == numeroCanciones #postcondicion
    return cancionRandom


def imprimirCancionesReproducidas(playListInicial):
    assert isinstance (playListInicial,list) #precondicion

    for cancion in playListInicial:
        print(cancion)


def lanzarVLC(libreria, playListInicial):
    assert isinstance (libreria,dict) #precondicion
    assert isinstance (playListInicial,list) #precondicion

    import subprocess
    import shlex
    import os

    linuxPathVLC = "/usr/bin/vlc"
    separador = " "

    for cancion in playListInicial:
        try:
            rutaAccesoFichero = libreria[cancion]["location"]
        except KeyError:
            print("la cancion " + str(cancion) + " no se encuentra en la biblioteca")
        else:
            if os.path.exists(str(rutaAccesoFichero)):
                linuxPathVLC = linuxPathVLC + separador + str(rutaAccesoFichero)
            else:
                pass

    # Popen necesita una lista de string
    args = shlex.split(linuxPathVLC)

    try:
        procesoVLC = subprocess.Popen(args)
        #procesoVLC = subprocess.Popen(["/usr/bin/vlc", "biblioteca/California_Uber_Alles.mp3", "Seattle_Party.flac"])
    except OSError:
        print("el fichero no existe")
    except ValueError:
        print("argumentos invalidos")
    else:
        print("lanzando VLC con lista aleatoria")


## FUNCION PRINCIPAL ## 

def generarplayListInicial(liberia,playListInicial):
    assert isinstance (libreria,dict) #precondicion
    assert isinstance (playListInicial,list) #precondicion

    while len(playListInicial) < len(libreria):
        nombre=seleccionaCancionRandom(libreria)
        if nombre not in playListInicial:
            playListInicial.append(nombre)
    assert isinstance (playListInicial, list)
    return playListInicial



def listaToDict(lista):
    assert isinstance (lista, list) #precondicion
    Dic = {}
    i=1
    for item in lista:
        Dic[i]=item
        i+=1
    assert isinstance (dic, dict) #postcondicion
    return Dic



## PROGRAMA PRINCIPAL ##
libreria = {"California_Uber_Alles": 
                {"track-number": 3, "artist": "Dead Kennedys", "album": "Dead Kennedys", "location": "./biblioteca/California_Uber_Alles.mp3"},
            "Seattle_Party": 
                {"track-number": 1, "artist": "Chastity Belt", "album": "No regrets", "location": "./biblioteca/Seattle_Party.flac"},
            "King_Kunta":
                {"track-number": 3, "artist": "Kendrick Lamar", "album": "To Pimp A Butterfly", "location": "./biblioteca/King_Kunta.mp3"}   
            }



playListInicial = []

# libreriaLista = []
# assert playSuffle(libreriaLista)

playListInicial = generarplayListInicial(libreria,playListInicial)

playList=listaToDict(playListInicial)

imprimirCancionesReproducidas(playListInicial)

lanzarVLC(libreria, playListInicial)
