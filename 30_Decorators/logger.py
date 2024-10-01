import time
import functools
from typing import Callable, Any

def timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        print(f'Function works: {runtime:.4f} seconds')
        return result
    return wrapped_func

def logging(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print(
            f"Function {func.__name__} start work.\n"
            f"Function docs: {func.__doc__}\n"
            f"Arguments: {args}\t"
            f"Keyword arguments: {kwargs}"
            )
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} succesfully ended")
        return result
    return wrapper

@logging
@timer    
def square_sum() -> int:
    """ Simple function."""
    return sum(i ** 2 for i in range(10000))

@timer
@logging
def cubes_sum(number: int) -> int:
    return sum(i ** 3 for i in range(number + 1))


my_square_sum = square_sum()
my_cubes_sum = cubes_sum(10000)

print(my_square_sum)
# print(my_cubes_sum)
