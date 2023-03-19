def show_all():
    with open('data.txt', 'r', encoding='UTF-8') as file:
        content = file.read()
        return content


def add_contact(user):
    with open('data.txt', 'a', encoding='UTF-8') as file:
        file.write(user)

def error():
    print('error')

def search(data_str):

    with open('data.txt', 'r', encoding='UTF-8') as file:
        count = True
        lst_str = file.readlines()
        for worker in lst_str:
            if data_str in worker:
                print(worker)
                count = False
        if count:
            print('\nТакого пользователя нет.\n')

def change_contact(data_str):
    with open('data.txt', 'r', encoding='UTF-8') as f1:
        lines = f1.readlines()

        for worker in lines:
            worker = worker.strip()
            if data_str in worker:
                f1.write(input()+'\n')


