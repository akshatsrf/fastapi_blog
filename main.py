from fastapi import FastAPI,Depends
import schemas,models
from sqlalchemy.orm import Session
from database import engine,SessionLocal
from celery import Celery

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def func():
    return "Add /docs in the URL for Swagger UI"

@app.post('/blog')
def create(blog: schemas.Blog, db: Session = Depends(get_db)):
    new_blog  = models.Blog(title = blog.title, body = blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog')
def all( db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs
