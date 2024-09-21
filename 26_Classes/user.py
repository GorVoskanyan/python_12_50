from password_manager import PasswordManager


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.password_manager = PasswordManager()
        
# user1 = User(name='Alex', age=20)
# user1.password_manager.set_password('qwerty')

# user1.password_manager.set_password('OOP')
# current = user1.password_manager.get_password()
# print(current)