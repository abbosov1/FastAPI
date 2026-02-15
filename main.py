from typing import Optional

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {
        "title": "My first post",
        "content": "Yes, this post",
        "id": 2
    },
    {
        "title": "My second post",
        "content": "No, not this post",
        "id": 1
    }
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/post")
async def get_posts():
    return {"data": my_posts}

#
# @app.post("/posts")
# async def create_posts(new_post: Post):
#     print(new_post.title)
#     print(new_post.content)
#     print(new_post.published)
#     print(new_post.rating)
#     print(new_post.dict())
#     return {"data": new_post}
#     return {"data": "Posted Successfully"}


@app.post("/posts")
async def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}