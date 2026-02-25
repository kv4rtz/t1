import unittest
from fastapi.testclient import TestClient
from fastapi import status
from app import app, votingService

class TestApp(unittest.TestCase):
    client: TestClient

    def setUp(self):
        self.client = TestClient(app=app)
        votingService.polls = []

    def testCreatePoll(self):
        response = self.client.post('/polls/FirstPoll')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"msg": "Poll FirstPoll successfully created"})

    def testVoteLogicAndResults(self):
        self.client.post('/polls/FirstPoll')
        self.client.post('/polls/FirstPoll/options/Yes')
        self.client.post('/polls/FirstPoll/options/No')

        self.client.post('/polls/FirstPoll/vote/Yes')
        self.client.post('/polls/FirstPoll/vote/Yes')
        self.client.post('/polls/FirstPoll/vote/No')

        response = self.client.get('/polls/FirstPoll/results')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"Yes": 2, "No": 1})

    def testDeletePoll(self):
        self.client.post('/polls/FirstPoll')
        response = self.client.delete('/polls/FirstPoll')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"msg": "Poll FirstPoll successfully deleted"})

    def testPollNotFoundException(self):
        response = self.client.get('/polls/Unknown')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json(), {"detail": "Poll not found"})

    def testVoteNotFoundException(self):
        self.client.post('/polls/FirstPoll')
        response = self.client.post('/polls/FirstPoll/vote/UnknownOption')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json(), {"detail": "Poll or option not found"})


if __name__ == '__main__':
    unittest.main()
