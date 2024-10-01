import time
from typing import Callable

def timer(func: Callable):
    def wrapped_func(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        print(f'Function works: {runtime:.4f} seconds')
        return result
    return wrapped_func


@timer    
def square_sum() -> int:
    return sum(i ** 2 for i in range(10000))

@timer
def cubes_sum(number: int) -> int:
    return sum(i ** 3 for i in range(number + 1))


my_square_sum = square_sum()
my_cubes_sum = cubes_sum(10000)

print(my_square_sum)
print(my_cubes_sum)