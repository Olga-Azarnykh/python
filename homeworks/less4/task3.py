# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
#Подсказка: использовать функцию range() и генератор.

"""
for itm in range(240):
    if (itm>=20) and (not(itm%20) or not(itm%21)):
        print(itm)
"""

my_dict = [itm for itm in range(240) if (itm >= 20) and (not (itm % 20) or not (itm % 21))]

print(my_dict)
