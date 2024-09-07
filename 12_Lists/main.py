# Built-in collections
# Lists are mutable collection

# numbers = [1, 2, 3, 4, 5]
# numbers.append(6)
# print(numbers)
# print(type(numbers))

# mutable vs immutable
# my_string = 'python'
# my_list = ['p', 'y', 't', 'h', 'o', 'n']

# print(my_string[0])
# print(my_list[0])

# my_string[0] = 'x'
# print(id(my_string))
# my_string = my_string + 'x'
# print(id(my_string))
# print(my_string)

# print(id(my_list))
# my_list[0] = 'x'
# print(my_list)
# print(id(my_list))


# empty = []
# print(empty)
# print(type(empty))

# for num in range(10):
#     empty.append(num)
#     empty = empty + [num]
    
# print(empty)

# my_string = 'python'
# my_list = list(my_string)
# my_list = []
# for char in my_string:
#     my_list.append(char)
# print(my_list)


# my_list = []
# for number in range(1, 21):
#     if number % 2 == 0:
#         my_list.append(number ** 2)
# print(my_list)


# lst = [10, -20, 30, 40]
# print(lst[-2:-4:-1])
# minimum = lst[0]
# maximum = lst[0]

# for element in lst[1:]:
#     if element < minimum:
#         minimum = element
#     elif element > maximum:
#         maximum = element

# print(minimum)
# print(maximum)


# students = ['Astghik', 'Lilit', 'Milena', 'Emilia', 'Narek']

# while True:
#     student_name = input('Enter student name or "q" for quit: ')
#     if student_name == 'q':
#         print('Bye bye')
#         break
    
#     for student in students:
#         if student_name == student:
#             print('Ok')
#             break
#     else:
#         print('Unknown student')
#         students.append(student_name)
#         print('Student', student_name, 'succesfully aded on list')


# students = ['Astghik', 'Lilit', 'Milena']
# students.remove('Astghik')
# del students[0]
# students.pop(0)
# print(students)


# s = input('>>> ')
# changed = s[1] + s[0] + s[2:]
# print(changed)


# lst = [2, 4, 6, 8]

# for num in lst:
#     print(num, num ** 2, num ** 3)


# l1 = [1, 3, 5, 10, 9]
# l2 = [2, 4, 6, 8, 7]

# result = l1 + l2
# result.sort()
# print(result)
# l1.extend(l2)
# print(l1)

# result = []
# for elem1, elem2 in zip(l1, l2):
#     result.append(elem1)
#     result.append(elem2)
    
# print(result)


# prices = [3.45, 6.34, 7.5, 1.2, 3.4, 9.8]
# new_prices = []

# for price in prices:
#     if price > 5:
#         new_price = price * 0.9
#         new_prices.append(new_price)
#     else:
#         new_prices.append(price)
        
# print(prices)
# print(new_prices)


# students = ['Astghik', 'Lilit', 'Milena']

# for element in students:
#     print(element)
#     print(students.index(element))

# for index in range(len(students)):
#     print(index, students[index])

