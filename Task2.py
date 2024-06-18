# Задание № 2: Функция для нахождения абонента по фамилии:
def find_by_lastname(phone_book, lastName):
    return [lineFromBook for lineFromBook in phone_book if lineFromBook['Фамилия'] == lastName]