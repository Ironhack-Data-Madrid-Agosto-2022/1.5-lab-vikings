import random

# Soldier

class Soldier():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
    

# Viking

class Viking(Soldier):
    """
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"
    """
    pass

# Saxon

class Saxon(Soldier):
    """
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
    """
    pass

# War

class War():
    
    """
    - `addViking()`
    - `addSaxon()`
    - `vikingAttack()`
    - `saxonAttack()`
    - `showStatus()`
    
    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
        
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        #saxon.receivedmg(viking.attack)
        numViking = random.choice()
        numSaxon = random.choice()
        
        self.saxonArmy[numSaxon].receiveDamage(self.vikingArmy[numViking].attack())
        
        if saxonArmy[numSaxon].health < 0:
            saxonArmy.pop(numSaxon)
            
    def saxonAttack(self):
        numViking = random.choice()
        numSaxon = random.choice()
        
        self.vikingArmy[numViking].receiveDamage(self.saxonArmy[numSaxon].attack())
        
        if vikingArmy[numViking].health < 0:
            vikingArmy.pop(numViking)        
        
    def showStatus(self):
        
    """    
    
    pass
