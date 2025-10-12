from fastapi import FastAPI
from . import schemas, models
from .database import engine

app = FastAPI()

# Create the database tables
models.Base.metadata.create_all(engine)


# Store blog posts in to database
@app.post("/blog")
def create(request: schemas.Blog):
    return request