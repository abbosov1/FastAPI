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

