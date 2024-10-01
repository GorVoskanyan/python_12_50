from typing import Callable
from functools import wraps

def decorator(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Some code before function work
        result = func(*args, **kwargs)
        # Some code after function work
        return result
    return wrapper
