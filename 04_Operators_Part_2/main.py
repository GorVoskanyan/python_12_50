# print function param sep, end

# print('Hello', 'World', sep='__')

# print('Hello', end='||')
# print('World')

# text = 'Python\n'
# print(text * 5, end='')


# assignment operators
# a = 5
# # a = a + 5
# a += 5  # a = a + 5
# a -= 3  # a = a - 3
# a *= 4  # a = a * 4
# a /= 7  # a = a / 7
# a //= 3 # a = a // 2
# a **= 3 # a = a ** 3
# a %= 3  # a = a % 3
# print(a)


# identity operators
# a = 5
# b = 7
# print(a is b)
# print(a is not b)
# print(id(a))
# print(id(b))


# membership operators
# word = 'python'
# print(word[0])    # indexing
# letter = 'tho'
# print(word.index('t'))

# print(letter in word)
# print(letter not in word)

# num = 1234
# digit = 2

# print(digit in num)


# logical operators

# result = 5 > 3 and 10 > 19 and 3 > 1 and 2 > -2
# result = 5 > 3 or 10 > 19 or 3 < 1 or 2 < -2
# print(result)

# result = (5 > 3 or 4 < 2) and 3 == 4
#        True   and    False
#              False

# result = True
# print(not result)


# username = input('Enter username: ')
# password = input('Enter password: ')

# t = 'python'
# length_t = len(t)
# print(length_t)

# if 'admin' in username and len(password) >= 8:
#     print('Welcome!')
# else:
#     print('Try again!')


# bitwise operators
#       8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
#   33      1   0   0   0   0   1   0   0                  
#   23                          1   0   1 |
#   &               0   0   0   0   0   1     
#   |               1   1   0   1   1   1
#   ^               1   1   0   1   1   0
#   ~
#   <<  
#   >>                                        
a = 33
# print(bin(a))
b = 23
bitwise_and = a & b
bitwise_or = a | b
bitwise_xor = a ^ b
bitwise_not = ~ a
left_shift = a << 2
a <<= 2
right_shift = b >> 2
b >>= 2
print(b)
