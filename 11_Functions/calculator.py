def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
     return x * y
 
def div(x, y):
    return x // y


def main():
    print('Welcome ...')
    choice = input('1. Add\n2. Sub\n3. Mult\n4. Div\nSelect: ')
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    
    if choice == '1':
        result = add(a, b)
    elif choice == '2':
        result = sub(a, b)
    elif choice == '3':
        result = mult(a, b)
    elif choice == '4':
        result = div(a, b)
    else:
        print('Invalid input!')
        
    print('Result is:', result)
    
main()
