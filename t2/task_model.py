import uuid

class TaskModel:
    name: str
    completed: bool

    def __init__(self, name):
        self.name = name
        self.completed = False