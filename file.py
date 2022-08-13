import vikingsClasses as vc
import time
import os
import random

class FailMenu(Exception):
    def __init__(self, message):
        super().__init__(message)
        
class TooManyViks(Exception):
    def __init__(self, message):
        super().__init__(message)
        
def dado():
    return random.randint(0,1)

def comenzarGuerra (partida):
    os.system("clear")

    turno = 0
    while len(partida.saxonArmy) >= 1 and len(partida.vikingArmy) >= 1:
        time.sleep(1)
        print("Turno ", turno, " --------------------------------------")
        if dado() == 1:
            print(partida.vikingAttack())
        else:
            print(partida.saxonAttack())
            
        print(partida.showStatus())
        print("--------------------------------------------------")

        turno += 1

        
def mostrarMenu():
    print()
    print("------------------------------")
    print("Welcome to Vikings Slayer 3000")
    print("------------------------------")
    print("1. Jugar")
    print("2. Readme")
    print("3. Salir")
    print("------------------------------")

    
def crearViking():
    listaNombres = ["CouchMaster", "Maestrodelsofa", "Expertoensofasymandos", "Gaminggolden", "Markattack", "Mamigamer", "Gamerbois", "Undergroundgamer", "Gamergoesout", "Bloodygamer", "EatPlayRepeat", "ELBICHO", "Damnbitch", "JuanCarlos", "Abelardo", "Chanquete", "Eustaquio", "PerroSucio", "KikeElMatador", "KikeArbitroDeMagic", "GitanoBueno"]
    vik = vc.Viking(random.choice(listaNombres), random.randrange(150,300), random.randrange(50,100))
    return vik

def crearSaxon():
    sax = vc.Saxon(random.randrange(150,300), random.randrange(45,80))
    return sax
    
def mainJuego():
    
    partidaEnMarcha = True
    
    while(partidaEnMarcha):
            #Inicializar partida--------------------------------------------------
            os.system("clear")
            partida = vc.War()  
            numViks = 0
            numSaxs = 0
            
            numViks = int(input("Introduce una cantidad de Vikings: "))
            numSaxs = int(input("Introduce una cantidad de Saxons: "))
            
            while(numViks > 20):
                print("Menos de 20 vikingos que nos tiramos hasta mañana si no...")
                numViks = int(input("Introduce una cantidad de Vikings: "))
                
            #Empieza la partida---------------------------------------------------
            for i in range (numViks):
                partida.addViking(crearViking())
            for j in range (numSaxs):
                partida.addSaxon(crearSaxon())
            partidaEnMarcha = comenzarGuerra(partida)


# "main" del programa ----------------------------------------------------------------            

msgFail = ":) Ese no es el camino compañero"

gaming = True
opc = 0

file_txt = "Rick.txt"


while gaming:
    try:
        mostrarMenu()
        opc = int(input("Introduce una opción: "))
        if opc == 1:
            mainJuego()
        elif opc == 2:
            print((open(file_txt,'r')).read())
        elif opc == 3:
            gaming = False
        else:
            raise ValueError(msgFail)
            
    except ValueError:
        print()
        print(FailMenu(msgFail))


