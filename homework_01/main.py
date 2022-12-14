"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num ** 2 for num in numbers]



# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_odd(num):
    """
    функция, определяющая принадлежность числа к нечетным числам
    """
    if num % 2 != 0:
        return True


def is_even(num):
    """
    функция, определяющая принадлежность числа к четным числам
    """
    if num % 2 == 0:
        return True


def is_prime(num):
    """
    функция, определяющая принадлежность числа к простым числам
    """
    counter = 0
    for i in range(2, num + 1):
        if num % i == 0:
            counter += 1
    if counter == 1:
        return True


def filter_numbers(numbers, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return list(filter(is_odd, numbers))
    elif filter_type == EVEN:
        return list(filter(is_even, numbers))
    elif filter_type == PRIME:
        return list(filter(is_prime, numbers))