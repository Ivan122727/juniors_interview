import unittest

from solution_v2 import strict


@strict
def sum_two_k_times(count: int, a: float, b: float) -> float:
    """Сумма двух чисел count раз

    Args:
        count (int): количество раз
        a (float): первое число
        b (float): второе число

    Returns:
        float: сумма а и b, count раз
    """
    res = 0.0
    for i in range(count):
        res += (a + b)
    return res


@strict
def num_to_bool(value: bool) -> int:
    """Перевод лог выражения в число

    Args:
        value (bool): _description_

    Returns:
        int: переведенное число
    """
    return int(value)


@strict
def square_of_int(num: int) -> int:
    """Квадрат целого числа

    Args:
        num (int): число

    Returns:
        int: квадрат числа
    """
    return num * num


@strict
def sqrt_of_float(num: float) -> float:
    """Квадратный корень из числа

    Args:
        num (float): число

    Returns:
        float: корень числа
    """
    return num ** 0.5


@strict
def upper_str(text: str) -> str:
    """Перевод текста в заглавный

    Args:
        text (str): текст для перевода

    Returns:
        (str): заглавный текст
    """
    return text.upper()

# Функции для return
@strict
def func_to_bool_return_int() -> bool:
    """
    Returns:
        bool: возращает int(в аннотации bool)
    """
    return 1


@strict
def func_to_bool_return_float() -> bool:
    """
    Returns:
        bool: возращает float(в аннотации bool)
    """
    return 1.0


@strict
def func_to_bool_return_str() -> bool:
    """
    Returns:
        bool: возращает str(в аннотации bool)
    """
    return "Hello, world!"


@strict
def func_to_int_return_bool() -> int:
    """
    Returns:
        int: возращает bool(в аннотации int)
    """
    return True


@strict
def func_to_int_return_float() -> int:
    """
    Returns:
        int: возращает float(в аннотации int)
    """
    return 1.0


@strict
def func_to_int_return_str() -> int:
    """
    Returns:
        int: возращает str(в аннотации int)
    """
    return True


@strict
def func_to_float_return_bool() -> float:
    """
    Returns:
        float: возращает bool(в аннотации float)
    """
    return True


@strict
def func_to_float_return_int() -> float:
    """
    Returns:
        float: возращает int(в аннотации float)
    """
    return 1


@strict
def func_to_float_return_str() -> float:
    """
    Returns:
        float: возращает str(в аннотации float)
    """
    return "1.0"


@strict
def func_to_str_return_bool() -> str:
    """
    Returns:
        str: возращает bool(в аннотации str)
    """
    return True


@strict
def func_to_str_return_int() -> str:
    """
    Returns:
        str: возращает int(в аннотации str)
    """
    return 1


@strict
def func_to_str_return_float() -> str:
    """
    Returns:
        str: возращает float(в аннотации str)
    """
    return 1.0


