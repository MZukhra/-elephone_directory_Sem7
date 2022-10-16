
# Добавление поиска
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#   author Victoria Burakhina
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


from input_output import phone_numbers
import User_Interface


def search():

    surname = input('введите фамилию ')
    if phone_numbers.keys().__contains__(surname):
        print(f'{surname} {" ".join(phone_numbers[surname])}')
    else:
        print('Данных нет в списке')

        print('Выход в общее меню')

        User_Interface.menu()