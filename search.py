
# Виктория Бурахина
# добавлен модуль search



from input_output import phone_numbers
import user_interface

def search(surname, phone_numbers):

     if phone_numbers.keys().__contains__(surname):
         print(f'{surname} {" ".join(phone_numbers[surname])}')
     else:

        print('Данных нет в списке')

        print('Выход в общее меню')
    user_interface.menu()





