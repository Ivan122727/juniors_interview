from functools import wraps
from typing import Callable

def strict(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        arg_names = func.__code__.co_varnames
        # Объединяем args и kwargs для проверки типов
        combined_args = dict(zip(arg_names, args))
        combined_args.update(kwargs)
        for name, arg in combined_args.items():
            if type(arg) != annotations[name]:
                raise TypeError(f"Argument '{name}' must be of type {annotations[name].__name__}, "
                                f"got {type(arg).__name__}.")
        # Проверяем для результата функции
        res = func(*args, **kwargs)
        if type(res) != annotations['return']:
            raise TypeError(f"Argument 'return' must be of type {annotations['return'].__name__}, "
                            f"got {type(res).__name__}.")
        return res
    return wrapper
