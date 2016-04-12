class Enemy(object):
    def __int__(self, health=100, attack=10):
        self.health = health
        self.attack = attack
   
    def attacks(self, target):
        target.damage(self.attack)
        return target.health
        
    def damage(self, amount):
        self.health -= amount
        
a = Enemy()
b = Enemy()