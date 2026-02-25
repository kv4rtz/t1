import unittest
from fastapi.testclient import TestClient
from fastapi import status
from app import app, blogService

class TestApp(unittest.TestCase):
    client: TestClient

    def setUp(self):
        self.client = TestClient(app=app)
        blogService.posts = []

    def testCreatePost(self):
        response = self.client.post('/posts/FirstPost/Hello')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"msg": "Post FirstPost successfully created"})

    def testEditPost(self):
        self.client.post('/posts/FirstPost/Hello')
        response = self.client.patch('/posts/FirstPost/EditedPost')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"msg": "Post EditedPost successfully updated"})

    def testDeletePost(self):
        self.client.post('/posts/FirstPost/Hello')
        response = self.client.delete('/posts/FirstPost')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"msg": "Post FirstPost successfully deleted"})

    def testCreateComment(self):
        self.client.post('/posts/FirstPost/Hello')
        response = self.client.post('/posts/FirstPost/comments/FirstComment')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        body = response.json()
        self.assertEqual(body["msg"], "Comment successfully created")
        self.assertTrue(len(body["commentId"]) > 0)

    def testEditComment(self):
        self.client.post('/posts/FirstPost/Hello')
        create = self.client.post('/posts/FirstPost/comments/FirstComment')
        commentId = create.json()["commentId"]

        response = self.client.patch(f'/posts/FirstPost/comments/{commentId}/EditedComment')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"msg": f"Comment {commentId} successfully updated"})

    def testDeleteComment(self):
        self.client.post('/posts/FirstPost/Hello')
        create = self.client.post('/posts/FirstPost/comments/FirstComment')
        commentId = create.json()["commentId"]

        response = self.client.delete(f'/posts/FirstPost/comments/{commentId}')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"msg": f"Comment {commentId} successfully deleted"})

    def testPostNotFoundException(self):
        response = self.client.get('/posts/UnknownPost')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json(), {"detail": "Post not found"})

    def testCommentNotFoundException(self):
        self.client.post('/posts/FirstPost/Hello')
        response = self.client.patch('/posts/FirstPost/comments/unknown/Edited')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json(), {"detail": "Comment not found"})


if __name__ == '__main__':
    unittest.main()