class TestStrictDecorator(unittest.TestCase):
    # Проверка считывания args
    def test_correct_args(self):
        self.assertEqual(sum_two_k_times(3, 2.0, 1.0), 9.0)

    # Проверка считывания kwargs
    def test_correct_kwargs(self):
        self.assertEqual(sum_two_k_times(count=3, a=2.0, b=1.0), 9.0)

    # Проверка смешанное считывания
    def test_correct_mixed(self):
        self.assertAlmostEqual(sum_two_k_times(3, b=2.0, a=1.0), 9.0)

    # bool -> int (args)
    def test_incorrect_bool_to_int_args(self):
        with self.assertRaises(TypeError):
            square_of_int(True)

    # float -> int (args)
    def test_incorrect_float_to_int_args(self):
        with self.assertRaises(TypeError):
            square_of_int(1.0)

    # str -> int (args)
    def test_incorrect_str_to_int_args(self):
        with self.assertRaises(TypeError):
            square_of_int("1")

     # bool -> int (kwargs)
    def test_incorrect_bool_to_int_kwargs(self):
        with self.assertRaises(TypeError):
            square_of_int(num=True)

    # float -> int (kwargs)
    def test_incorrect_float_to_int_kwargs(self):
        with self.assertRaises(TypeError):
            square_of_int(num=1.0)

    # str -> int (kwargs)
    def test_incorrect_str_to_int_kwargs(self):
        with self.assertRaises(TypeError):
            square_of_int(num="1")

    # bool -> float (args)
    def test_incorrect_bool_to_float_args(self):
        with self.assertRaises(TypeError):
            sqrt_of_float(False)

    # int -> float (args)
    def test_incorrect_int_to_float_args(self):
        with self.assertRaises(TypeError):
            sqrt_of_float(1)

    # str -> float (args)
    def test_incorrect_str_to_float_args(self):
        with self.assertRaises(TypeError):
            sqrt_of_float("1.0")

    # bool -> float (kwargs)
    def test_incorrect_bool_to_float_kwargs(self):
        with self.assertRaises(TypeError):
            sqrt_of_float(num=False)

    # int -> float (kwargs)
    def test_incorrect_int_to_float_kwargs(self):
        with self.assertRaises(TypeError):
            sqrt_of_float(num=1)

    # str -> float (kwargs)
    def test_incorrect_str_to_float_kwargs(self):
        with self.assertRaises(TypeError):
            sqrt_of_float(num="1.0")

    # bool -> str (args)
    def test_incorrect_bool_to_str_args(self):
        with self.assertRaises(TypeError):
            upper_str(True)

    # int -> str (args)
    def test_incorrect_int_to_str_args(self):
        with self.assertRaises(TypeError):
            upper_str(12121)

    # float -> str (args)
    def test_incorrect_float_to_str_args(self):
        with self.assertRaises(TypeError):
            upper_str(12121.0)

    # bool -> str (kwargs)
    def test_incorrect_bool_to_str_kwargs(self):
        with self.assertRaises(TypeError):
            upper_str(text=True)

    # int -> str (kwargs)
    def test_incorrect_int_to_str_kwargs(self):
        with self.assertRaises(TypeError):
            upper_str(text=12121)

    # float -> str (kwargs)
    def test_incorrect_float_to_str_kwargs(self):
        with self.assertRaises(TypeError):
            upper_str(text=12121.0)

     # int -> bool (args)
    def test_incorrect_int_to_bool_args(self):
        with self.assertRaises(TypeError):
            num_to_bool(1)

    # float -> bool (args)
    def test_incorrect_float_to_bool_args(self):
        with self.assertRaises(TypeError):
            num_to_bool(1.0)

    # str -> bool (args)
    def test_incorrect_str_to_bool_args(self):
        with self.assertRaises(TypeError):
            num_to_bool("1")

    # int -> bool (kwargs)
    def test_incorrect_int_to_bool_kwargs(self):
        with self.assertRaises(TypeError):
            num_to_bool(value=1)

    # float -> bool (kwargs)
    def test_incorrect_float_to_bool_kwargs(self):
        with self.assertRaises(TypeError):
            num_to_bool(value=1.0)

    # str -> bool (kwargs)
    def test_incorrect_str_to_bool_kwargs(self):
        with self.assertRaises(TypeError):
            num_to_bool(value="1")

    # return int -> bool
    def test_incorrect_return_int_to_bool(self):
        with self.assertRaises(TypeError):
            func_to_bool_return_int()

    # return float -> bool
    def test_incorrect_return_float_to_bool(self):
        with self.assertRaises(TypeError):
            func_to_bool_return_float()

    # return str -> bool
    def test_incorrect_return_str_to_bool(self):
        with self.assertRaises(TypeError):
            func_to_bool_return_str()

    # return bool -> int
    def test_incorrect_return_bool_to_int(self):
        with self.assertRaises(TypeError):
            func_to_int_return_bool()

    # return float -> int
    def test_incorrect_return_float_to_int(self):
        with self.assertRaises(TypeError):
            func_to_int_return_float()

    # return str -> int
    def test_incorrect_return_str_to_int(self):
        with self.assertRaises(TypeError):
            func_to_int_return_str()

    # return bool -> float
    def test_incorrect_return_bool_to_int(self):
        with self.assertRaises(TypeError):
            func_to_float_return_bool()

    # return int -> float
    def test_incorrect_return_int_to_float(self):
        with self.assertRaises(TypeError):
            func_to_float_return_int()

    # return str -> float
    def test_incorrect_return_str_to_float(self):
        with self.assertRaises(TypeError):
            func_to_float_return_str()
    
    # return bool -> float
    def test_incorrect_return_bool_to_str(self):
        with self.assertRaises(TypeError):
            func_to_str_return_bool()

    # return int -> float
    def test_incorrect_return_int_to_str(self):
        with self.assertRaises(TypeError):
            func_to_str_return_int()

    # return str -> float
    def test_incorrect_return_float_to_str(self):
        with self.assertRaises(TypeError):
            func_to_str_return_float()


if __name__ == "__main__":
    unittest.main()
