class User:
    def __init__(self, name, age):  # constructor
        self.name = name
        self.age = age
        self.is_banned = False
        self.friends = []
                
    def print_info(self):           # method
        print(f"Name: {self.name}\nAge: {self.age}\nBan status: {self.is_banned}")
        
    def add_friend(self, friend):
        if isinstance(friend, User):
            self.friends.append(friend.name)

    def __str__(self):
        return f"Name: {self.name}\tAge: {self.age}\tFriends: {self.friends}"

# user1 = User('Alex', 20)
# user2 = User(name='Ben', age=30)

# print(user2.name, user2.age, user2.is_banned)
# user2.print_info()
# print(user1)
# user1.print_info()

# user1.add_friend(user2)
# print(user1.friends)



class MyList:
    def __init__(self):
        self.zambyux = []
        
    def avelacnel(self, element):
        self.zambyux += [element]
    
    def __str__(self):
        return '<<' + ', '.join(self.zambyux) + '>>'
        
l = MyList()
l.avelacnel('a')
l.avelacnel('b')
l.avelacnel('c')

# print(l.zambyux)
print(l)