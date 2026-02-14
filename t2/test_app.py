import unittest
import json
from fastapi.testclient import TestClient
from app import app
from fastapi import status
from task_model import TaskModel

class TestApp(unittest.TestCase):
    client: TestClient

    def setUp(self):
        self.client = TestClient(app=app)

    def testCreateTask(self):
        response = self.client.post('/tasks/FirstTestTask')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"msg": "Task FirstTestTask successfully created"})

    def testEditTask(self):
        response = self.client.patch('/tasks/FirstTestTask/EditedFirstTestTask')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"msg": "Task EditedFirstTestTask successfully updated"})

    def testCompleteTask(self):
        response = self.client.post('/tasks/FirstTestTask')
        response = self.client.patch('/tasks/complete/FirstTestTask')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"msg": "Task FirstTestTask successfully completed"})

    def testFindTaskByName(self):
        response = self.client.get('/tasks/FirstTestTask')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), TaskModel("FirstTestTask").__dict__)

    def testDeleteTask(self):
        response = self.client.post('/tasks/FirstTestTask')
        response = self.client.delete('/tasks/FirstTestTask')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"msg": "Task FirstTestTask successfully deleted"})

    def testNotFoundException(self):
        response = self.client.get('/tasks/FirstTestTask123')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json(), {"detail": "Task not found"})
        


if __name__ == '__main__':
    unittest.main()
