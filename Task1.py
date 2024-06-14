# Задание № 1: Функция для отображения всего телефонного справочника:
def print_result(phone_book):
    for lineFromBook in phone_book:
        print(f"{lineFromBook['Фамилия']} {lineFromBook['Имя']} {lineFromBook['Телефон']} {lineFromBook['Должность']}")