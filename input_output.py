#Добавление удаление построчно
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#   author Yalushkin Alexey
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


#ToDo  расписать ф-ии чтения и записи файла, и вывода в терминал всего справочника


def get_name(phone_numbers, surname):
    if surname in phone_numbers:
        return phone_numbers[surname]
    else:
        return print(f'{surname} not in phone numbers')

def input_surname():
    surname = str(input('введите фамилию - '))
    return surname

def write_file():
    pass

def read_file():
    pass

def view_all():
    pass