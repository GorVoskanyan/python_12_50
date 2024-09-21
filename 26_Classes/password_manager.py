class PasswordManager:
    def __init__(self) -> None:
        self.old_passwords: list = []
        
    def get_password(self) -> str:
        return self.old_passwords[-1]
        
    def set_password(self, password: str) -> None:
        if password not in self.old_passwords:
            self.old_passwords.append(password)
        
    def is_correct(self, password: str) -> bool:
        return password == self.get_password()
        


if __name__ == '__main__':
    # create instance
    password_manager = PasswordManager()

    password_manager.set_password('qwerty')
    # current_password = password_manager.get_password()
    password_manager.set_password('user123')
    password_manager.set_password('qwerty')
    password_manager.set_password('qwertyuiop')
    current_password = password_manager.get_password()
    print(current_password)
    print(password_manager.old_passwords)

    if password_manager.is_correct('qwertyuiop'):
        print('Password is true')
    else:
        print('Wrong password')
        
        
        