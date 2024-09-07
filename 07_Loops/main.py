# while loops
# import time

# pin = input('Enter pin: ')
# count = 0

# while pin != '1793':
#     print('Lets try again')
#     count += 1                  # keep counter
#     if count == 5:
#         time.sleep(10)
#     elif count == 3:
#         time.sleep(5)
#     pin = input('Enter pin: ')
    
# print('Welcome')


# num = input('Enter num or enter for quit: ')
# count = 0
# summ = 0

# while num != '=':
#     summ += int(num)
#     count += 1
#     num = input('Enter num: ')
    
# print(summ / count)


# num = int(input('Enter num: '))

# while num:
#     print(num % 10, end='')
#     num //= 10
    
    
# infintie loop
# while True:
#     print('Type Ctrl-C to stop me...')


# break, continue
# while True:
#     num = int(input('Enter number: '))
#     if num == 0:
#         break
#     print(num ** 2)
  
   
#  
# i = 1
# while i < 10:
    # i += 1
    # if i % 2 != 0:
    #     continue
    # print(i)

    # if i % 2 == 0:
    #     print(i)
    # i += 1

# ------
# print('Calculator')
# length = input('Enter length or q for quit: ')

# while length != 'q':
#     length = float(length)
#     width = float(input('Enter width: '))
#     area = length * width
#     print(area, 'm^2')
#     length = input('Enter length or q for quit: ')
# -------------
 
    
# print(' ' * 10 + 'Welcome our first calculator!\n')

# main_menu = """1. Arithmetic calculator
# 2. Geometric calculator
# 3. Exit"""


# print(main_menu)
# choice = input('Select: ')

# while choice != '3':
#     if choice == '1':
#         x = int(input('>>> '))
#         operator = input('Enter operator: ')
#         y = int(input('>>> '))

#         if operator == '+':
#             print(x + y)
#         elif operator == '-':
#             print(x - y)
#         elif operator == '*':
#             print(x * y)
#         elif operator == '/':
#             print(x / y)
#         else:
#             print('Unknown oeprator')
#     elif choice == '2':
#         length = float(input('Enter length: '))
#         width = float(input('Enter width: '))
#         area = length * width
#         print(area, 'm^2')
#     else:
#         print('Please choose a 1, 2 or 3')
        
#     print(main_menu)
#     choice = input('Select: ')


# i = 1

# while i <= 10:
#     if i % 2 == 0:
#         print(i, '-', i**2)
#     else:
#         print(i, '-', i**3)
#     i = i + 1
# ------

# gumar = 0
# while n := input('Enter number or blank to stop: '):
#     gumar += int(n)

# print(gumar)


# -----
# nested loops
i = 1
while i < 10:
    j = 1
    while j < 10:
        print(f"{(i * j):4d}", end='')
        j += 1
    i += 1
    print()