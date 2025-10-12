from fastapi import FastAPI    

app = FastAPI()
@app.get("/") # dùng để khai báo route
def index():
    return {'data' : 'Block list'}

@app.get("/blog/unpublished")
def unpublished():
    # fetch unpublished blogs
    return {'data' : 'all unpublished blogs'}

@app.get("/blog/{id}")
def show(id: int):
    # fetch blog with id = id
    return {'data' : id}


@app.get("/blog/{id}/comments")
def comments(id):
    # fetch comments of blog with id = id
    return {'data' : {'1','2'}}