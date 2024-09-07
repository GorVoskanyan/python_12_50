# list comprehension

# my_list = []
# for i in range(10):
#     my_list.append(i)

# my_list = [i for i in range(10)]

# my_list = []
# for i in range(10):
#     if i % 2 == 0:
#         my_list.append(i)
        
# my_list = [i for i in range(10) if i % 2 == 0]

# my_list = []
# for i in range(10):
#     if i % 2 == 0:
#         my_list.append(i)
#     else:
#         my_list.append('odd')

# my_list = [i if i % 2 == 0 else 'odd' for i in range(10)]
# print(my_list)


# my_list = ['1', '2', '3']
# numbers_list = []

# for i in my_list:
#     numbers_list.append(int(i))

# numbers_list = [int(i) for i in my_list]
# numbers_list = list(map(int, my_list))
# print(numbers_list)


# nested lists
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]


# unpacked_matrix = []
# for elem in matrix:
#     # print(elem)
#     for subelem in elem:
#         print(subelem, end=' ')
#         unpacked_matrix.append(subelem)
#     print()


# unpacked_matrix = [subelem for elem in matrix for subelem in elem]

# matrix = [[0] * 3 for _ in range(3)]
# print(matrix)

# for elem in matrix:
#     print(elem)
# print(unpacked_matrix)
# print(matrix)
# print(len(matrix))

# import time

# start = time.time()
# my_list = []
# for i in range(100):
#     for j in range(100):
#         for k in range(100):
#             if i ** 2 + j ** 2 == k ** 2:
#                 my_list.append([i, j, k])

# runtime = time.time() - start 

# print(runtime, 'seconds')


# s = time.time()
# l = [
#     [i, j, k]
#     for i in range(100) 
#     for j in range(100) 
#     for k in range(100) 
#     if i ** 2 + j ** 2 == k ** 2
#     ]
# r = time.time() - s
# print(r, 'seconds')