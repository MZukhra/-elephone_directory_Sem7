#Добавление удаление построчно
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#   author Yalushkin Alexey
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
from input_output import phone_numbers
import logger



def add_note():
    surname = input('введите фамилию ')
    if surname in phone_numbers.keys():
        phone_numbers.pop(surname)
    lst = [input('введите имя :'), input('введите номер телефона :'), input('описание :')]
    phone_numbers[surname] = lst
    print(f'{surname} {" ".join(phone_numbers[surname])}')
    logger.number_logger(f"Добавляем контакт: {surname}")
    return phone_numbers

def delete_note():
    surname = input('введите имя для удаления ')
    phone_numbers.pop(surname)
    logger.number_logger(f"Удаляем контакт: {surname}")
    return phone_numbers
