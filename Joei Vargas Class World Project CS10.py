import sys

class Item:
    def __int__ (self, name, descript):
        self.name = name
        self.descript = descript

class Armor(object):
    def __int__ (self, health = 100, defense = 0):
        self.health = health
        self.defense = defense
   
    def shield(self, target):
        target.damage(self.defense)
        return target.health
    

class Enemy(object):
    def __int__(self, health=100, attack=10):
        self.health = health
        self.attack = attack
   
    def attacks(self, target):
        target.damage(self.attack)
        return target.health
        
    def damage(self, amount):
        self.health -= amount
        
#weapon
class SuperWeapons(Item):
   def __int__(self, name, value, attack):
       self.name = name
       self.value = value
       self.attack = attack
      
class Ranged(SuperWeapons):
    def __int__ (self, health = 100, defense):
        self.health = health
        self.defense = defense
        
class Throwing(SuperWeapons):
    def __int__ (self, axe = 10, chain = 5, dart = 10, javalin = 15, knife = 20, stick = 5):
        self.axe = axe
        self.chain = chain
        self.dart = dart
        self.javalin = javalin
        self.knife = knife
        self.stick = stick
        
class Melee(SuperWeapons):
    def __int__ (self, bowieknife = 20, sickle = 10):
        self.bowieknife = bowieknife
        self.sickle = sickle
    
class Ranged(SuperWeapons):
    def __int__ (self, arrow = 20, crossbow = 10, bow = 15 , headcannon = .5):
        self.arrow = arrow
        self.crossbow = crossbow
        self.bow = bow
        self.headcannon = headcannon
        
class Throwing(SuperWeapons):
    def __int__ (self, axe = 10, chain = 5, dart = 10, javalin = 15, knife = 20, stick = 5):
        self.axe = axe
        self.chain = chain
        self.dart = dart
        self.javalin = javalin
        self.knife = knife
        self.stick = stick
        
class Melee(SuperWeapons):
    def __int__ (self, bowieknife = 20, sickle = 10):
        self.bowieknife = bowieknife
        self.sickle = sickle
        
#class SuperWeapons(Item):
   # def __int__(self, name, value, attack):
    #    self.name = name
    #    self.value = value
      #  self.attack = attack
 
#class Ranged(SuperWeapons):
   # def __int__ (self, arrow = 20, crossbow = 10, bow = 15 , headcannon = .5):
   #    self.arrow = arrow
    #    self.crossbow = crossbow
    #    self.bow = bow
    #    self.headcannon = headcannon
        
#class Throwing(SuperWeapons):
  #  def __int__ (self, axe = 10, chain = 5, dart = 10, javalin = 15, knife = 20, stick = 5):
  #      self.axe = axe
   #     self.chain = chain
   #     self.dart = dart
  #      self.javalin = javalin
  #      self.knife = knife
  #     self.stick = stick
        
#class Melee(SuperWeapons):
 #  def __int__ (self, bowieknife = 20, sickle = 10):
   #     self.bowieknife = bowieknife
   #     self.sickle = sickle
  
#class Ranged(SuperWeapons):
 #   def __int__ (self, arrow = 20, crossbow = 10, bow = 15 , headcannon = .5):
 #      self.arrow = arrow
  #      self.crossbow = crossbow
   #     self.bow = bow
  #      self.headcannon = headcannon
        
#class Throwing(SuperWeapons):
 #   def __int__ (self, axe = 10, chain = 5, dart = 10, javalin = 15, knife = 20, stick = 5):
  #      self.axe = axe
   #     self.chain = chain
   #     self.dart = dart
     #   self.javalin = javalin
      #  self.knife = knife
       # self.stick = stick
        
#class Melee(SuperWeapons):
 #   def __int__ (self, bowieknife = 20, sickle = 10):
  #      self.bowieknife = bowieknife
   #     self.sickle = sickle
    
