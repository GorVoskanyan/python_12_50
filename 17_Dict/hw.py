# data = {
#     '1': '.,?!:',
#     '2': 'ABC',
#     '3': 'DEF',
#     '4': 'GHI',
#     '5': 'JKL',
#     '6': 'MNO',
#     '7': 'PQRS',
#     '8': 'TUV',
#     '9': 'WXYZ',
#     '0': ' '
# }

# text = input('>>> ').upper()
# converted = ''

# for char in text:
#     for key, value in data.items():
#         if char in value:
#             quantity = value.index(char) + 1
#             converted += quantity * key
    
# print(converted)


s1 = input('>>> ')
s2 = input('>>> ')
d1 = {char: s1.count(char) for char in s1}
d2 = {c: s2.count(c) for c in s2}
if d1 == d2:
    print('Anagrama')
else:
    print('Anagrama chi')
    
