# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

r_list = []
ch = False
i = 0
j = 0
while not ch:
    usr_value = input('Введите значения списка элементов или EXIT для завершения ввода\n>>>')
    r_list.insert(i, usr_value)

    if not (len(r_list) % 2) and r_list[i].upper() != 'EXIT':
        [r_list[j], r_list[j + 1]] = r_list[j + 1], r_list[j]
        j += 2
    elif r_list[i].upper() == 'EXIT':
        r_list.pop()
        break
    i = i + 1
print(r_list)