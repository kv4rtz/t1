import unittest
from fastapi.testclient import TestClient
from fastapi import status
from app import app, libraryService

class TestApp(unittest.TestCase):
    client: TestClient

    def setUp(self):
        self.client = TestClient(app=app)
        libraryService.books = []
        libraryService.readers = []

    def testAddBook(self):
        response = self.client.post('/books/FirstBook/FirstAuthor')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"msg": "Book FirstBook successfully created"})

    def testDeleteBook(self):
        self.client.post('/books/FirstBook/FirstAuthor')
        response = self.client.delete('/books/FirstBook')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"msg": "Book FirstBook successfully deleted"})

    def testBorrowBook(self):
        self.client.post('/books/FirstBook/FirstAuthor')
        self.client.post('/readers/FirstReader')

        response = self.client.post('/borrow/FirstBook/FirstReader')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"msg": "Book FirstBook successfully borrowed by FirstReader"})

    def testReturnBook(self):
        self.client.post('/books/FirstBook/FirstAuthor')
        self.client.post('/readers/FirstReader')
        self.client.post('/borrow/FirstBook/FirstReader')

        response = self.client.post('/return/FirstBook/FirstReader')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"msg": "Book FirstBook successfully returned by FirstReader"})

    def testBookNotFoundException(self):
        response = self.client.get('/books/UnknownBook')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json(), {"detail": "Book not found"})

    def testBorrowNotFoundException(self):
        self.client.post('/books/FirstBook/FirstAuthor')

        response = self.client.post('/borrow/FirstBook/UnknownReader')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json(), {"detail": "Book or reader not found"})

    def testBorrowAlreadyBorrowedException(self):
        self.client.post('/books/FirstBook/FirstAuthor')
        self.client.post('/readers/FirstReader')
        self.client.post('/borrow/FirstBook/FirstReader')

        response = self.client.post('/borrow/FirstBook/FirstReader')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {"detail": "Book already borrowed"})

    def testReturnNotBorrowedException(self):
        self.client.post('/books/FirstBook/FirstAuthor')
        self.client.post('/readers/FirstReader')

        response = self.client.post('/return/FirstBook/FirstReader')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {"detail": "Book is not borrowed"})

    def testReturnBorrowedByAnotherReaderException(self):
        self.client.post('/books/FirstBook/FirstAuthor')
        self.client.post('/readers/FirstReader')
        self.client.post('/readers/SecondReader')
        self.client.post('/borrow/FirstBook/FirstReader')

        response = self.client.post('/return/FirstBook/SecondReader')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {"detail": "Book is borrowed by another reader"})


if __name__ == '__main__':
    unittest.main()
