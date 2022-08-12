
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def salud(self):
        return self.health
        
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage
        

# Viking


class Viking(Soldier):
    
    def __init__(self, name ="", health = '', strength = ''):
        self.name = name
        self.health = health
        self.strength = strength
    
    #def salud(self):
     #   return self.health
    
    def attack(self):
        return self.strength
        
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage

        if self.health <= 0:
            return f'{self.name} has died in act of combat'
        else:
            return f'{self.name} has received {self.damage} points of damage'
        
    def battleCry(self):
        return f'Odin Owns You All!'
        
    
# Saxon


class Saxon(Soldier):
    
    def __init__(self, health ='', strength = ''):
        self.health = health
        self.strength = strength
    
    def salud(self):
        return self.health
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage
        if self.health <= 0:
            return'A Saxon has died in combat'  
        else:
            return f'A Saxon has received {self.damage} points of damage'
# War


class War:
        
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
        
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
        

    def vikingAttack(self):
        b = self.saxonArmy[0].receiveDamage(self.vikingArmy[0].strength)
        if self.saxonArmy[0].health <= 0:
            self.saxonArmy.pop(0)
        
        return b
    
    def saxonAttack(self):
        a = self.vikingArmy[0].receiveDamage(self.saxonArmy[0].strength)
        if self.vikingArmy[0].health <= 0:
            self.vikingArmy.pop(0)
        
        return a
    
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return 'Vikings have won the war of the century!'
        elif len(self.vikingArmy) == 0:
            return 'Saxons have fought for their lives and survive another day...'
        else:
            return 'Vikings and Saxons are still in the thick of battle.'
