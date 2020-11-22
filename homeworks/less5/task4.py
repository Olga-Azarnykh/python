"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

import os

curr_path = os.path.dirname(os.path.join(os.getenv('PWD'), __file__))
# curr_path = curr_path+'/'+'hw_1_5.txt'

# def ru_num(my_numeral,my_string):
#    with open(curr_path+'/'+'ru_numeral.txt', 'w', encoding='UTF-8') as ru_file:

ru_numeral = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре'}
ru_list = {}

itx = 0
with open(curr_path + '/' + 'en_numeral.txt', 'r', encoding='UTF-8') as en_file:
    for line in en_file:
        div = line.find('—')
        numeral = line[div + 1:]
        numeral = numeral.strip()
        if len(numeral) > 1:
            numeral = numeral[len(numeral) - 2]
        ru_list[numeral] = ru_numeral[numeral]
        print(ru_list[numeral])

print(ru_list)

with open(curr_path + '/' + 'ru_numeral.txt', 'w', encoding='UTF-8') as ru_file:
    for itx in ru_list:
        data_str = ru_list[itx] + ' — ' + itx + ' \n'
        print(data_str)
        ru_file.write(data_str)
