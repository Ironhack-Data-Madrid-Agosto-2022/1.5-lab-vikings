
# Soldier
# metodo constructor es la propia clase, dentro van los argumentos. Luego debajo añadimos sus atributos. Y por ultimo creamos funciones que se llaman métodos ( para poder crear nuestras interactuaciones)

#probando probando

#Los atributos solo pueden estar si existen en la clase padre,  o si se crean añaden en el constructor como argumentos en la Subclase. Si no da error ya que no los encuentra, en caso de que se haga en este ejercicio no funciona porque es un test, pero en cualquier otro caso deberia funcionar.
import random

class Soldier:
    
    def __init__(self, health , strength):
        
        #atributos solo como argumentos, deben ser identicos
        self.health = health
        self.strength = strength
        
           #métodos
                    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health= self.health - damage
        
        
# Viking

class Viking(Soldier):
    
    def __init__(self, name, health , strength):
        
        self.health = health
        self.strength = strength
        self.name = name
        
        
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        
        self.health= self.health - damage
        
        if self.health >0:
            return f'{self.name} has received {damage} points of damage'
            
        else:
            return f'{self.name} has died in act of combat'
      
    
    def battleCry(self):
        return 'Odin Owns You All!'
    

# Saxon


class Saxon(Soldier):
    
    def __init__(self, health , strength):
        
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        
        self.health= self.health - damage
        
        if self.health >0:
            
            return f'A Saxon has received {damage} points of damage'
            
        else:
            return f'A Saxon has died in combat'


# War

class War():
    
    def __init__(self):
        
        self.vikingArmy = []
        self.saxonArmy = []
    
    
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)    
    
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
        
    
    def vikingAttack(self):
        
        pepe= random.choice(self.saxonArmy)
        elbicho= random.choice(self.vikingArmy)
        pepe2= pepe.receiveDamage(elbicho.strength)  
        
        if pepe.health <=0:
            self.saxonArmy.remove(pepe)
            
        return pepe2

    
    def saxonAttack(self):
        
        pepe= random.choice(self.saxonArmy)
        elbicho= random.choice(self.vikingArmy)
        elbicho2= elbicho.receiveDamage(pepe.strength)  
        
        if elbicho.health <=0:
            self.vikingArmy.remove(elbicho)
            
        return elbicho2   

    
    
    def showStatus(self):
        
        if len(self.saxonArmy)== 0:
            return f'Vikings have won the war of the century!'
            
        elif len(self.vikingArmy)== 0:
            return f'Saxons have fought for their lives and survive another day...'
        
        else:
            return f'Vikings and Saxons are still in the thick of battle.'
        
        














