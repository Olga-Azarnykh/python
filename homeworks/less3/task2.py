# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

data_name = str(input('Введите имя\n>>>'))
data_surname = str(input('Введите фамилию\n>>>'))
data_birthday = str(input('Введите день рождения\n>>>'))
data_city = str(input('Введите город проживания\n>>>'))
data_email = str(input('Введите email\n>>>'))
data_tel = str(input('Введите tel\n>>>'))


def user_data(name, surname, birthday, city, email, tel):
    """Функция собирает данные пользователя
    :param name: Имя
    :param surname: Фамилия
    :param birthday: Дата рождения
    :param city: Город проживания
    :param email: Эл. почта
    :param tel: Телефон
    :return: Выводит данные о пользователе одной строкой
    """
    return f'UserData: имя - {name}, фамилия - {surname}, день рождения - {birthday},' \
           f' город проживания - {city}, email: {email}, тел: {tel}'

"""
user = {
    'name': 'Olga',
    'surname': 'Azarnykh',
    'birthday': '14.09.1983',
    'city': 'Voronehz',
    'email': 'xshadowx2@ya.ru',
    'tel': '+7(999) 999 99 99'
}

print(user_data(**user))
"""
print(user_data(data_name, data_surname, data_birthday, data_city, data_email, data_tel))
