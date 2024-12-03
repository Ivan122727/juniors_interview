import unittest

from solution_v2 import strict


@strict
def sum_two_n_times(count: int, a: float, b: float) -> float:
    """Сумма двух чисел n раз

    Args:
        count (int): количество раз
        a (float): первое число
        b (float): второе число

    Returns:
        return (float): результат
    """
    res = 0.0
    for i in range(count):
        res += (a + b)
    return res


@strict
def incorrect_str_from_int(num_to_str: int) -> str:
    """Неверный перевод числа в строку 

    Args:
        num_to_str (int): число для перевода

    Returns:
        return (str): результат с ошибкой int -> str
    """
    return num_to_str


@strict
def correct_str_from_int(num_to_str: int) -> str:
    """Перевод числа в строку

    Args:
        num_to_str (int): число для перевода

    Returns:
        return (str): результат str
    """
    return str(num_to_str)


class TestStrictDecorator(unittest.TestCase):
    # Корректные args
    def test_correct_args(self):
        self.assertEqual(sum_two_n_times(3, 2.0, 1.0), 9.0)
    
    # Корректные kwargs
    def test_correct_kwargs(self):
        self.assertEqual(sum_two_n_times(count=3, a=2.0, b=1.0), 9.0)
    
    # Корректные смешанные 
    def test_correct_mixed(self):
        self.assertAlmostEqual(sum_two_n_times(3, b=2.0, a=1.0), 9.0)

    # bool -> int
    def test_incorrect_args_1(self):
        with self.assertRaises(TypeError):
            sum_two_n_times(True, 2.0, 1.0)

    # float -> int
    def test_incorrect_args_2(self):
        with self.assertRaises(TypeError):
            sum_two_n_times(1.0, 2.0, 3.0)

    # str -> int
    def test_incorrect_kwargs_1(self):
        with self.assertRaises(TypeError):
            sum_two_n_times(count="1", b=2.0, a=3.0)
    
    # bool -> float
    def test_incorrect_kwargs_2(self):
        with self.assertRaises(TypeError):
            sum_two_n_times(count=1, a=True, b=3.0)

    # int -> float
    def test_incorrect_mixed_1(self):
        with self.assertRaises(TypeError):
            sum_two_n_times(1, b=2, a=3.0)

    # str -> float
    def test_incorrect_mixed_2(self):
        with self.assertRaises(TypeError):
            sum_two_n_times(1.0, a="2.0", b=3.0)

    # return str
    def test_correct_return(self):
        self.assertEqual(correct_str_from_int(121), "121")
    
    # return int -> str
    def test_incorrect_return(self):
        with self.assertRaises(TypeError):
            incorrect_str_from_int(121)


if __name__ == "__main__":
    unittest.main()
