class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.borrowed = False


class Library:
    def __init__(self):
        self.books = {}  # book_id -> Book

    # Sprint 1
    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise ValueError("Duplicate book ID")
        self.books[book_id] = Book(book_id, title, author)

    # Sprint 2
    def borrow_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book not found")

        book = self.books[book_id]
        if book.borrowed:
            raise ValueError("Book already borrowed")

        book.borrowed = True

    def return_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book not found")

        self.books[book_id].borrowed = False

    # Sprint 3
    def generate_report(self):
        lines = ["BookID | Title | Author | Status"]
        for book in self.books.values():
            status = "Borrowed" if book.borrowed else "Available"
            lines.append(f"{book.book_id} | {book.title} | {book.author} | {status}")
        return "\n".join(lines)
