from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from task_service import TaskService

app = FastAPI()

taskService = TaskService()

@app.get("/tasks")
def getAllTasks():
    return taskService.allTasks()

@app.get("/tasks/{name}")
def getTask(name: str):
    try:
        return taskService.findTaskByName(name=name)
    except ValueError:
        raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks/{name}")
def createTasks(name: str):
    taskService.addTask(name=name)

    return {"msg": f"Task {name} successfully created"}

@app.patch("/tasks/complete/{name}")
def completeTask(name: str):
    try:
        taskService.completeTask(name=name)
        return {"msg": f"Task {name} successfully completed"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Task not found")

@app.patch("/tasks/{oldName}/{newName}")
def editTask(oldName: str, newName: str):
    try:
        taskService.editTask(oldName=oldName, newName=newName)
        return {"msg": f"Task {newName} successfully updated"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{name}")
def deleteTask(name: str):
    try:
        taskService.deleteTask(name=name)
        return {"msg": f"Task {name} successfully deleted"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Task not found")

