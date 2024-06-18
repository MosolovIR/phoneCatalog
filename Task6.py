# Задание № 6: Функция для добавления новой записи в телефонный справочник:
def add_user(phone_book, lastName, firstName, number, jobInfo):
    newLine = {
        'Фамилия': lastName,
        'Имя': firstName,
        'Телефон': number,
        'Должность': jobInfo
    }
    phone_book.append(newLine)
    print("Новая запись добавлена в телефонный справочник.")
    return phone_book
