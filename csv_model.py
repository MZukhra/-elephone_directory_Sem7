#Добавление csv
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#   author Yalushkin Alexey
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
import csv

def write_file_csv():

    with open('phone_notebook.csv', 'w', encoding="utf-8", newline='') as file:
        fieldnames = ['surname', 'name', 'phone_number', 'comment']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'surname':'Петров', 'name':'Олег', 'phone_number':84645646, 'comment':'Сантехник'})
        writer.writerow({'surname':'Карпов', 'name':'Саша', 'phone_number':85422646, 'comment':'Врач'})
        file.close()

def read_csv():

    with open('phone_notebook.csv', newline='') as file:
        reader = csv.DictReader(file)
    for row in reader:
        print(row)
    file.close()

write_file_csv()
read_csv()
#print(row[surname], row[name], row[phone_number], row[comment])