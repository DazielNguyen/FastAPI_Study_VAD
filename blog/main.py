from fastapi import FastAPI, Depends
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
app = FastAPI()

# Create the database tables
models.Base.metadata.create_all(engine)

def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()


# Store blog posts in to database
@app.post("/blog")
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog