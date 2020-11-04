# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def my_func(x, y):
    """ Возведение числа x в степень y
    """
    usr_deg = y * (-1)
    result = x ** usr_deg
    if usr_deg % 2:
        result = result * (-1)
    print('Возведение числа x в степень y')
    return result


def my_func_two(x, y):
    """ Возведение числа x в степень y (цикл)
    """
    usr_deg = y * (-1)
    result = x
    i = 1
    while True:
        result = result * x
        i = i + 1
        if i == usr_deg:
            break
    if usr_deg % 2:
        result = result * (-1)
    print('Возведение числа x в степень y (цикл)')
    return result


print(my_func(3, -3))
print(my_func_two(3, -3))
