"""
1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел
и строк и сохраните в переменные, выведите на экран.
"""

user_str1 = "Это первая переменная. Тип 'СТРОКА'"
user_str2 = 'Это вторая переменная. Тип "Строка"'

print(user_str1)
print(type(user_str1))
print(user_str2)
print(type(user_str2))

user_int1 = 10;
print(user_int1)
print(type(user_int1))

user_float1 = 14.78
print(user_float1)
print(type(user_float1))

user_bool_true = True
print(user_bool_true)
print(type(user_bool_true))

user_bool_false = False
print(user_bool_false)
print(type(user_bool_false))

user_input_str1 = input("Назовите свой город \n>>>")
user_input_num1 = input("Сколько этажей в вашем доме? \n>>>")
user_input_num2 = input("На каком этаже ваша квартира? \n>>>")

all_user_input = f"Вы живете в городе {user_input_str1} в {user_input_num1} этажном доме, на {user_input_num2} этаже."

print(all_user_input)

usr_name = input("Назовите свое имя \n>>>")
usr_scope = input("Кто вы по специальности? \n>>>")

print(f"Вас зовут {usr_name}, ваша специальность {usr_scope} ")