from typing import Callable
from functools import wraps

def how_are_you(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        input('Inch ka chka? ')
        print('Im mot vabshe ban chka!!')
        result = func(*args, **kwargs)
        return result
    return wrapper


@how_are_you
def test():
    print('Inch vor ban...')
    
test()    