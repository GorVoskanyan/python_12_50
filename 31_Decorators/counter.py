from typing import Callable, Any
from functools import wraps

def counter(func: Callable) -> Callable:
    count = 0
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        nonlocal count
        count += 1
        # wrapper.count += 1
        res = func(*args, **kwargs)
        # print(wrapper.count)
        print(count)
        return res
    # wrapper.count = 0
    return wrapper


@counter
def test(): print('ok')

test()
test()
test()
