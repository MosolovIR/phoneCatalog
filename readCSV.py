def read_csv(filename): 

    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Должность']

    with open(filename, 'r', encoding = 'utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
        phone_book.append(record)	

    return phone_book