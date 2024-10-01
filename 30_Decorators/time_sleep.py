from time import sleep
from typing import Callable, Any
from functools import wraps

def time_sleep(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        sleep(3)
        return func(*args, **kwargs)
    return wrapper


@time_sleep
def test():
    print('Request to ...')
    
test()