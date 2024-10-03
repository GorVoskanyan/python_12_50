class Person:
    COUNT = 0
    
    def __init__(self, name, age):
        self.__age = age
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    
    @name.setter    
    def name(self, name):
        if name.isalpha():
            self.__name = name
    
    @property    
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if 1 < age < 100:
            self.__age = age
    
    @staticmethod
    def hello():
        print('Hello')
    
    @classmethod
    def count(cls):
        print(cls.COUNT)
    

person = Person(name='Spartak', age=20)
# person.hello()
person.count()
# print(person.age)
# person.age = 21
# print(person.age)