class Person:
    __count = 0 # private attribute
    
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)
        if Person.__count <= 5:
            Person.__count += 1
        else:
            raise Exception('Persons must be a less than 5')

    def __str__(self):
        return f"Name: {self.__name}\tAge: {self.__age}"
    
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
            
            
class Citizen(Person):
    def __init__(self, name, age, city):
        super().__init__(name, age)
        self.city = city
        
    def __str__(self):
        return super().__str__() + f'\tCity: {self.city}'
    

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def __str__(self):
        return super().__str__() + f"\tSalary: {self.salary}"
    

citizen = Citizen('Sergey', 20, 'Yerevan')
print(citizen)
employee = Employee('Spartak', 20, 1000)
print(employee)