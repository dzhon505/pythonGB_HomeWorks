def choice():
    op = int(input('Выберете что вы хотите сделать:\n1 - Посмотреть все\n2 - Поиск контакта\n3 - Добавить контакт\n4 - Удалить контакт'
                           '\n5 - Изменить контакт\n6 - Выход\n'))
    return op

def get_user():
    name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    phone = input('Введите телефон: ')
    data_str = name + ' ' + last_name + ' ' + phone + '\n'
    return data_str

def get_search():
    data_str = input('Поиск: ')
    return data_str

def change_data():
    data_str = input('Введите искомую строку: ')
    user_lst = []
    with open('data.txt', 'r', encoding='UTF-8') as file:
        lst = file.readlines()
        for line in lst:
            if data_str in line:
                user_lst.append(line)
    print(*user_lst)
    answer = int(input('Введите номер строки которую надо изменить: '))
    print('Введите новую строку')
    new_str = get_user()
    with open('data.txt', 'w', encoding='UTF-8') as file:
        for line in lst:
            if user_lst[answer - 1] != line:
                file.write(line)
            else:
                file.write(new_str)

    print('Done!')

def del_data():
    data_str = input('Введите искомую строку: ')
    user_lst = []
    with open('data.txt', 'r', encoding='UTF-8') as file:
        lst = file.readlines()
        for line in lst:
            if data_str in line:
                user_lst.append(line)
    print(*user_lst)
    answer = int(input('Введите номер строки которую надо удалить: '))
    with open('data.txt', 'w', encoding='UTF-8') as file:
        for line in lst:
            if user_lst[answer - 1] != line:
                file.write(line)
            else:
                continue

    print('Done!')