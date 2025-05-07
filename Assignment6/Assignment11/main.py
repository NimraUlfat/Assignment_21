# 11. Class Methods
#Assignment:
#Create a class Book with a class variable total_books.
#Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0  

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def display_total_books(cls):
        print(f"Total books: {cls.total_books}")

# Creating book objects
book1 = Book("Boys over flowers")
book2 = Book("A crash landing on you")
book3 = Book("Vincenzo")

# Display total books
Book.display_total_books()
