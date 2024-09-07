# files
# file = open('text.txt', 'w', encoding='utf-8')
# file = open('text.txt', 'a', encoding='utf-8')
# file = open('text.txt', 'r', encoding='utf-8')

# file.write('Hello\nWorld\n!\n')
# file.writelines([f"{i} - {i ** 2}\n" for i in range(1, 10)])
# l = [f"{i} - {i ** 2}\n" for i in range(1, 10)]
# print(l)
# one_string = file.read()
# one_string = file.read(5)

# file.close()
# one_line = file.readline()
# one_line = file.readline()
# one_line = file.readline()
# one_line = file.readline(3)

# all_lines = file.readlines()[-1]
# print(all_lines)


# iterate over files
# for line in file:
#     print(line.rstrip())

# for char in file.read():
#     print(char)

# for line in file.readlines():
#     print(line.strip())



# context manager
# with open('text.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         print(line.rstrip())
        
# print('ok')