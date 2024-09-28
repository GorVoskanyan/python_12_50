class Person:
    __count = 0 # private attribute
    
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
        if Person.__count <= 5:
            Person.__count += 1
        else:
            raise Exception('Persons must be a less than 5')
    
    def get_count(self):        # getter
        return Person.__count

    def get_age(self):
        return self.__age
    
    def set_age(self, age):     # setter
        if age in range(1, 100):
            self.__age = age
        else:
            print('Age must be a range 1, 100')

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            print('Name must be alpha')
            
    
person = Person('Spartak', 20)
# Person.__count -= 10
person2 = Person('Astghik', 10)
person2 = Person('Astghik', 10)
person2 = Person('Astghik', 10)
person2 = Person('Astghik', 10)
person2 = Person('Astghik', 10)
person2 = Person('Astghik', 10)
print(person2.get_count())

# person2._Person__name = 'Gor'   # name mangling
# print(person2.get_name())

# person2.set_name('Astghik')
# print(person2.get_name())

# person2.set_age(99)
# print(person2.get_age())