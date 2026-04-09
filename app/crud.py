from typing import Optional

from fastapi import FastAPI, Response, status, HTTPException
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


def find_post(id):
    for found_post in my_posts:
        if found_post["id"] == id:
            return found_post


def find_index_post(id):
    for i, found_post in enumerate(my_posts):
        if found_post["id"] == id:
            return i


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/posts")
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


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/latest")
async def get_latest_post():
    latest_post = my_posts[len(my_posts) - 1]
    return {"detail": latest_post}


@app.get("/posts/{id}")
async def get_post(id: int, response: Response):
    found_post = find_post(id)
    if not found_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} not found")
        # or we can use this:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"Post with id {id} not found"}
    return {"post_detail": found_post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    # deleting post
    # find the index of the array that has a required ID
    # my_posts.pop(index)
    index = find_index_post(id)
    if not index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id {id} not found")
    post_dict = post.dict()
    post_dict['id'] = index
    my_posts[index] = post_dict
    print(post)
    return {"detail": post_dict}

# @app.patch("/posts/{id}", status_code=status.HTTP_202_ACCEPTED)
# async def update_post(id: int, post: Post):
#     index = find_index_post(id)
#     if index == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Post with id {id} not found")
#     post_dict = post.dict()
#     post_dict['id'] = index
#     my_posts[index] = post_dict
#     return {"detail": post_dict}
