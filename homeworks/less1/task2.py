"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

inp_seconds = input("Введите время в секундах \n>>>")

#вычислим секунды
my_seconds = int(inp_seconds)%60
if my_seconds<10:
    usr_seconds = "0"+str(my_seconds)
else:
    usr_seconds = str(my_seconds)

#сколько минут во ввденом числе
usr_minute = int(inp_seconds)//60

if usr_minute<60:
    usr_time = '00:'+str(usr_minute)+":"+usr_seconds
else:

    if usr_minute%60>=10:
        usr_time = str(usr_minute//60)+":"+str(int(usr_minute%60))+":"+usr_seconds
    else:
        usr_time = str(usr_minute//60) + ":0" + str(int(usr_minute % 60)) + ":" + usr_seconds

print(usr_time)