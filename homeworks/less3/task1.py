# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

number_1 = float(input('Введите делимое\n>>>'))
number_2 = float(input('Введите делитель\n>>>'))


def my_division(p_1: float = 12, p_2: float = 6) -> float:
    """Возвращает частное от делнеия, присутствут проверка деления на 0
    :param p_1: делимое (по умоолчанию 12)
    :param p_2: делитель (по умолчанию 6)
    :return: результат деления
    """
    if p_2 != 0:
        return p_1 / p_2
    else:
        print('На 0 делить нельзя!')


print(my_division(number_1, number_2))
