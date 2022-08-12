class Soldier:
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack (self):
        return self.strength
    
    def receiveDamage(self, damage):
        if self.health  <= damage:
            self.health = 0
        else:
            self.health -= damage


class Viking(Soldier):
    def __init__ (self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
            
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return (f"{self.name} has received {damage} points of damage")
        else:
            return (f"{self.name} has died in act of combat")
            
    def battleCry(self):
        return "Odin Owns You All!"
    

class Saxon(Soldier):
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength
        
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return (f"A Saxon has received {damage} points of damage")
        else:
            return ("A Saxon has died in combat")
        
class War:
    
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
        
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
        
    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        vikingo = random.choice(self.vikingArmy)
        
        receiveDamage2 = saxon.receiveDamage(vikingo.strength)
        
        if saxon.health <= 0:
            self.saxonArmy.pop()
        
        return (f'{receiveDamage2}')
    
    def saxonAttack(self):
    
        saxon = random.choice(self.saxonArmy)
        vikingo = random.choice(self.vikingArmy)
        
        receiveDamage3 = vikingo.receiveDamage(saxon.strength)
        
        if vikingo.health <= 0:
            self.vikingArmy.pop()
        
        return (f'{receiveDamage3}')

       
        
    def showStatus(self):
        if self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        
        if self.vikingArmy != [] and self.saxonArmy != []:
            return "Vikings and Saxons are still in the thick of battle."
