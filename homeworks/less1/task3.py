"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""

usr_input = float(input('Введите производьное число \n>>>'))

usr_summa = (usr_input*100+usr_input*10+usr_input)+(usr_input*10+usr_input)+usr_input

print(usr_summa)
