# Задание № 3: Функция для нахождения абонента по номеру телефона:
def find_by_number(phone_book, number):
    return [lineFromBook for lineFromBook in phone_book if lineFromBook['Телефон'] == int(number)]