from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models
from .schemas import *
from .database import *

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="FastAPI",
            user="abbosov",
            password="abbosovm",
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("Database connection established")
        break
    except Exception as error:
        print("Database connection failed")
        print(error)
        time.sleep(2.5)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts", response_model=List[Post])
async def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return posts


@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=Post)
async def create_post(post: PostCreate, db: Session = Depends(get_db)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@app.get("/posts/{id}", response_model=Post)
async def get_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} not found")
        # or we can use this:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"Post with id {id} not found"}
    return post


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=Post)
async def update_post(id: int, post: PostCreate, db: Session = Depends(get_db)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    updated_post = post_query.first()
    conn.commit()
    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} not found")

    post_query.update(post.dict(), synchronize_session=False)
    db.commit()

    return post_query.first()
