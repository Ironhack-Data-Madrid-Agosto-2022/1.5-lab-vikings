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
    
    pass

# Saxon

class Saxon(Soldier):
 
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
    
    pass

# War

class War():
    
    """
    - `addViking()`
    - `addSaxon()`
    - `vikingAttack()`
    - `saxonAttack()`
    - `showStatus()`
    """
    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
        
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        #saxon.receivedmg(viking.attack)
        voluntier_vik = random.choice(self.vikingArmy)
        voluntier_sax = random.choice(self.saxonArmy)
        
        string = voluntier_sax.receiveDamage(voluntier_vik.attack())
        
        if voluntier_sax.health <= 0:
            self.saxonArmy.pop(self.saxonArmy.index(voluntier_sax))
        
        return string
            
    def saxonAttack(self):
        voluntier_vik = random.choice(self.vikingArmy)
        voluntier_sax = random.choice(self.saxonArmy)
        
        string = voluntier_vik.receiveDamage(voluntier_sax.attack())
        
        if voluntier_vik.health <= 0:
            self.vikingArmy.pop(self.vikingArmy.index(voluntier_vik))      
        
        return string
        
    def showStatus(self):
        
        """
        - **if the `Saxon` array is empty**, should return _**"Vikings have won the war of the century!"**_
        - **if the `Viking` array is empty**, should return _**"Saxons have fought for their lives and survive another day..."**_
        - **if there are at least 1 `Viking` and 1 `Saxon`**, should return _**"Vikings and Saxons are still in the thick of battle."**_
        """
        
        if len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."
        else:
            if len(self.saxonArmy) == 0:
                return "Vikings have won the war of the century!"
            else:   #len(self.vikingArmy) == 0:
                return "Saxons have fought for their lives and survive another day..."
    
    pass
