from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models
from .database import *

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


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


@app.get("/posts")
async def get_posts():
    cursor.execute(""" SELECT *
                       FROM posts """)
    posts = cursor.fetchall()
    return {"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    cursor.execute(""" INSERT INTO posts (title, content, published)
                       VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
    created_post = cursor.fetchone()
    conn.commit()
    return {"data": created_post}


@app.get("/posts/{id}")
async def get_post(id: int):
    cursor.execute(""" SELECT *
                       FROM posts
                       WHERE id = %s """, (id,))
    found_post = cursor.fetchone()
    if not found_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} not found")
        # or we can use this:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"Post with id {id} not found"}
    return {"post_detail": found_post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    cursor.execute(""" DELETE
                       FROM posts
                       WHERE id = %s returning * """, (id,))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_post(id: int, post: Post):
    cursor.execute(""" UPDATE posts
                       SET title     = %s,
                           content   = %s,
                           published = %s
                       where id = %s returning *""", (post.title, post.content, post.published, id))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} not found")

    return {"detail": updated_post}


@app.get('/tt')
async def get_tt(db: Session = Depends(get_db)):
    return {'status': 'ok'}
