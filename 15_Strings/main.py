# strings

# text = 'I\'m ok'
# text = "I'm ok"

# text = "he said \"ok\""
# text = 'he said "ok"'

# long_text = """My
# Long
# Text"""

# long_text = '''My
# Long
# Text'''
# print(long_text)


# iterate over string
# text = 'python'
# for char in text:
#     print(char, end='->')

# index, slice
# text = 'python'
# print(text[0])
# print(text[-1])
# text[0] = 'a'     # TypeError str is immutable

# first_half = text[ : len(text) // 2]
# print(first_half)

# text = 'python'
# l = list(text)
# l[0] = 'w'

# l = [char for char in text]
# for char in text:
#     l.append(char)
# print(l)
# nums_list = list(range(10))
# print(nums_list)

# new_text = str(l)
# print(type(new_text))
# for char in new_text:
#     print(char, end='>>')
# "['p', 'y']"


# string methods
# students = 'Aga, Lilit, Milena'
# l = students.split(', ')
# print(l)

# my_string = ', '.join(l)
# print(my_string)


# text = 'London is the capital of Great Britain.'
# words = text.split(' ')
# replaced_text = text.replace('London', 'Yerevan')
# print(replaced_text)
# print(text)
# print(words)

# if text.startswith('London'):
#     print('Valid')
    
# if text.endswith('Britain.'):
#     print('Valid')

# word = 'Britain.'

# if text[:len(word)] == word:
#     print('Valid')

# if text[-1 : -len(word)-1 : -1] == word[::-1]:
#     print('Valid')

# name_surname = 'london is the capital'
# capitalized_text = name_surname.capitalize()
# capitalized_text = name_surname.title()
# upper = name_surname.upper()
# lower = name_surname.lower()
# print(capitalized_text)

# db = ['Aga', 'Lilit']

# fullname = input('Enter name: ').capitalize()

# if fullname in db:
#     print('Welcome')

# text = '      ASC          '
# text = text.center(len(text) + 20, '-')
# text = text.center(200, '-')
# print(text)

# print(text.count('o'))
# print(text.index('w', 8, 30))
# print(text.find('w', 8, 30))

# print(text.isalnum())
# print(text.isalpha())
# print(text.isdigit())

# print(text.islower())
# print(text.isupper())

# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())


# string formatting
# product = 'Iphone15 PRO'
# price = 999.00
# quantity = 5

# result = str(quantity) + ' ' + product + ' ' + str(price * quantity) + '$'  # concatenation

# result = '{} {} total {}$'.format(quantity, product, price*quantity)
# result = '{1} {0} total {2}$'.format(quantity, product, price*quantity)
# result = '{q} {p} total {t}$'.format(q=quantity, p=product, t=price*quantity)

# Python 3.6 +  f-string
# result = f"{quantity:05d} {product:>30} total {(quantity * price):.2f}$"
# result = f"{quantity:05d} {product:^30} total {(quantity * price):.2f}$"

# result = "%05d %s total %.2f" % (quantity, product, quantity * price)
# print(result)

# def add(a, b):
#     print('Start to convert "a" to int')
#     a = int(a)
#     print('Succesfully converted "a"')
#     print()
#     print('Converting "b" to int')
#     b = int(b)
#     print('Succesfully converted')
#     print()
#     print('Run calculate result')
#     result = a / b
#     print('Result calculated')
#     return result


# result = add(5, 0)
# print(result)


