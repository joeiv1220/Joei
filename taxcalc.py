class tax:
    def __int__(self, name, gross_income, dependents):
        self.name = name
        self.dependents = dependents
        self.gross_income = gross_income    
       
        
    def tcalc(self):
        total = self.gross_income - 10000 - 2000 * self.dependents
        intax = total * 0.2
        return intax