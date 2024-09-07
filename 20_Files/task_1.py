# file = open('example.txt', 'w', encoding='utf-8')
# with open('example.txt', 'w', encoding='utf-8') as file:
#     file.write('1\n2\n3\n')

# with open('example.txt', 'a', encoding='utf-8') as file:
#     file.write('4\n5\n6\n')
#     file.writelines(['7\n', '8\n', '9\n'])

# with open('example.txt', 'r', encoding='utf-8') as file:
#     file.read()
#     file.readline()
#     file.readlines()

# with open('example.txt', 'r', encoding='utf-8') as file:
    # lines = file.readlines()
    # maximum = 0
    # for line in lines:
    #     line = line.rstrip()
    #     line = int(line)
    #     if line > maximum:
    #         maximum = line
    # print(maximum)
    
    # print(max([int(line.rstrip()) for line in file]))
    
    # file = file.read().split()
    # file = [int(number) for number in file]
    # print(file)
    
    
# with open('example.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
    # print(words)
    # print(type(words))
    
# words = open('example.txt', 'r', encoding='utf-8').read().split()

# maximum_length = len(max(words, key=len))
# for word in words:
#     if len(word) > maximum_length:
#         maximum_length = len(word)
        
# max_length_words = [word for word in words if len(word) == maximum_length]

# for word in words:
#     if len(word) == maximum_length:
#         max_length_words.append(word)
        
# print('Maximum length:', maximum_length)
# print('Words:', max_length_words)


# text = open('example.txt', 'r', encoding='utf-8').read().lower()
# data = dict()
# data = {char: text.count(char) for char  in text if char.isalpha()}

# for char in text:
#     if char.isalpha():
#         if char in data:
#             data[char] += 1
#         else:
#             data[char] = 1
            
# for key, value in data.items():
#     print(f"{key} -> {value}")

# words = open('example.txt', 'r', encoding='utf-8').read().split()
# data = {word: words.count(word) for word in words}
# print(data)

