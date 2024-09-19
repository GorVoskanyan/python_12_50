# lambda functions
# add = lambda x, y: x + y
# res = add(3, 4)
# print(res)

# map, filter, reduce
# data = [1, 2, 3, 4]
# float_data = list(map(float, data))
# float_data = list(map(lambda x: x ** 2, data))
# print(float_data)
# for num in float_data: print(num)

# data = [(3, 2), (2, 1), (1, 1.5)]
# data.sort(key=lambda t: t[1])
# print(data)


# def f(x):
#     return lambda y: x + y

# res = f(3)(4)
# print(res)


# data = [3, -3, 5, 8, -8, 9, -2]
# filtered_data = list(filter(lambda num: num > 0, data))
# print(filtered_data)


# from functools import reduce

# data = [1, 2, 3, 4, 5]
# _sum = reduce(lambda x, y: x+y, data)
# print(_sum)



# data = list(map(int, input('Enter numbers seperated by a comma: ').split(',')))
# print(data)


# # result = lambda a, b, step: [num for num in range(a, b+1, step)]
# # print(result(10, 100, 20))

# def f(a, b, step):
#     result = []
#     for num in range(a, b+1, step):
#         result.append(num)
    
#     return result

# result = f(1, 5, 1)
# print(result)



# [3, 7, 12, 5, 20, 0] [21, 84, 60, 100, 0]
# [1, 1, 4, 32, 6] [1, 4, 128, 192]


# def f(l: list) -> list:
#     return [l[i] * l[i+1] for i in range(len(l) - 1)]

# r = f([1, 1, 4, 32, 6])
# print(r)


# word =  "_, we have a _."
# data = ["Ashot", "problem"]

# word = word.replace('_', data[0], 1)
# word = word.replace('_', data[1], 1)
# print(word)


words = ["anymore", "raven", "me", "communicate"]
min_len, max_len = len(min(words, key=len)), len(max(words, key=len))
print(min_len + max_len)
