from typing import Callable, Any
from functools import wraps
import datetime

def logger(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        try:
            print(f'Function {func.__name__} start work...')
            res = func(*args, **kwargs)
            print(f'Function {func.__name__} end work...')
            return res
        except Exception as msg:
            with open('errors.txt', 'a', encoding='utf-8') as log_file:
                log_file.write(
                    f"[{__name__}] - [{func.__name__}] - [{datetime.datetime.now()}] - [{msg}]\n"
                )
        
    return wrapper


@logger
def test(a, b):
    return a / b


test(1, 0)
