size_of_1_char = 4  # в байтах
symbols = 25
lines = 50
pages = 100
book_size = symbols * lines * pages * size_of_1_char

size_diskettes = 1.44 * 1024 * 1024  # в байтах
total_books = size_diskettes // book_size

print(f"Количество книг, помещающихся на дискету: {total_books:.0f}")
