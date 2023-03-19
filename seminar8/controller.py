from func import *
from view import *

while True:
    op = choice()
    if op == 1:
        print(show_all())
    elif op == 2:
        find_str = get_search()
        search(find_str)
    elif op == 3:
        user = get_user()
        add_contact(user)
    elif op == 4:
        del_data()
    elif op == 5:
        change_data()
    elif op == 6:
        break
    else:
        print('error')


