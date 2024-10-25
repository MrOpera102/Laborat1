# TODO Найдите количество книг, которое можно разместить на дискете
book_information = 4*25*50*100
disk_byte = 1.44*1024*1024
quantity_book = disk_byte // book_information

print("Количество книг, помещающихся на дискету:", int(quantity_book))
