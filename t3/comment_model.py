import uuid

class CommentModel:
    id: str
    text: str

    def __init__(self, text: str, id: str | None = None):
        self.id = id if id is not None else str(uuid.uuid4())
        self.text = text
