from functools import wraps


def strict(func: callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        # Проверяем для args
        for arg, (name, expected_type) in zip(args, annotations.items()):
            if not isinstance(arg, expected_type):
                raise TypeError(f"Argument '{name}' must be of type {expected_type.__name__}, "
                                f"got {type(arg).__name__}.")
        # Проверяем для kwargs
        for name, value in kwargs.items():
            if name in annotations:
                expected_type = annotations[name]
                if not isinstance(value, expected_type):
                    raise TypeError(f"Argument '{name}' must be of type {expected_type.__name__}, "
                                    f"got {type(value).__name__}.")
        # Проверяем для результата функции
        res = func(*args, **kwargs)
        if not isinstance(res, annotations['return']):
            raise TypeError(f"Argument 'return' must be of type {annotations['return'].__name__}, "
                            f"got {type(res).__name__}.")
        return res
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def divide_two(a: int, b: int) -> int:
    return a / b


if __name__ == "__main__":
    print(sum_two(1, 2))  # >>> 3
    print(sum_two(1, 2.4))  # >>> TypeError
    print(divide_two(a=2, b=1))  # >>> TypeError
