class Cheese:
    def __int__(self, color, origin, texture, cheese_type, weight):
        self.age= 0
        self.color = color 
        self.origin = origin 
        self.shape
        self.texture = texture
        self.type = cheese_type
        self.weight = weight
        
    def eat(self, amount):
        self.weight -= amount
    
    def melt(self):
        self.texture = "creamy"
        self.shape = "liquid-ish"
        