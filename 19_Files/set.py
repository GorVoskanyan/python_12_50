# set
# s = {1, 1, 1, 1, 2, 3, 4}
# l = [1, 1, 1, 1, 2, 2, 3]
# s = list(set(l))
# print(s)


# empty = set()
# empty.add(1)
# empty.update({3, 3, 4, 1, 2})
# empty.remove(2)
# empty.discard(2)
# empty.clear()
# empty.pop()
# print(type(empty))
# print(empty)


# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5, 1}

# print(s2.issubset(s1))
# print(s1.issuperset(s2))

# s3 = s1.intersection(s2)
# s3 = s1 & s2
# s1.intersection_update(s2)


# s3 = s1.difference(s2)
# s3 = s1 - s2
# s1.difference_update(s2)


# s3 = s1.symmetric_difference(s2)
# s3 = s1 ^ s2
# s1.symmetric_difference_update(s2)


# s3 = s1.union(s2)
# s3 = s1 | s2
# print(s3)


# s = {i ** 2 for i in range(10) if i % 2 == 0}
# s = sorted(s)
# print(s)

# words = ['this', 'is', 'a', 'test', 'of', 'sets']
# letters = ['s', 't']

# result = [word for word in words if set(word).issuperset(set(letters))]

# for word in words:
#     if set(word).issuperset(set(letters)):
#         result.append(word)
        
# print(result)