from task_model import TaskModel

class TaskService:
    tasks: list[TaskModel]

    def __init__(self):
        self.tasks = []

    def allTasks(self):
        return self.tasks

    def findTaskByName(self, name: str):
        for task in self.tasks:
            if task.name == name:
                return task
        raise ValueError("Not Found")
        

    def addTask(self, name: str):
        self.tasks.append(TaskModel(name))

    def editTask(self, oldName: str, newName: str):
        for task in self.tasks:
            if task.name == oldName:
                task.name = newName
                return
        raise ValueError("Not Found")
    
    def completeTask(self, name: str):
        for task in self.tasks:
            if task.name == name:
                task.completed = True
                return
        raise ValueError("Not Found")
    
    def deleteTask(self, name: str):
        for index, task in enumerate(self.tasks):
            if task.name == name:
                del self.tasks[index]
                return
        raise ValueError("Not Found")
