class BankAccount:
    
    def __init__(self, card_holder, pin, balance):
        self.set_card_holder(card_holder)
        self.set_pin(pin)
        self.set_balance(balance)
            
    def get_card_holder(self):
        return self.__card_holder
    
    def set_card_holder(self, card_holder_name):
        if card_holder_name.isalpha():
            self.__card_holder = card_holder_name
        else:
            print('Invalid card holder name!')
            
    def get_pin(self):
        return self.__pin
    
    def set_pin(self, pin):
        if len(pin) == 4 and pin.isdigit():
            self.__pin = pin
        else:
            print('Invalid pin!')
            
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        if balance > 0:
            self.__balance = balance
        else:
            print('invalid balance!')
            self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
 
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            
    def transfer(self, amount, another_bank_account):
        if isinstance(another_bank_account, BankAccount):
            if self.__balance >= amount:
               self.__balance -= amount
               another_bank_account.__balance += amount
               print('Succesfully')
            else:
                print('Not enough money')
        else:
            print('Invalid bank account') 
                        
            
bank_account2 = BankAccount(card_holder='Spartak', pin='4321', balance=5000)
bank_account = BankAccount(card_holder='Andre', pin='1234', balance=10000)

print(bank_account.get_balance())

bank_account.deposit(10000)
print(bank_account.get_balance())

bank_account.withdraw(5000)
print(bank_account.get_balance())

bank_account.transfer(amount=10000, another_bank_account=bank_account2)
print(bank_account.get_balance())
print(bank_account2.get_balance())
