"""
 Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
 Об окончании ввода данных свидетельствует пустая строка.
"""

print('Вариант 1')
file = open('hw_1_5_1.txt','w',encoding = 'UTF-8')  #открываем на запись
my_endinp = False
while not my_endinp:
    scrstr = input('введите строку, для выхода нажмите ENTER \n>>')
    if len(scrstr) == 0:
        break
    scrstr = scrstr+'\n'
    file.write(scrstr)

file.close()

print('Вариант 2')
date_str=''
my_endinp = False
while not my_endinp:
    scrstr = input('введите строку, для выхода нажмите ENTER \n>>')
    if len(scrstr) == 0:
        break
    date_str = date_str+scrstr+'\n'

with open('hw_1_5_2.txt', 'w', encoding='UTF-8') as user_file:
    user_file.write(date_str)