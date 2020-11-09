# 5. Реализовать формирование списка, используя функцию range()
# и возможности генератора. В список должны войти четные числа
# от 100 до 1000 (включая границы). Необходимо получить результат
# вычисления произведения всех элементов списка

from functools import reduce
"""
new_list=[]
for itm in range(1001):
    if not itm&1 and itm>=100:
        new_list.append(itm)
"""

new_list = [itm for itm in range(1001) if not itm&1 and itm >= 100]
print(new_list)

mult_all = reduce(lambda x, y: x * y, new_list)

print(mult_all)

