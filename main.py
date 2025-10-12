from fastapi import FastAPI    

app = FastAPI()
@app.get("/") # dùng để khai báo route
def index():
    return {'data' : {'name' : 'Van Anh Duy', 'age' : 21}}

@app.get("/about")
def about():
    return {'data' : {'about page' : 'This is about page'}}