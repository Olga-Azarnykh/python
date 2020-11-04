# 3. Реализовать функцию my_func(), которая принимает три
# позиционных аргумента, и возвращает сумму наибольших двух аргументов.

num_1 = int(input('Введите число 1\n>>>'))
num_2 = int(input('Введите число 2\n>>>'))
num_3 = int(input('Введите число 3\n>>>'))


def my_func_max(a: int, b: int, c: int):
    """Функция, которая находит максимум из трех чисел
    :param a: число1
    :param b: число2
    :param c: число2
    :return: max
    """
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    else:
        return c


def my_func(a: int, b: int, c: int):
    """ Функция, которая находит максимальную сумму двух чисел
    """
    return my_func_max(a + b, b + c, c + a)


print(my_func(num_1, num_2, num_3))

"""
def usr_max(arg1,arg2,arg3):
    usr_args = [usr_arg1, usr_arg2, usr_arg3]
    usr_args.sort()
    return usr_args[2]+usr_args[1]

while True:
  
    usr_arg1 = input('Введите первый аргумент /n>>>')
    usr_arg2 = input('Введите второй аргумент /n>>>')
    usr_arg3 = input('Введите третий аргумент /n>>>')

    try:
        usr_arg1 = int(usr_arg1)
        usr_arg2 = int(usr_arg2)
        usr_arg3 = int(usr_arg3)
        usr_summ = usr_max(usr_arg1,usr_arg2,usr_arg3)
        print(f'Сумма двух наибольших аргументов = {usr_summ}')
        break
    except ValueError:
        print('Введите числовые значения')
 """
