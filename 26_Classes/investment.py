class Investment:
    def __init__(self, principal, interest):
        self.p = principal
        self.i = interest
        
    def value_after(self, n):
        return self.p * (1 + self.i) ** n
    
    def __str__(self) -> str:
        return f"Principal - ${self.p:.2f}, Interest rate - {self.i}%"
    
    
obj = Investment(1000, 5.12)
after_one_year = obj.value_after(1)
# print(obj)
print(after_one_year)