from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from calendar_service import CalendarService

app = FastAPI()

calendarService = CalendarService()

@app.get("/events")
def getAllEvents():
    return calendarService.allEvents()

@app.get("/events/{title}")
def getEvent(title: str):
    try:
        return calendarService.findEventByTitle(title=title)
    except ValueError:
        raise HTTPException(status_code=404, detail="Event not found")

@app.post("/events/{title}/{when}")
def createEvent(title: str, when: str):
    calendarService.addEvent(title=title, when=when)
    return {"msg": f"Event {title} successfully created"}

@app.patch("/events/{oldTitle}/{newTitle}")
def editEventTitle(oldTitle: str, newTitle: str):
    try:
        calendarService.editEventTitle(oldTitle=oldTitle, newTitle=newTitle)
        return {"msg": f"Event {newTitle} successfully updated"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Event not found")

@app.patch("/events/time/{title}/{newWhen}")
def editEventTime(title: str, newWhen: str):
    try:
        calendarService.editEventTime(title=title, newWhen=newWhen)
        return {"msg": f"Event {title} time successfully updated"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Event not found")

@app.delete("/events/{title}")
def deleteEvent(title: str):
    try:
        calendarService.deleteEvent(title=title)
        return {"msg": f"Event {title} successfully deleted"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Event not found")

@app.get("/notifications/{now}/{windowMinutes}")
def getNotifications(now: str, windowMinutes: int):
    return calendarService.upcomingEvents(now=now, windowMinutes=windowMinutes)
