import uvicorn
from fastapi import FastAPI
from routers import books, authors


app = FastAPI(title="Books API")


app.include_router(authors.router)
app.include_router(books.router)


if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)