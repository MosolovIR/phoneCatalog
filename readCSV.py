def read_csv(filename): 

    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding = 'utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
		    #dict(((Фамилия, Иванов),(Имя, Иван),(Телефон, 111)))
        phone_book.append(record)	

    return phone_book