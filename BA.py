class BA:
    def __int__(self):
        self.bal = 0
        
    def deposit(self, amount):
        self.bal += amount
        return self.bal
        
    def withdraw(self, amount):
        self.bal -= amount
        return self.bal
        