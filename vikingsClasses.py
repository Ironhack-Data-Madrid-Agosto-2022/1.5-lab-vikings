
# Soldier

from email.base64mime import header_length
from readline import set_history_length
from sys import set_coroutine_origin_tracking_depth


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage
        return


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.health = health
        self.strength = strength
        self.name = name

    def receiveDamage(self, damage):
        self.health = self.health - damage

        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else: 
            return f'{self.name} has died in act of combat'
    def battleCry(self):
        return 'Odin Owns You All!'




# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        self.strength = strength
        self.health = health
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else: 
            return 'A Saxon has died in combat'
  
    
# War

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self, viking):
        self.vikingArmy.append(viking)
        return 
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
        return
    def vikingAttack(self):
        viking_atacante = self.vikingArmy[0]
        saxon_atacante = self.saxonArmy[0]
        fuerza_vikingo = viking_atacante.strength
        resultado_lucha = saxon_atacante.receiveDamage(fuerza_vikingo)

        if saxon_atacante.health <= 0:
            self.saxonArmy.remove(saxon_atacante)
        return resultado_lucha

    def saxonAttack(self):
        viking_atacante = self.vikingArmy[0]
        saxon_atacante = self.saxonArmy[0]
        fuerza_saxon = saxon_atacante.strength        
        resultado_lucha_2 = viking_atacante.receiveDamage(fuerza_saxon)

        if viking_atacante.health <= 0:
            self.vikingArmy.remove(viking_atacante)
        return resultado_lucha_2


    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1: 
            return "Vikings and Saxons are still in the thick of battle."




