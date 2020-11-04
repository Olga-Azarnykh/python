# 6. Реализовать функцию int_func(), принимающую слово из маленьких
# латинских букв и возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text

def my_func(user_curr):
    first_chr = user_curr[0:1]
    result = first_chr.upper() + user_curr[1:]
    return result


usr_res = 0
usr_exit = False
while not usr_exit:
    usr_str = input('Введите строку слов разделенных пробелом, для выхода введите "Q" \n>>>')
    usr_outstr = ''
    i = 0
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
                # usr_curr = usr_curr + usr_str[itx]
                print(usr_curr)
                usr_curr = my_func(usr_curr)
                if len(usr_outstr) > 0:
                    usr_outstr = usr_outstr + ' ' + usr_curr
                else:
                    usr_outstr = usr_outstr + usr_curr
                # usr_res = usr_res + int(usr_curr)
                usr_curr = ''
        except IndexError:
            # print('ex')
            print(usr_curr)
            usr_curr = my_func(usr_curr)
            usr_outstr = usr_outstr + ' ' + usr_curr
            # usr_res = usr_res + int(usr_curr)
            break
        i = i + 1

    print(usr_outstr)