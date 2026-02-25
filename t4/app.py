from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from library_service import LibraryService

app = FastAPI()

libraryService = LibraryService()

@app.get("/books")
def getAllBooks():
    return libraryService.allBooks()

@app.get("/books/{title}")
def getBook(title: str):
    try:
        return libraryService.findBookByTitle(title=title)
    except ValueError:
        raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books/{title}/{author}")
def createBook(title: str, author: str):
    libraryService.addBook(title=title, author=author)
    return {"msg": f"Book {title} successfully created"}

@app.delete("/books/{title}")
def deleteBook(title: str):
    try:
        libraryService.deleteBook(title=title)
        return {"msg": f"Book {title} successfully deleted"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Book not found")

@app.get("/readers")
def getAllReaders():
    return libraryService.allReaders()

@app.post("/readers/{name}")
def createReader(name: str):
    libraryService.addReader(name=name)
    return {"msg": f"Reader {name} successfully created"}

@app.post("/borrow/{title}/{readerName}")
def borrowBook(title: str, readerName: str):
    try:
        libraryService.borrowBook(title=title, readerName=readerName)
        return {"msg": f"Book {title} successfully borrowed by {readerName}"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Book or reader not found")
    except RuntimeError:
        raise HTTPException(status_code=400, detail="Book already borrowed")

@app.post("/return/{title}/{readerName}")
def returnBook(title: str, readerName: str):
    try:
        libraryService.returnBook(title=title, readerName=readerName)
        return {"msg": f"Book {title} successfully returned by {readerName}"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Book or reader not found")
    except RuntimeError as ex:
        if str(ex) == "Not borrowed":
            raise HTTPException(status_code=400, detail="Book is not borrowed")
        raise HTTPException(status_code=400, detail="Book is borrowed by another reader")
