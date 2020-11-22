"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30
"""
import os

curr_path = os.path.dirname(os.path.join(os.getenv('PWD'), __file__))
dict_tran = {}


def restr(chr):
    result = False
    figures = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    if figures.count(chr) > 0:
        result = True
    return result


with open(curr_path + '/' + 'list_tranning.txt', 'r', encoding='UTF-8') as lst_tran:
    # print(data_src)
    for line in lst_tran:

        div = line.find(':')
        name_tr = line[:div]

        print(name_tr)
        itx = div

        counttr = 0
        cur_tr = ''
        while itx < len(line):
            cur_chr = line[itx:itx + 1]
            if restr(cur_chr):
                cur_tr = cur_tr + cur_chr
            else:
                if len(cur_tr) > 0:
                    counttr = counttr + int(cur_tr)
                    cur_tr = ''

            itx = itx + 1

        dict_tran[name_tr] = counttr
        # print(counttr)

        print(dict_tran)
