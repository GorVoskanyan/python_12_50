# the next prime number
# number = int(input('Enter number: '))

# while True:
#     number += 1
#     for divider in range(2, number):
#         if number % divider == 0:
#             break
#     else:
#         print('Next prime number:', number)
#         break
        

# words = 'madam', 'engine', 'level', 'python'

# for word in words:
#     print(word, end=': ')
#     while word != '':
#         if word[0] != word[-1]: # indexing
#             print('is not palindrome')
#             break
#         word = word[1:-1]   # sliceing
#     else:
#         print('is palindrome')


# matrix
# 1 0 0 0 0
# 2 1 0 0 0
# 2 2 1 0 0
# 2 2 2 1 0
# 2 2 2 2 1

# template for nested loops
# size = 5
# for row  in range(size):
#     for col in range(size):
#         if row == col:
#             print(1, end='  ')
#         elif col > row:
#             print(0, end='  ')
#         else:
#             print(2, end='  ')
#     print()



# draw coordinate plane
#          |
#          |
#          |
# ---------------------         
#          |
#          |
#          |

# height = int(input('Enter height: '))
# width = int(input('Enter width: '))

# for row in range(height):
#     for col in range(width):
#         if col == width // 2:
#             print('|', end='')
#         elif row == height // 2:
#             print('-', end='')
#         else:
#             print(' ', end='')
#     print()        


# ================================
# |-----------------------------|
# |                             |
# |                             |
# |                             |
# |                             |
# |                             |
# |                             |
# |                             |
# |                             |
# |                             |
# |-----------------------------|

height = int(input('Enter height: '))
width = int(input('Enter width: '))

for row in range(height):
    for col in range(width):
        if col == 0 or col == width - 1:
            print('|', end='')
        elif row == 0 or row == height - 1:
            print('-', end='')
        else:
            print(' ', end='')
    print()