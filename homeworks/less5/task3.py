"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

import os

curr_path = os.path.dirname(os.path.join(os.getenv('PWD'), __file__))
curr_path = curr_path + '/' + 'hw_1_5_2.txt'

# очистить файл
with open(curr_path, 'w', encoding='UTF-8') as user_file:
    date_str = ''
    user_file.write(date_str)

emp_list = dict(Иванов='15000', Петров='19500', Сидоров='22000')
# Записать сотрудников в файл
with open(curr_path, 'w', encoding='UTF-8') as user_file:
    for itx in emp_list:
        date_str = itx + ' ' + emp_list[itx] + '\n'
        # print(date_str)
        user_file.write(date_str)

with open(curr_path, 'r', encoding='UTF-8') as user_file:
    print('Зарплата менее 20000 :')
    summa = 0
    count_emp = 0
    for line in user_file:
        div = line.find(' ')
        pay_emp = line[div + 1:]
        pay_emp = int(pay_emp)
        if pay_emp < 20000:
            print(line[0:div])
            summa = summa + pay_emp
            count_emp = count_emp + 1
    print(f'Средняя величина дохода составляет {summa / count_emp}')
