"""
5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
"""
from homeworks.less8.task4 import Warehouse, Off_equp

result = []
whouse = Warehouse('')


def receipt():
    usrсh = False
    while usrсh == False:
        usr_whouse = input('Укажите склад, для окончания ввода введите Quit \n>> ')

        if usr_whouse == 'Quit':
            return 'break'

        usr_goods = input('Укажите товар >> ')
        usr_brand = input('Введите производителя >> ')
        usr_value = input('Введите количество >> ')

        if usr_goods == 'Printer':
            usr_colorval = input('Введите кол-во цветов >> ')

        elif usr_goods == 'Scanner':
            usr_hendle = input('Это ручной сканер или дикий >> ?')

        elif usr_goods == 'Copy_Equp':
            usr_auto = input('Подача авто? >> ')

        usr_delivery = Off_equp.delivery_good(usr_whouse, usr_goods, usr_brand, usr_value)
        print(usr_delivery)
        result.append(usr_delivery)


receipt()
print(result)
