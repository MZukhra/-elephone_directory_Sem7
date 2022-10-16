#Добавление удаление построчно
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#   author Yalushkin Alexey
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
from input_output import phone_numbers


def add_note():
    s = ''
    surname = input('введите фамилию ')
    lst = [input('введите имя :'), input('введите номер телефона :'), input('описание :')]
    phone_numbers[surname] = lst
    print(f'{surname} {s.join(phone_numbers[surname])}')
    return phone_numbers
def delete_note(phone_numbers):
    surname = input('введите имя для удаления ')
    phone_numbers.pop(surname)
    return phone_numbers
