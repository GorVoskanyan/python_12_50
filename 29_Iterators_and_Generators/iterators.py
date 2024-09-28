# Iterators

# l = [10, 20, 30]
# for elem in l: print(elem)

# iterator = l.__iter__()
# print(iterator)
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())

# iterator = iter(l)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for elem in iterator: print(elem)
# for elem in iterator: print(elem)


l = [10, 20, 30]

# iterator = l.__iter__()
iterator = iter(l)

while iterator:
    try:
        # print(iterator.__next__())
        print(next(iterator))
    except StopIteration:
        print('Iterator is empty')
        break