
# Soldier


class Soldier():
    
    def __init__(self, health, strength):
     
        self.health = health
        self.strength = strength
     
    def attack(self):
        
        return self.strength
    
    def receiveDamage(self, damage):
        
        self.damage = damage
        self.health = self.health - damage
    
# Viking


class Viking(Soldier):
    
    def __init__(self, name, health, strength):
        
        self.name = name
        self.health = health
        self.strength = strength
        
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - damage
        
        if self.health > 0:
            return f'{self.name} has received {self.damage} points of damage'
       
        else:
            return f'{self.name} has died in act of combat'
    
    def battleCry(self):
        return f"Odin Owns You All!"
    

# Saxon


class Saxon(Soldier):
    
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - damage
    
        if self.health > 0:
            return f'A Saxon has received {self.damage} points of damage'
       
        else:
            return f'A Saxon has died in combat'
    

# War


class War():
    
    def __init__ (self):
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self, viking):
        self.vikingArmy.append(viking)
        
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
       
    def vikingAttack(self):
        import random
        Sax_X = random.choice(self.saxonArmy)
        Vik_X = random.choice(self.vikingArmy)
        
        Hostia = Sax_X.receiveDamage(Vik_X.attack())
        
        if Sax_X.health <= 0:
            self.saxonArmy.remove(Sax_X)
        
        return Hostia
    
    def saxonAttack(self):
        import random
        Sax_X = random.choice(self.saxonArmy)
        Vik_X = random.choice(self.vikingArmy)
        
        Hostia = Vik_X.receiveDamage(Sax_X.attack())
        
        if Vik_X.health <= 0:
            self.vikingArmy.remove(Vik_X)
        
        return Hostia
        
    def showStatus(self):
        if len(self.saxonArmy) <= 0 and len(self.saxonArmy) < len(self.vikingArmy):
            return f'Vikings have won the war of the century!'
        
        elif len(self.vikingArmy) <= 0 and len(self.vikingArmy) < len(self.saxonArmy):
            return f'Saxons have fought for their lives and survive another day...'
        
        elif len(self.vikingArmy) and len(self.saxonArmy) >= 1:
            return f'Vikings and Saxons are still in the thick of battle.'

 
        