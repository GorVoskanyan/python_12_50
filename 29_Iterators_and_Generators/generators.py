def fibonacci(number):
    cur_value, next_value = 0, 1
    for _ in range(number):
        yield cur_value
        cur_value, next_value = next_value, cur_value + next_value
        if cur_value > 10:
            return

# fibo_10 = fibonacci(10)
# print(type(fibo_10))
# for elem in fibo_10:
#     print(elem)


# generator expressions
# my_gen = (i for i in range(10) if i % 2 == 0)
# print(type(my_gen))
# print(sum(my_gen))
# for elem in my_gen:
#     print(elem)

list_gen = [i for i in range(10)]
print(list_gen)
 