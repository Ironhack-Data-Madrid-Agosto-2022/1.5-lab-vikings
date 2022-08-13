

class Soldier:

    def __init__(self, health, strength):
        
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
        
class Viking(Soldier):
    
    def __init__(self, name, health, strength):
        
        self.name = name
        self.health = health
        self.strength = strength
        
        
    def attack(self):
        return self.strength

    
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health >=0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'
        
    def battleCry(self):
        return 'Odin Owns You All!'


class Saxon(Soldier):
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength
        
        
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health >=0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return f'A Saxon has died in combat'
        

class War:
    
    def __init__(self):
        
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, viking):
        self.vikingArmy.append(viking)
           
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
        
    def vikingAttack(self):
        import random   

        oneSaxon = random.choice(self.saxonArmy)
        oneViking = random.choice(self.vikingArmy)
        
        SaxonReceiveDamage = oneSaxon.receiveDamage(oneViking.attack())
        
        if oneSaxon.health <= 0:
            self.saxonArmy.remove(oneSaxon)
            
        return SaxonReceiveDamage

    def saxonAttack(self):
        import random
        oneSaxon = random.choice(self.saxonArmy)
        oneViking = random.choice(self.vikingArmy)
        
        VikingReceiveDamage = oneViking.receiveDamage(oneSaxon.attack())
        
        if oneViking.health <= 0:
            self.vikingArmy.remove(oneViking)
            
        return VikingReceiveDamage
    
    def showStatus(self):
        if len(self.saxonArmy) <= 0 and len(self.saxonArmy) < len(self.vikingArmy):
            return f'Vikings have won the war of the century!'
        elif len(self.vikingArmy) <= 0 and len(self.vikingArmy) < len(self.saxonArmy):
            return f'Saxons have fought for their lives and survive another day...'
        elif len(self.vikingArmy) >= 1 and len(self.saxonArmy) >= 1:
            return f'Vikings and Saxons are still in the thick of battle.'

    
    
