# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

usr_value = input('Введите месяц в виде целого числа от 1 до 12\n>>>')

my_dict = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь",
           7: "Июль", 8: "Август", 9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}

usr_value = int(usr_value)
if (usr_value < 3) or (usr_value == 12):
    print(my_dict[usr_value] + ' -> ' + 'Зима')
elif (usr_value >= 3) and (usr_value <= 5):
    print(my_dict[usr_value] + ' -> ' + 'Весна')
elif (usr_value >= 6) and (usr_value <= 8):
    print(my_dict[usr_value] + ' -> ' + 'Лето')
elif (usr_value >= 9) and (usr_value <= 11):
    print(my_dict[usr_value] + ' -> ' + 'Осень')

"""
# Реализация через список
i = False
while i == False:
    usr_inp=input('Введите номер месяца \n>>')
    if not(usr_inp.isdigit()) or int(usr_inp)>12:
        print('Введите число от 1 до 12')
    else:
        i = True

usr_inp = int(usr_inp)

if (usr_inp < 3) or (usr_inp == 12):
    print('Зима')
elif usr_inp >= 3 and usr_inp <= 5:
    print('Весна')
elif usr_inp >= 6 and usr_inp <= 8:
    print('Лето')
elif usr_inp >= 9 and usr_inp <= 11:
    print('Осень')
"""