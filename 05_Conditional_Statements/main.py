# Conditional statements

# num = int(input('>>> '))

# if num % 2 == 0:
#     print(num, 'is even')
# else:
#     print(num, 'is odd')


# num = int(input('>>> '))

# if num > 0:
#     print('Positive.')
# elif num == 0:
#     print('Zero')
# else:
#     print('Negative.')


# _______
# print(bool(' '))

# is_rain = input('>>> ')

# if is_rain == '1':
#     print('Raining.')
# elif is_rain == '0':
#     print('Not rain')
# else:
#     print('please enter a 1 or 0')


# nested conditions
# num = int(input('>>> '))

# if num > 0:
#     print(num, 'is positive')
#     if num % 2 == 0:
#         print(num, 'is even')
#     else:
#         print(num, 'is odd')
# elif num < 0:
#     print(num, 'is negative')
# else:
#     print(num, 'is zero')


# x = 1

# if x:
#     y = 1
#     if y:
#         z = x + y
#         print(z)


# ternary operator
# x = 0
# is_even = True if x % 2 == 0 else False
# print(is_even)


# ________
print(' ' * 10 + 'Welcome our first calculator!\n')

main_menu = """1. Arithmetic calculator
2. Geometric calculator"""

print(main_menu)

choice = input('Select: ')

if choice == '1':
    x = int(input('>>> '))
    operator = input('Enter operator: ')
    y = int(input('>>> '))

    if operator == '+':
        print(x + y)
    elif operator == '-':
        print(x - y)
    elif operator == '*':
        print(x * y)
    elif operator == '/':
        print(x / y)
    else:
        print('Unknown oeprator')
elif choice == '2':
    length = float(input('Enter length: '))
    width = float(input('Enter width: '))
    area = length * width
    print(area, 'm^2')
else:
    print('Please choose a 1 or 2')
