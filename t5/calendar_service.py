from datetime import datetime, timedelta
from event_model import EventModel

class CalendarService:
    events: list[EventModel]

    def __init__(self):
        self.events = []

    def allEvents(self):
        return self.events

    def findEventByTitle(self, title: str):
        for event in self.events:
            if event.title == title:
                return event
        raise ValueError("Not Found")

    def addEvent(self, title: str, when: str):
        self.events.append(EventModel(title=title, when=when))

    def editEventTitle(self, oldTitle: str, newTitle: str):
        event = self.findEventByTitle(title=oldTitle)
        event.title = newTitle

    def editEventTime(self, title: str, newWhen: str):
        event = self.findEventByTitle(title=title)
        event.when = newWhen

    def deleteEvent(self, title: str):
        for index, event in enumerate(self.events):
            if event.title == title:
                del self.events[index]
                return
        raise ValueError("Not Found")

    def upcomingEvents(self, now: str, windowMinutes: int):
        nowDt = datetime.fromisoformat(now)
        windowEnd = nowDt + timedelta(minutes=windowMinutes)

        result: list[EventModel] = []
        for event in self.events:
            eventDt = datetime.fromisoformat(event.when)
            if nowDt <= eventDt <= windowEnd:
                result.append(event)
        return result
