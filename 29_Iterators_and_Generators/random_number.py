import random

class RandomNumber:
    def __init__(self, limit):
        self.__limit = limit
        self.__counter = 0
    
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.__counter < self.__limit:
            self.__counter += 1
            # return __import__('random').randint(1, 10)
            return random.randint(1, 10)            
        else:
            raise StopIteration
        
random_number = RandomNumber(limit=3)

# print(random_number.__next__())
# print(random_number.__next__())
# print(random_number.__next__())
# print(random_number.__next__())

for elem in random_number: print(elem)