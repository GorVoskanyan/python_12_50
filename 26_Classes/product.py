class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
        
    def get_price(self, items_quantity):
        if items_quantity < 10:
            return self.price * items_quantity
        elif 10 < items_quantity < 100:
            return (self.price * items_quantity) * .9
        elif items_quantity > 100:
            return self.price * items_quantity * .8
        
    def make_purchase(self, items_quantity):
        if items_quantity <= self.amount:
            return self.get_price(items_quantity)
        else:
            return 'Not enough product'
        
obj = Product(name='Smartphone', amount=100, price=1000)
# print(obj.get_price(150))
total = obj.make_purchase(90)
print(total)