# List methods

# class im_list:
#     def __init__(self):
#         self.l = []
#     def avelacnel_verjic_amenaverjic(self, number):
#         self.l += [number]

#     def __str__(self):
#         return f"{self.l}"
        
# l = list()
# print(l)
# l.append(1)
# print(l)

# im_l = im_list()
# im_l.avelacnel_verjic_amenaverjic(-1)
# print(im_l)


students = ['Astghik', 'Aga', 'Lilit']

# adding
students.append('Milena')
students.insert(3, 'Emilia')

new_students = ['Narek', 'Sergey']
# new_students = 'Milena'
students.extend(new_students)


# removing
students.remove('Milena')
deleted_student = students.pop(0)
# print(deleted_student)
# students.clear()

# count, index
students.append('Emilia')
students.append('Emilia')
# print(students)
# print(students.count('Emilia'))
emilia_count = students.count('Gor')
emilia_index = students.index('Emilia')
emilia_index = students.index('Emilia', 3)
emilia_index = students.index('Emilia', 3, 10)
# print(emilia_index)


# sort, reverse
# students.append('aga')
# students.sort(reverse=True)
# def my_lower(elem): return elem.lower()
# students.sort(key=str.lower)
# students.sort(key=my_lower)
# students.sort(key=lambda elem: elem.lower())
# students.sort(key=lambda elem: elem.lower(), reverse=True)

# students.reverse()
# print(students)

# copy
import copy

students.append(['Spartak', 'Artur'])
# students_copy = students.copy()
# students_copy = students[:]
students_copy = copy.deepcopy(students)
print(id(students))
print(id(students_copy))

students_copy[-1][-1] = 'Milena'
# print(students_copy)

# del students[0]
# del students[-1]
# del students

# print(students)

