from fastapi import FastAPI    
from typing import Optional
from pydantic import BaseModel

import uvicorn
app = FastAPI()
@app.get("/blog")  # dùng để khai báo route
def index(limit=10, published: bool = True, sort: Optional[str] = None):  # khai báo kiểu dữ liệu cho biến limit và published
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} published Blogs from DB'}
    else:   
        return {'data': f'{limit} Blogs from DB'}

@app.get("/blog/unpublished")
def unpublished():
    # fetch unpublished blogs
    return {'data' : 'all unpublished blogs'}

@app.get("/blog/{id}")
def show(id: int):
    # fetch blog with id = id
    return {'data' : id}


@app.get("/blog/{id}/comments")
def comments(id, limit=10):
    # fetch comments of blog with id = id
    return {'data' : {'1','2'}}



class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]  # not required


@app.post("/blog")
def create_blog(blog: Blog):
    return {'data': f'Blog is created with title as {blog.title}'}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)