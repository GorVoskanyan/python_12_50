# class MyError(BaseException):
#     pass

# raise MyError('ERRROR!!')

# try:
#     a = int(input('>>> '))
#     b = int(input('>>> '))
#     print(a + b)
# except ValueError as message:
#     print(message)
# print('ok')


# try:
#     with open('test.txt', 'r', encoding='utf-8') as file:
#         print(''.join(line.rstrip()) for line in file)
# except FileNotFoundError:
#     open('test.txt', 'x')
#     print('File succesfully created')


# try:
#     open('test.txt', 'x')
# except FileExistsError:
#     with open('test.txt', 'r', encoding='utf-8') as file:
#         print((''.join(line.rstrip()) for line in file))
# finally:
#     file.close()
#     print('File closed')