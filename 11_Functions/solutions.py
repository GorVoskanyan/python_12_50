# 0       2       4       6       8       10
# 1       3       5       7       9       11
# 2       4       6       8       10      12
# 3       5       7       9       11      13
# 4       6       8       10      12      14
# 5       7       9       11      13      15

# solution 1
# for row in range(6):
#     for col in range(0, 11, 2):
#         print(row + col, end='\t')
#     print()


# 1
# 2       2
# 3       3       3
# 4       4       4       4
# 5       5       5       5       5

# solution 2
# rows_count = int(input("Enter rows count: "))
#
# for row in range(1, rows_count + 1):
#     for col in range(row):
#         print(row, end="\t")
#     print()


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

# solution 3
# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))
#
# for row in range(rows):
#     print('|', end='')
#     for col in range(cols):
#         if row == 0 or row == rows - 1:
#             print('-', end='')
#         else:
#             print(' ', end='')
#     print('|')


# solution 4
# numbers = int(input("Enter number of numbers: "))
# primes = 0

# for _ in range(numbers):
#     number = int(input("Enter number: "))
#     for div in range(2, number):
#         if number % div == 0:
#             break
#     else:
#         primes += 1

# print('Primes: ', primes)


# solution 5
# n = input('Enter number or q to quit: ')
# max_sum = 0

# while n != 'q':
#     n = int(n)
#     sum_ = 0
#     while n:
#         sum_ += n % 10
#         n //= 10
#     if sum_ > max_sum:
#         max_sum = sum_
#     n = input('Enter number or q to quit: ')

# print("Max sum is:", max_sum)



# solution 6
# height = int(input("Enter a height: "))

# for row in range(height):
#     # for space in range(height - row - 1, 0, -1):    # space_count = height - row - 1
#     #     print(end='   ')
#     # or
#     space_count = height - row - 1
#     print('   ' * space_count, end='')
#     for _ in range(row + 1):
#         print('#', end='    ')
#     print()


#             1
#          3    5
#       7    9    11
#    13    15    17    19
# 21    23    25    27    29

# solution 7
# height = int(input("Enter a height: "))
# number = 1

# for line in range(height):
#     # for space in range(height - line - 1, 0, -1):   # space_count = height - line -1
#     #     print(end='   ')
#     # or
#     space_count = height - line - 1
#     print('   ' * space_count, end='')

#     for _ in range(line + 1):
#         print(number, end='    ')
#         number += 2
#     print()


# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345

# solution 8
# height = int(input("Enter a height: "))

# for row in range(height):
#     for left_number in range(height, height - row - 1, -1):
#         print(left_number, end='')
    
#     point_count = 2 * (height - row - 1)
#     print('.' * point_count, end='')
    
#     for right_number in range(height - row, height + 1):
#         print(right_number, end='')
#     print()


# import main
# main.is_even(13)

# from main import is_even
# print(is_even(7))