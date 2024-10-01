import time
from typing import Callable

def timer(func: Callable, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    runtime = end - start
    print(f'Function works: {runtime:.4f} seconds')
    return result
    
def square_sum() -> int:
    return sum(i ** 2 for i in range(10000))

def cubes_sum(number: int) -> int:
    return sum(i ** 3 for i in range(number + 1))


print(timer(square_sum))
print(timer(cubes_sum, 10000))