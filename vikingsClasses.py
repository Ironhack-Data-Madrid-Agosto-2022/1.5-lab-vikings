
# Soldier


class Soldier:
    
    def __init__(self, health, strength):
        
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        if self.health <= damage:
            self.health = 0
        else:
            self.health -= damage

# Viking


class Viking(Soldier):
    
    def __init__(self, name, health, strength):
        
        self.name = name
        self.health = health
        self.strength = strength
    
    def receiveDamage(self, damage):
        
        self.health -= damage
            
        if self.health > 0:
            return self.name + " has received " + str(damage) + " points of damage"
        else:
            return self.name + " has died in act of combat"
        
    def battleCry(self):
        return "Odin Owns You All!" 

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        
        self.health = health
        self.strength = strength
        
    def receiveDamage(self, damage):
        #if self.health <= damage:
            #self.health = 0
        #else:
        self.health -= damage

        if self.health > 0:
            return "A Saxon has received " + str(damage) + " points of damage"
        else:
            return "A Saxon has died in combat"
        

# War

import random
class War(Viking,Saxon):
    
    def __init__(self):
        
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self, Viking):
        
        self.vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon):
        
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        
        if len(self.vikingArmy) >= 1 and len(self.saxonArmy) >= 1:
            soldier = random.choice(self.saxonArmy)
            b = soldier.receiveDamage(random.choice(self.vikingArmy).health)
            if soldier.health <= 0:
                self.saxonArmy.remove(soldier)
            
    def saxonAttack(self):
        
        if len(self.vikingArmy) >= 1 and len(self.saxonArmy) >= 1:
            soldier = random.choice(self.vikingArmy)
            b = soldier.receiveDamage(random.choice(self.saxonArmy).health)
            if soldier.health <= 0:
                self.vikingArmy.remove(soldier)
        
    def showStatus(self):
        
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle." 
        
        
        
        
    
     
    
