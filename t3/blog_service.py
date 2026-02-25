from post_model import PostModel
from comment_model import CommentModel

class BlogService:
    posts: list[PostModel]

    def __init__(self):
        self.posts = []

    def allPosts(self):
        return self.posts

    def findPostByTitle(self, title: str):
        for post in self.posts:
            if post.title == title:
                return post
        raise ValueError("Not Found")

    def addPost(self, title: str, content: str = ""):
        self.posts.append(PostModel(title=title, content=content))

    def editPostTitle(self, oldTitle: str, newTitle: str):
        post = self.findPostByTitle(title=oldTitle)
        post.title = newTitle

    def deletePost(self, title: str):
        for index, post in enumerate(self.posts):
            if post.title == title:
                del self.posts[index]
                return
        raise ValueError("Not Found")

    def addComment(self, postTitle: str, text: str):
        post = self.findPostByTitle(title=postTitle)
        comment = CommentModel(text=text)
        post.comments.append(comment)
        return comment

    def editComment(self, postTitle: str, commentId: str, newText: str):
        post = self.findPostByTitle(title=postTitle)
        for comment in post.comments:
            if comment.id == commentId:
                comment.text = newText
                return
        raise ValueError("Not Found")

    def deleteComment(self, postTitle: str, commentId: str):
        post = self.findPostByTitle(title=postTitle)
        for index, comment in enumerate(post.comments):
            if comment.id == commentId:
                del post.comments[index]
                return
        raise ValueError("Not Found")
