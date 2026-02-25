import unittest
from fastapi.testclient import TestClient
from fastapi import status
from app import app, calendarService
from event_model import EventModel

class TestApp(unittest.TestCase):
    client: TestClient

    def setUp(self):
        self.client = TestClient(app=app)
        calendarService.events = []

    def testCreateEvent(self):
        response = self.client.post('/events/FirstEvent/2026-01-01T10:00:00')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"msg": "Event FirstEvent successfully created"})

    def testEditEventTitle(self):
        self.client.post('/events/FirstEvent/2026-01-01T10:00:00')
        response = self.client.patch('/events/FirstEvent/EditedEvent')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"msg": "Event EditedEvent successfully updated"})

    def testEditEventTime(self):
        self.client.post('/events/FirstEvent/2026-01-01T10:00:00')
        response = self.client.patch('/events/time/FirstEvent/2026-01-01T11:30:00')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"msg": "Event FirstEvent time successfully updated"})

    def testDeleteEvent(self):
        self.client.post('/events/FirstEvent/2026-01-01T10:00:00')
        response = self.client.delete('/events/FirstEvent')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {"msg": "Event FirstEvent successfully deleted"})

    def testGetEvent(self):
        self.client.post('/events/FirstEvent/2026-01-01T10:00:00')
        response = self.client.get('/events/FirstEvent')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), EventModel("FirstEvent", "2026-01-01T10:00:00").__dict__)

    def testEventNotFoundException(self):
        response = self.client.get('/events/UnknownEvent')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json(), {"detail": "Event not found"})

    def testNotificationsUpcoming(self):
        self.client.post('/events/FirstEvent/2026-01-01T10:10:00')
        self.client.post('/events/SecondEvent/2026-01-01T12:00:00')

        response = self.client.get('/notifications/2026-01-01T10:00:00/30')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [EventModel("FirstEvent", "2026-01-01T10:10:00").__dict__])

    def testNotificationsNoUpcoming(self):
        self.client.post('/events/FirstEvent/2026-01-01T09:00:00')
        self.client.post('/events/SecondEvent/2026-01-01T12:00:00')

        response = self.client.get('/notifications/2026-01-01T10:00:00/30')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [])


if __name__ == '__main__':
    unittest.main()
