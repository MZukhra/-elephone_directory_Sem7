
# Menu
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#   author Zukhra
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

from datetime import datetime as dt
from time import time

def number_logger(text):
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a', encoding="utf-8") as file:
        file.write('{};phonebook;{}\n'
                   .format(time, text))


# if __name__ == "__logger__":
phone_numbers = {'петров': ['вася', '02', 'милиция'],
                 'иванов': ['Михаил', '03', 'скорая']}
number_logger(phone_numbers)