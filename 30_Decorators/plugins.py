from typing import Callable, Dict

PLUGINS: Dict[str, Callable] = dict()

def register(func: Callable) -> Callable:
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name: str) -> str:
    return f"Hello, {name}"


def say_goodbye(name: str) -> str:
    return f"Goodbye, {name}"


print(say_hello('Sergey'))
print(PLUGINS)