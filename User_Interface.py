# Menu
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#   author Zukhra
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import input_output
import add_delete
import search
import logger


def menu():
    z = input(
        "Введите 1, если хотите найти контакт. \nВведите 2, если хотите отредактировать существующий. \nВведите 3, если хотите добавить новый контакт. \nВведите 4, если хотите удалить контакт. \n")
    
    match z:
        case '1':
            logger.number_logger("Выполняем поиск")
            return search.search()
        case '2':
            logger.number_logger("Редактируем запись")
            return add_delete.add_note()
        case '3':
            return add_delete.add_note()
        case '4':
            return add_delete.delete_note()


