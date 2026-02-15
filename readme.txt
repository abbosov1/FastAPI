                                                                        Explaining the beginning of hte code
# firstly you have to understand what is going on: so now @app.get means that written a thing in third
# line means how to call our FastAPI for example here we gave name an app, and so we used @app in line
# six. @app.get("/") what does it mean: in FastAPI called app when comes request get in page "/"
# async - working asyncio
# def - function
# root - name of the function we can use any name, but actually we should name it by the functionality
# of the function for example if we write code for API logins we will name it login_user or just login
# return {"message: "Hello World""} - means what this function actually is returning us when it will
# receive a request get. here output will be: {"message":"Hello World"}.
# / = it's like a home page we can say no actually it's the page where we are staying, I mean
# for example about/ equal to about




                                            Explaining how works a CRUD.
CRUD

C - Create. Create -> Post request an example --> @app.post("/posts")

R - Read. Read -> Get request, it's gonna be like this --> /posts or by choosing one post by its id --> /posts/:id
    an example: @app.get("/posts/{id}") or for all the posts @app.get("/posts")

U - Update. Update -> Put/Patch request, here we have two types of update Put and Patch
    We use Put for updating all the datas even which weren't updated like a change was at only two files, but we made
    git commit for all the files, an example for this --> @app.put("/posts/{post_id}")
    We use Patch to update only one thing using or chosen things without touching others an example for this -->
    @app.patch("/posts/{post_id}")


    PUT и PATCH в REST API используются для обновления ресурсов, но имеют разные цели и принципы работы.
    PUT заменяет весь ресурс целиком, требуя отправки всех полей. PATCH производит частичное обновление,
    меняя только указанные поля, что эффективнее при небольших изменениях. PUT — всегда идемпотентен, PATCH — нет.
    Ключевые отличия PUT и PATCH:
    PUT (Полная замена):
    Принцип: Клиент отправляет обновленную версию ресурса, которая целиком замещает старую.
    Данные: Необходимо отправлять весь объект, даже если меняется только одно поле. Если поле не указано,
    оно может быть затерто (или обнулено).
    Идемпотентность: Да (многократный вызов не меняет результат).
    PATCH (Частичное обновление):
    Принцип: Клиент отправляет только набор инструкций (изменений), которые нужно применить к ресурсу.
    Данные: Отправляются только те поля, которые нужно изменить.
    Идемпотентность: Нет (в зависимости от реализации, может не быть).
    Пример:
    Если у пользователя есть {"name": "Ivan", "age": 25}:
    PUT /users/1 с {"name": "Dmitry"} сделает: {"name": "Dmitry"} (возраст исчезнет).
    PATCH /users/1 с {"name": "Dmitry"} сделает: {"name": "Dmitry", "age": 25}.
    Что выбрать?
    Используйте PUT, когда у вас есть полный объект и вы хотите обновить его целиком, или если ресурс простой.
    Используйте PATCH, когда нужно обновить одно или несколько полей, не затрагивая остальные.



D - Delete. Delete -> Delete request, deleting data an example for this --> @app.delete("/posts/{post_id}")





                                                        Sending Requests:

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


@app.get("/posts/{id}")  |   here writen path of the how to get a single post. @app.get = method of request. ("/posts/{id}") = it' a path where we can get the post
async def get_post(id: int): | here written name and validation for our search function.
#                             async = working asynco; def = function; get_post = name of the function; (id: int) = parameters of a function, the id has to be int it's a validation.
    found_post = find_post(id) | found_post = name of the variable; = = equal; find_post = we're calling the function named
#                                find_post; (id) = give this parameter to it like what is the input and what I have to search here it will be search details of a post with this {id}
    print(found_post)          | print output to the console
    return {"post_detail": found_post}  | called return for the output


@app.get("/posts/latest")   | new app for latest post
async def get_latest_post():    | given name for function
    latest_post = my_posts[len(my_posts) - 1]   | created variable, and it's equal to my_post .... my_post[] = called dictionary
#                                               | len(my_post) - 1 = take the latest value of (this) dictionary
    return {"detail": latest_post}  | called return for the output

                                                        FOCUS ON THIS PART CAREFULLY

    WE GAVE PARAMETER ID FOR SEARCHING SINGLE POST AND IT IS WORKING AND WHEN WE WANT TO SEARCH LATEST POST IT WILL RETURN AN ERROR

                                                                BUT WHY?
    BECAUSE UNTIL LATEST POSTS WE GAVE PARAMETER TO SEARCHING SINGLE POST SO WHEN WE CALLED LATEST POST IT FIRSTLY LOOKED FOR THE IS THERE ANY PARAMETER ABOVE OR NOT
    AND IT COULD FIND PARAMETER INT AT SEARCHING SINGLE POST AND THE SEARCHING LATEST POST GET THAT PARAMETER TO ITSELF.

    HERE WE CAN DO ONLY ONE THING TAKE THAT FUNCTION ABOVE THE SEARCHING POST BY ID

    TAKE LATEST FUNCTION ABOVE THE SEARCHING POST BY ID








@app.get("/posts/latest")
async def get_latest_post():
    latest_post = my_posts[len(my_posts) - 1]
    return {"detail": latest_post}


@app.get("/posts/{id}")
async def get_post(id: int, response: Response):    | added another parameter response import this "from fastapi import FastAPI, Response, status"
    found_post = find_post(id)
    if not found_post:  | if statement, if found_post is not found
        response.status_code = status.HTTP_404_NOT_FOUND    | used response, if the status is equal to not found 404
        return {"detail": f"Post with id {id} not found"}   | return this output.
    return {"post_detail": found_post}                      | this gonna be like an else statement.



and also we can replace:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detail": f"Post with id {id} not found"}
with:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")









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



@app.post("/posts")
async def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


HERE WE CAN SEE DICTIONARY WITH DATA AND FUNCTION FOR CREATING POSTS THEY'RE STAYING CORRECT AND THEY'RE WORKING BUT THERE IS ONE ISSUE
HERE WHEN WE CREATE ANY POST CODE OF REQUEST WILL BECOME 200 BUT IT HAS TO BE 201, SO WE HAVE TO CHANGE THE CODE TO THIS:





@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}
