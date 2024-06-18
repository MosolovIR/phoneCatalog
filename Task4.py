# Задание № 4: Функция для изменения данных (на примере номера телефона):
def change_number(phone_book, lastName, firstName, newNumber):
    for lineFromBook in phone_book:
        if lineFromBook['Фамилия'] == lastName and lineFromBook['Имя'] == firstName:
            lineFromBook['Телефон'] = newNumber
    return phone_book