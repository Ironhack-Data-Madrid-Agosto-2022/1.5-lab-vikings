import random
# Soldier

class Soldier:

    def __init__(self, health, strength):

        #Atributos
        self.health= health
        self.strength= strength

        #Métodos

    def attack(self):

        
        return self.strength

    def receiveDamage(self, damage): #receive the damage):

        self.health= self.health - damage

# Viking

class Viking:
    
    def  __init__(self, name, health, strength):

        #Atributos
        #Soldier.__init__(self)

        self.name=name
        self.health=health
        self.strength=strength

    #Métodos

    def attack(self):
        return self.strength

    def receiveDamage(self, damage): #receive the damage):
        
        self.health= self.health - damage

        if self.health>0:
            return f'{self.name} has received {damage} points of damage'

        if self.health<=0:
            return f'{self.name} has died in act of combat'

    def battleCry(self):
        return f'Odin Owns You All!'

# Saxon

class Saxon:

    def  __init__(self, health, strength):

        #Atributos
        #Soldier.__init__(self)

        self.health=health
        self.strength=strength

    #Métodos

    def attack(self):
        return self.strength

    def receiveDamage(self, damage): #receive the damage):
        
        self.health= self.health - damage

        if self.health>0:
            return f'A Saxon has received {damage} points of damage'

        if self.health<=0:
            return f'A Saxon has died in combat'

# War

class War:

    def __init__(self):

        #Atributos
        self.vikingArmy= []
        self.saxonArmy= []          

    #Metodos
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        largov=len(self.vikingArmy)
        largos=len(self.saxonArmy)

        vik_ele=random.randint(0, largov-1)
        sax_ele=random.randint(0, largos-1)
        golpe=self.vikingArmy[vik_ele].attack()
        
        estado_sax= self.saxonArmy[sax_ele].receiveDamage(golpe)
        if estado_sax==f'A Saxon has died in combat':
            self.saxonArmy.pop(sax_ele)
        
        return estado_sax

    def saxonAttack(self):
        largov=len(self.vikingArmy)
        largos=len(self.saxonArmy)

        vik_ele=random.randint(0, largov-1)
        vik_name=self.vikingArmy[vik_ele].name
        sax_ele=random.randint(0, largos-1)
        golpe1=self.saxonArmy[sax_ele].attack()
        

        estado_vik= self.vikingArmy[vik_ele].receiveDamage(golpe1)
        if estado_vik== f'{vik_name} has died in act of combat':
            self.vikingArmy.pop(vik_ele)
        
        return estado_vik

   
    def showStatus(self):

        if len(self.saxonArmy)==0:
            return f'Vikings have won the war of the century!'
        if len(self.vikingArmy)==0:
            return f'Saxons have fought for their lives and survive another day...'
        if len(self.saxonArmy)!=0 and len(self.vikingArmy)!=0:
            return f'Vikings and Saxons are still in the thick of battle.'



        
