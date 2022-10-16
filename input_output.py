# Alexandr Ulitin
# Input_Outpunt

phone_numbers = {'петров': ['вася', '02', 'милиция'], 'иванов': ['Михаил', '03', 'скорая']}

# Ввод имени
def input_name(): 
    name = input("Введите ваше имя: ") 
    remfname = name[1:] 
    firstchar = name[0] 
    return firstchar.upper() + remfname 
 
# Ввод Фамилии 
def input_fameli(): 
    surname = input("Введите вашу фамилию: ") 
    remlname = surname[1:] 
    firstchar = surname[0] 
    return firstchar.upper() + remlname
