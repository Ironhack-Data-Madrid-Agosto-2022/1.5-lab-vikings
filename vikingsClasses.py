
# Soldier


class Soldier:
    import random
    def __init__(self, health, strength):
        self.health= health
        self.strength= strength
        
    def attack (self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage

        
        #OK
        
# Viking



class Viking (Soldier):
    import random
    def __init__(self, name, health, strenght):
        Soldier.__init__ (self, health, strenght)
        
        self.name= name
        self.health= health
        self.strenght=strenght
    

    def receiveDamage(self, damage):
        self.health= self.health - damage
        if self.health> 0:
            return self.name +   " has received " + str(damage) + " points of damage"
        else:
            return self.name + " has died in act of combat"
                  
                  
    def battleCry(self):
            return "Odin Owns You All!"


#OK



# Saxon


class Saxon(Soldier):
    import random
    def __init__(self, health, strenght):
        Soldier.__init__ (self, health, strenght)
         
        self.health= health
        self.strenght= strenght
        
        
    def receiveDamage(self, damage):
        self.health= self.health - damage
        if self.health> 0:
            return "A Saxon has received " + str(damage) + " points of damage"
        else:
            return "A Saxon has died in combat"
        
        
#OK
        
    

# War


class War: #(Viking,Saxon): 
    #Viking.__init__ (self, health, strenght)
    #Saxon.__init__ (self, health, strenght)
    #def __init__ (self):
    import random
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
            
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)
        
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    
    def vikingAttack(self):
        import random
 
        #random.choice(self.vikingArmy).receiveDamage(Saxon.strength)
        #self.health= self.health - damage
        
        b=random.choice(self.vikingArmy) 
        a=random.choice(self.saxonArmy)
        c=a.receiveDamage(b.strength)
        
        if a.health<= 0:
            self.saxonArmy.remove(a)
            return c #Viking.receiveDamage(Saxon.strength)
        else:
             pass
            
    def saxonAttack(self):
        import random
        #random.choice(self.vikingArmy).receiveDamage(Saxon.strength)
        #self.health= self.health - damage
        a=random.choice(self.vikingArmy) 
        b=random.choice(self.saxonArmy)
        c=a.receiveDamage(b.strenght)
            return c
        
        if a.health<= 0:
            self.vikingArmy.remove(a)
            #return c
                                   
        
            
            
    def showStatus(self):
        import random
        if len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        #elif len(saxonArmy)>=0 and len(vikingArmy)>=0:
            #return "Vikings and Saxons are still in the thick of battle."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        