"""
Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
"""
import os
curr_path = os.path.dirname(os.path.join(os.getenv('PWD'),__file__))
curr_path = curr_path+'/'+'hw_1_5_1.txt'

#очистить файл
with open(curr_path, 'w', encoding='UTF-8') as user_file:
    date_str=''
    user_file.write(date_str)

#Записать несколько строк в файл
with open(curr_path, 'w', encoding='UTF-8') as user_file:
    date_str='Первая строка, \n Вторая строка, \n Третья почти последняя строка, \n Четвертая последняя строка'
    user_file.write(date_str)


#Прочитать файл
with open(curr_path, 'r', encoding='UTF-8') as user_file:
    # подсчитать строки и символы в каждой строке
    count_str = 0
    count_chr=0
    for line in user_file:
        #считаем символы
        count_chr = len(line) - line.count(' ', 0)
        #считаем строки
        count_str = count_str + 1
        print(f'ИЛИ В строке {count_str} {count_chr} символов')
        count_chr = 0

        #print(line)
    print(f' В файле {count_str} строк')