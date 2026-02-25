from book_model import BookModel
from reader_model import ReaderModel

class LibraryService:
    books: list[BookModel]
    readers: list[ReaderModel]

    def __init__(self):
        self.books = []
        self.readers = []

    def allBooks(self):
        return self.books

    def allReaders(self):
        return self.readers

    def findBookByTitle(self, title: str):
        for book in self.books:
            if book.title == title:
                return book
        raise ValueError("Not Found")

    def findReaderByName(self, name: str):
        for reader in self.readers:
            if reader.name == name:
                return reader
        raise ValueError("Not Found")

    def addBook(self, title: str, author: str):
        self.books.append(BookModel(title=title, author=author))

    def deleteBook(self, title: str):
        for index, book in enumerate(self.books):
            if book.title == title:
                del self.books[index]
                return
        raise ValueError("Not Found")

    def addReader(self, name: str):
        self.readers.append(ReaderModel(name=name))

    def borrowBook(self, title: str, readerName: str):
        book = self.findBookByTitle(title=title)
        reader = self.findReaderByName(name=readerName)

        if book.borrowed:
            raise RuntimeError("Already borrowed")

        book.borrowed = True
        book.borrowedBy = reader.name

    def returnBook(self, title: str, readerName: str):
        book = self.findBookByTitle(title=title)
        reader = self.findReaderByName(name=readerName)

        if not book.borrowed:
            raise RuntimeError("Not borrowed")

        if book.borrowedBy != reader.name:
            raise RuntimeError("Borrowed by another reader")

        book.borrowed = False
        book.borrowedBy = None
