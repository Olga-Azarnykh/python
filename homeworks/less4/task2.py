# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.


my_dictsource = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

"""
for itm in range(len(my_dictsource)):
    if my_dictsource[itm] > my_dictsource[itm - 1]:
        print(my_dictsource[itm])
"""

my_poz = [my_dictsource[itm] for itm in range(len(my_dictsource)) if my_dictsource[itm]>my_dictsource[itm-1]]

print(my_poz)