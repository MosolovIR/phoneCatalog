# Задание № 5: Функция для удаления записи в телефонном справочнике по фамилии:
def delete_by_lastname(phone_book, lastname):
    deleteCount = 0
    
    for lineFromBook in phone_book:
        if lineFromBook['Фамилия'] == lastname:
            phone_book.remove(lineFromBook)
            deleteCount += 1
            print(f"Удалено записей: {deleteCount}")
            
    return phone_book
