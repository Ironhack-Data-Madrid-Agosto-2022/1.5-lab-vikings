# Soldier
from random import choice

class Soldier:
    def __init__(self, health, strength):
        # add code here
        
        #atributos
        self.health = health
        self.strength = strength
    
    #Metodos

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage
        
        return None
        

# Viking


class Viking(Soldier):
    
    def __init__(self, name, health, strength): 
        
        #Nuevos atributos
        self.name = name
        #self.health = health
        #self.strength = strength
        super().__init__(health, strength)

        
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0: 
            return self.name + ' has received ' + str(damage) + ' points of damage'
        else: 
            return self.name + ' has died in act of combat'
    
    def battleCry(self):
        return "Odin Owns You All!"
        
        

# Saxon


class Saxon(Soldier):
    
    def __init__(self, health, strength): 
        
        #Nuevos atributos
        #self.health = health
        #self.strength = strength
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0: 
            return 'A Saxon has received ' + str(damage) + ' points of damage'
        if self.health <= 0: 
            return 'A Saxon has died in combat'
    
    def battleCry(self):
        return "Odin Owns You All!"

# War


class War:
    
    def __init__(self):
        
        self.vikingArmy = [] #should assign an empty array to the vikingArmy property
        self.saxonArmy = [] #should assign an empty array to the saxonArmy property
    
    #Metodos

    def addViking(self, vik):
        if isinstance(vik, Viking):
            self.vikingArmy.append(vik)
        
        return None
    
    def addSaxon(self, sax):
        if isinstance(sax, Saxon):
            self.saxonArmy.append(sax)
        
        return None
    
    def vikingAttack(self):
        viking = choice(self.vikingArmy)
        saxon = choice(self.saxonArmy)
        damage = saxon.receiveDamage(viking.attack())

        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)

        return damage
    
    def saxonAttack(self):
        viking = choice(self.vikingArmy)
        saxon = choice(self.saxonArmy)
        damage = viking.receiveDamage(saxon.attack())

        if viking.health <= 0:
            self.vikingArmy.remove(viking)

        return damage
    
    def showStatus(self):
        if len(self.saxonArmy) == 0: return 'Vikings have won the war of the century!'
        if len(self.vikingArmy) == 0: return 'Saxons have fought for their lives and survive another day...'
        return 'Vikings and Saxons are still in the thick of battle.'
        

