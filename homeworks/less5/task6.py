"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import os
import json

curr_path = os.path.dirname(os.path.join(os.getenv('PWD'), __file__))
dict_profit = {}
average_profit = {}

with open(curr_path + '/' + 'list_firme.txt', 'r', encoding='UTF-8') as lst_firme:
    for line in lst_firme:

        stpoz = 0
        myiter = 0
        itx=0
        while itx <= 4:
            div = line.find(' ', stpoz+1)
            if myiter == 0: #Наименование
                fname = line[stpoz:div]
                stpoz = div
                myiter = myiter+1
            elif myiter == 1: #Форма собственности
                stpoz = div
                myiter = myiter + 1
            elif myiter == 2:   #Выручка
                fpay = line[stpoz:div]
                stpoz = div
                myiter = myiter+1
            elif myiter == 3:   #Издержки
                fcost = line[stpoz:div]
                #print(f'{fname} {fpay} {fcost}')
                sprofit = int(fpay) - int(fcost)
                if(sprofit > 0):
                    dict_profit[fname] = sprofit
                else:
                    average_profit[fname] = sprofit
                    #dict_profit[fname] = average_profit
                fname = ""
                stpoz = 0
                myiter = 0
            itx = itx+1

    #print(dict_profit)
    #print(average_profit)

    #Собранные словари объединяем для создания json
    dict_res = []
    dict_res.append(dict_profit)
    dict_res.append(average_profit)
    js_dcprofit = json.dumps(dict_res)
    print(js_dcprofit)
