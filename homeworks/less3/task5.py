# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
# ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
# специальный символ, выполнение программы завершается. Если специальный символ
# введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
# к полученной ранее сумме и после этого завершить программу.

usr_res = 0
usr_exit = False
while not usr_exit:
    usr_str = input('Введите строку чисел разделенных пробелом, для выхода введите "Q" \n>>>')

    i: int = 0
    poz_sp = 0
    # usr_res = 0
    usr_curr = ''
    while i <= len(usr_str):
        try:
            if usr_str[i] == "Q":
                usr_exit = True
                break
            elif usr_str[i] != ' ':
                usr_curr = usr_curr + usr_str[i]
            elif (usr_str[i] == " ") or (i == len(usr_str)):
                print(usr_curr)
                usr_res = usr_res + int(usr_curr)
                usr_curr = ''
        except IndexError:

            print(usr_curr)
            usr_res = usr_res + int(usr_curr)
            break

        i = i + 1

    print(f'Сумма {usr_res}')
