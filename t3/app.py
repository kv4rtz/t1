from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from blog_service import BlogService

app = FastAPI()

blogService = BlogService()

@app.get("/posts")
def getAllPosts():
    return blogService.allPosts()

@app.get("/posts/{title}")
def getPost(title: str):
    try:
        return blogService.findPostByTitle(title=title)
    except ValueError:
        raise HTTPException(status_code=404, detail="Post not found")

@app.post("/posts/{title}/{content}")
def createPost(title: str, content: str):
    blogService.addPost(title=title, content=content)
    return {"msg": f"Post {title} successfully created"}

@app.patch("/posts/{oldTitle}/{newTitle}")
def editPost(oldTitle: str, newTitle: str):
    try:
        blogService.editPostTitle(oldTitle=oldTitle, newTitle=newTitle)
        return {"msg": f"Post {newTitle} successfully updated"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Post not found")

@app.delete("/posts/{title}")
def deletePost(title: str):
    try:
        blogService.deletePost(title=title)
        return {"msg": f"Post {title} successfully deleted"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Post not found")

@app.get("/posts/{title}/comments")
def getPostComments(title: str):
    try:
        post = blogService.findPostByTitle(title=title)
        return post.comments
    except ValueError:
        raise HTTPException(status_code=404, detail="Post not found")

@app.post("/posts/{title}/comments/{text}")
def createComment(title: str, text: str):
    try:
        comment = blogService.addComment(postTitle=title, text=text)
        return {"msg": f"Comment successfully created", "commentId": comment.id}
    except ValueError:
        raise HTTPException(status_code=404, detail="Post not found")

@app.patch("/posts/{title}/comments/{commentId}/{newText}")
def editComment(title: str, commentId: str, newText: str):
    try:
        blogService.findPostByTitle(title=title)
    except ValueError:
        raise HTTPException(status_code=404, detail="Post not found")

    try:
        blogService.editComment(postTitle=title, commentId=commentId, newText=newText)
        return {"msg": f"Comment {commentId} successfully updated"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Comment not found")

@app.delete("/posts/{title}/comments/{commentId}")
def deleteComment(title: str, commentId: str):
    try:
        blogService.findPostByTitle(title=title)
    except ValueError:
        raise HTTPException(status_code=404, detail="Post not found")

    try:
        blogService.deleteComment(postTitle=title, commentId=commentId)
        return {"msg": f"Comment {commentId} successfully deleted"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Comment not found")

