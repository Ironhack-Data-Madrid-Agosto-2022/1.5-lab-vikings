# Import libraries

import random


# Soldier


class Soldier:
    
    def __init__(self, health, strength):
    
        self.health = health
        self.strength = strength

    def attack(self):
       
        return self.strength
    
    def receiveDamage(self, damage):
        
        self.health = self.health - damage
        
# Viking


class Viking:
    
    def __init__(self, name, health, strength):
        
        self.name = name
        self.health = health
        self.strength = strength
     
        
    def attack(self):
        
        return self.strength
    
    def receiveDamage(self, damage):
        
        self.health = self.health - damage
        if self.health >0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'
            
    def battleCry(self):
        
        return "Odin Owns You All!"
        
    

# Saxon


class Saxon:
    
    def __init__(self, health, strength):
        
        self.health = health
        self.strength = strength
     
        
    def attack(self):
        
        return self.strength
    
    def receiveDamage(self, damage):
        
        self.health = self.health - damage
        if self.health >0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return f'A Saxon has died in combat'
            

        
    

# War


class War:
    
    def __init__(self):
        
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self, viking):
        self.vikingArmy.append(viking)
        
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
        
    def vikingAttack(self):
        vik = random.choice(self.vikingArmy)
        sax = random.choice(self.saxonArmy)
        
        attack_vik = sax.receiveDamage(vik.attack())
        
        if sax.health <= 0:
            self.saxonArmy.remove(sax)
        
        return attack_vik
    
    def saxonAttack(self):
        vik = random.choice(self.vikingArmy)
        sax = random.choice(self.saxonArmy)
        
        attack_sax = vik.receiveDamage(sax.attack())
        
        if vik.health <= 0:
            self.vikingArmy.remove(vik)
        
        return attack_sax
    
    def showStatus(self):
        if len(self.saxonArmy) == 0 and len(self.vikingArmy) > 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0 and len(self.saxonArmy) > 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        

