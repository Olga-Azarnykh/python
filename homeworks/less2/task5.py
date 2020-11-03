# 5. Реализовать структуру «Рейтинг»,
# представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [9, 7, 4, 2, 2, 1, 0]
usr_num = input('Введите натуральное число \n>>>')

if not (usr_num.isdigit()):
    print("Введено не число!")
else:
    usr_num = int(usr_num)
    val_count = my_list.count(usr_num)
    idx = 0
    while idx <= len(my_list):
        if val_count >= 1:
            cur_poz = my_list.index(usr_num, idx)
            my_list.insert(cur_poz+1, usr_num)
            break
        else:
            my_list.insert(0, usr_num)
            break
print(my_list)
