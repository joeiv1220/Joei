class Item(object):
    def __init__ (self, name, descript):
        self.name = name
        self.descript = descript
        
#__________________#__________________#__________________#__________________#__________________#__________________#__________________#__________________#______________________   

#weapon
class Weapons(Item):
   def __init__(self, name, descript, damage):
        super(Weapons, self).__init__(name, descript)
        self.damage = damage
          
#body        
class Body(Weapons):
   def __init__(self, name, descript, damage):
        super(Body, self).__init__(name, descript, damage)
        self.damage = damage
        
class Elbow(Body):
   def __init__(self, name, descript, damage):
        super(Elbow,self).__init__(name, descript, damage)
        self.damage = damage    
#__________________#__________________#__________________#__________________#__________________#__________________#__________________#__________________#__________________#_____________________
#defense        
class Defense(Weapons):
   def __init__(self, name, descript, damage):
        super(Defense,self).__init__(name, descript, damage)
        self.damage = damage
        
class Cannon(Defense):
   def __init__(self, name, descript, damage):
        super(Cannon,self).__init__(name, descript, damage)  
        self.damage = damage
#__________________#__________________#__________________#__________________#__________________#__________________#__________________#__________________#__________________#_____________________  

#melee       
class Melee(Weapons):
   def __init__(self, name, descript, damage):
        super(Melee,self).__init__(name, descript, damage)
        self.damage = damage
        
class Battleaxe(Melee):#slash
   def __init__(self, name, descript, damage):
        super(Battleaxe,self).__init__(name, descript, damage) 
        self.damage = damage
        
class Whip(Melee):
   def __init__(self, name, descript, damage):
        super(Whip,self).__init__(name, descript, damage)
        self.damage = damage
        
class Sword(Melee):
   def __init__(self, name, descript, damage):
        super(Sword,self).__init__(name, descript, damage)
        self.damage = damage
#_______________________
                           
#ranged
class Ranged(Weapons):
   def __init__(self, name, descript, damage):
        super(Ranged,self).__init__(name, descript, damage)

class Javalin(Ranged):
   def __init__(self, name, descript, damage):
        super(Javalin,self).__init__(name, descript, damage)       
#__________________#__________________#__________________#__________________#__________________#__________________#__________________#__________________#__________________#_____________________
                                               
#throwing
class Throwing(Weapons):
   def __init__(self, name, descript, damage):
        super(Throwing,self).__init__(name, descript, damage)

class ThrowingKnife(Throwing):
   def __init__(self, name, descript, damage):
        super(ThrowingKnife,self).__init__(name, descript, damage)      
#__________________#__________________#__________________#__________________#__________________#__________________#__________________#__________________#__________________#_____________________
#armor
class Armor(Item):
   def __init__(self, name, descript, defense):
      super(Armor,self).__init__(name, descript, defense)
        
class Shield(Armor):
    def __init__(self, name, descript, defense):
      super(Shield,self).__init__(name, descript, defense)      

        
     
#__________________#__________________#__________________#__________________#__________________#__________________#__________________#__________________#__________________#_____________________                        
#consumable
class Consumable(Item):
   def __init__(self, name, descript):
        super(Consumable,self).__init__(name, descript)
##__________________#__________________#__________________#__________________#__________________#__________________#__________________#__________________#__________________#__________________#__________________#_____________________
class Drugs(Consumable):
   def __init__(self, name, descript, addhealth):
       super(Drugs,self).__init__(name, descript, addhealth)
        
#__________________#__________________#__________________#__________________#__________________#__________________#__________________#__________________#__________________#_____________________   
             
class Food(Consumable):
   def __init__(self, name, descript, addhealth):
        super(Food,self).__init__(name, descript, addhealth)
#__________________#__________________#__________________#__________________#__________________#__________________#__________________#__________________#__________________#_____________________
class Tools(Consumable):
   def __init__(self, name, descript):
        super(Tools,self).__init__(name, descript)
#___________________________________________________________________________           