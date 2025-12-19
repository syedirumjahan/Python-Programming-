class Book:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append((title, author))
        print("Book added successfully")

    def drop_book(self, title):
        for book in self.books:
            if book[0] == title:
                self.books.remove(book)
                print("Book removed successfully")
                return
        print("Book not found")

    def display_books(self):
        if not self.books:
            print("No books available")
        else:
            for title, author in self.books:
                print("Title:", title, "| Author:", author)

# Example usage
b = Book()
b.add_book("Python Basics", "Guido")
b.add_book("AI Fundamentals", "Andrew")
b.display_books()
b.drop_book("Python Basics")
b.display_books()
