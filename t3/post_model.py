import uuid
from comment_model import CommentModel

class PostModel:
    title: str
    content: str
    comments: list[CommentModel]

    def __init__(self, title: str, content: str = ""):
        self.title = title
        self.content = content
        self.comments = []
