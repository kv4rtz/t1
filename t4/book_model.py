import uuid

class BookModel:
    title: str
    author: str
    borrowed: bool
    borrowedBy: str | None

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.borrowed = False
        self.borrowedBy = None
