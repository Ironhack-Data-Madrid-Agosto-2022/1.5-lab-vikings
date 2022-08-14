import vikingsClasses as clases
import time
import random


def dado():
    return random.randint(0,1)

def armyStatus(army):
    fighters = []
    for soldier in army:
        if soldier.health >= 50: fighters.append('❤️')
        else: fighters.append('🤕')
    return fighters

def combat (self):
    turno = 1
    while len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:
        time.sleep(1)
        print("\n\t-------------------  COMBAT ", turno, " -------------------\n")
        if dado() == 1: print(self.vikingAttack())
        else: print(self.saxonAttack())
        print("🔵:", armyStatus(self.vikingArmy))
        print("🔴:", armyStatus(self.saxonArmy))
        print(self.showStatus())
        
        turno += 1
     

def createViking():
    namesList = ["Kike", "mabarrera", "Javi", "Antonio", "Espe", "Jaime", "Jose", "Lucia", "Berta", "Miguel", "Carlos", "Pablo", "Mar", "Vito", "Ironhack"]
    name = random.choice(namesList) 
    namesList.remove(name) #LO BORRAMOS PARA QUE NO SE REPITAN NOMBRES
    return clases.Viking(name, random.randint(100,300), random.randint(100,300))

def createSaxon():
    return clases.Saxon(random.randint(1,200), random.randrange(1,200))

def Game():

    partidaEnMarcha = True

    while(partidaEnMarcha):
        fight = clases.War()  

        #PEDIMOS AL USUARIO EL NUMERO DE LUCHADORES DE CADA TIPO
        vikingsFighting = 0

        vikingsFighting = int(input("\tVikingos fighting: "))
        while (vikingsFighting > 15): 
            print("\t\tSOLO HAY 15 VIKINGOS DISPONIBLES")
            vikingsFighting = int(input("\tVikingos fighting: "))

        saxonsFighting = 0   
        saxonsFighting = int(input("\tSaxons fighting: "))
        print("\n")

        #CREAMOS LAS LISTAS CON TODOS LOS LUCHADORES
        for num in range (vikingsFighting): 
            viking = createViking()
            print("🔵", num+1, ": NAME = ", viking.name, "\t\tHEALTH = ", viking.health, "\tSTRENGTH = ", viking.strength)
            fight.addViking(viking)
            
        for num in range (saxonsFighting): 
            saxon = createSaxon()
            print("🔴", num+1, ":\t\t\t\t HEALTH = ", saxon.health, "\tSTRENGTH = ", saxon.strength)
            fight.addSaxon(saxon)
        
        print("\n")

        partidaEnMarcha = combat(fight)

        return None
             

print("\n\n\n---------------------------------------------------------------------------------\n\n\n")
print("\t\t\t----- VIKINGS VS SAXONS -----")
print("\n\n\n---------------------------------------------------------------------------------\n")

Game()
print("\n\n")



 

