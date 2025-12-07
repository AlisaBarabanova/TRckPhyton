# TODO Найдите количество книг, которое можно разместить на дискете
disk = 1.44 * 1024 * 1024
pages = 100
lines = 50
chars = 25
bytes = 4

book_size =  pages * lines * bytes * chars
books = int(disk // book_size)

print("Количество книг, помещающихся на дискету:", books)
