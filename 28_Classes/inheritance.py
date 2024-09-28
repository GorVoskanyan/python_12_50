class Pet(object):
    legs = 4
    has_a_tail = True
        
    def __str__(self):
        return f"Legs: {self.legs}\tHas a tail: {'Yes' if self.has_a_tail else 'No'}"
    
    
class Cat(Pet):
    def sound(self):
        print('Meow!')
        
    
class Dog(Pet): 
    def sound(self):
        print('Woof!')
        
    
class Frog(Pet):
    has_a_tail = False
    
    def sound(self):
        print('Kwa!')
        
        
cat = Cat()
dog = Dog()
frog = Frog()
print(cat)
print(dog)
print(frog)
cat.sound()
dog.sound()
frog.sound()