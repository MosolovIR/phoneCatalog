# Импортируем функции нашего справочника
from readCSV import read_csv
from writeCSV import write_csv
from showMenu import show_menu
from Task1 import print_result
from Task2 import find_by_lastname
from Task3 import find_by_number
from Task4 import change_number
from Task5 import delete_by_lastname
from Task6 import add_user

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phoneBook.csv')

    while (choice != 7):
        if choice > 7 and choice < 1:
            print('Ошибка ввода команды меню')
            choice = show_menu()
        else:
            if choice == 1: # файл Task1.py
                print_result(phone_book)

            elif choice == 2: # файл Task2.py
                lastName = input('Введите фамилию абонента: ')
                print(find_by_lastname(phone_book, lastName))

            elif choice == 3: # файл Task3.py
                number = input('Введите телефон абонента: ')
                print(find_by_number(phone_book, number))

            elif choice == 4: # файл Task4.py
                lastName = input('Введите фамилию абонента: ')
                firstName = input('Введите имя абонента: ')
                newNumber = input('Введите новый телефон абонента: ')
                print(change_number(phone_book, lastName, firstName, newNumber))
                write_csv('phoneBook.csv', phone_book)

            elif choice == 5: # файл Task6.py
                lastName = input('Введите фамилию абонента: ')
                firstName = input('Введите имя абонента: ')
                number = input('Введите телефон абонента: ')
                jobInfo = input('Введите должность абонента: ')
                add_user(phone_book, lastName, firstName, number, jobInfo)
                write_csv('phoneBook.csv', phone_book)
            
            elif choice == 6: # файл Task5.py
                lastname = input('lastname ')
                print(delete_by_lastname(phone_book, lastname))

        choice = show_menu()
    
    write_csv('phoneBook.csv', phone_book)
    print("\n\nСпасибо что воспользовались нашим справочником!")

work_with_phonebook()
