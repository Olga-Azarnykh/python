# 6. Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# my_list = [(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#          (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#         (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})]

idx = 0
usr_list = []
while idx <= 2:

    usr_nom = {
        "name": "Наименование \n>>>",
        "price": "Цена \n>>>",
        "value": "Количество \n>>>",
        "unit": "Ед.изм \n>>>"
    }
    usr_book = {}
    for key, value in usr_nom.items():
        usr_book[key] = input(value)

    cur_tuple = (idx, usr_book)
    usr_list.append(cur_tuple)
    idx = idx + 1

lst_name = []
lst_price = []
lst_value = []
lst_unit = []

usr_price = {"name": lst_name, "price": lst_price, "value": lst_value, "unit": lst_unit}

idx = 0
while idx < len(usr_list):
    cur_dict = usr_list[idx][1]

    for key, value in cur_dict.items():
        value = cur_dict[key]
        if key == "name":
            lst_name.append(cur_dict[key])
        elif key == "price":
            lst_price.append(cur_dict[key])
        elif key == "value":
            lst_value.append(cur_dict[key])
        else:
            lst_unit.append(cur_dict[key])
    idx = idx + 1
print(usr_price)
