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









                                    Working with postgres
download postgres and pgAdmin open pgAdmin there will be password ect. ect. ect. so I think you can understand how to open and run it.
So the first thing what we will do is:
    pgAdmin:

        Servers → with right button → Register → Server
        General tab:

        Name: Postgres (Admin)


        Connection tab:

        Host: localhost
        Port: 5432
        Username: postgres
        Maintenance database: postgres
        Password: (what you want)


        Save



                            Postgres in terminal:
open - sudo -u username psql or psql -U username
open the directory -psql -U username -d db_name

-U -> пользователь (User)
-d -> база данных (Database)
-h -> хост (Host)
-p -> порт (Port)
-W -> спросить пароль(Ask password)

list of the dbs -> psql -U username -l (without entering to the db)
SQL request -> psql -U username -c "SELECT * FROM users;"


Connection and information:

\q -- log out of psql
\l -- list of all databases
\c dbname -- connect to the database
\conninfo -- information about the current connection
\du -- list of users and roles
\dn -- list of schemas


Tables:

\dt -- list of tables
\dt *.* -- list of all tables in all schemas
\d tablename -- table structure (columns, types)
\di -- list of indexes
\dv -- list of views
\ds -- list of sequences

HELP:

\h -- list of all SQL commands
\h CREATE TABLE -- help for a specific command
\? -- list of all \ commands


SQL commands:

CREATE DATABASE mydb;
DROP DATABASE mydb;


Users:

CREATE USER username WITH PASSWORD 'pass';
ALTER USER username WITH SUPERUSER;
ALTER USER username WITH PASSWORD 'newpass';
DROP USER username;


Tables:

-- Create a table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    age INT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Delete the table
DROP TABLE users;

-- Change the table
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
ALTER TABLE users DROP COLUMN phone;
ALTER TABLE users RENAME COLUMN name TO full_name;


CRUD operations:

-- Add data
INSERT INTO users (name, email, age) VALUES ('Name', 'ab@mail.com', 25);

-- Get the data
SELECT * FROM users;
SELECT name, email FROM users;
SELECT * FROM users WHERE age > 20;
SELECT * FROM users ORDER BY name ASC;
SELECT * FROM users ORDER BY name DESC;
SELECT * FROM users LIMIT 10;

-- Update the data
UPDATE users SET age = 26 WHERE name = 'Name';

-- Delete data
DELETE FROM users WHERE id = 1;
DELETE FROM users; -- удалить все записи


Filtering:

WHERE age > 20
WHERE name = 'Name'
WHERE name LIKE 'Ab%'        -- starts with Ab
WHERE age BETWEEN 20 AND 30
WHERE name IN ('Ali', 'Bob')
WHERE email IS NULL
WHERE email IS NOT NULL


Aggregate functions:

SELECT COUNT(*) FROM users;
SELECT MAX(age) FROM users;
SELECT MIN(age) FROM users;
SELECT AVG(age) FROM users;
SELECT SUM(age) FROM users;
SELECT name, COUNT(*) FROM users GROUP BY name;


JOIN (объединение таблиц):

-- INNER JOIN
SELECT users.name, orders.product
FROM users
INNER JOIN orders ON users.id = orders.user_id;

-- LEFT JOIN
SELECT users.name, orders.product
FROM users
LEFT JOIN orders ON users.id = orders.user_id;


Indexes:

CREATE INDEX idx_name ON users(name);
DROP INDEX idx_name;


Rights:

GRANT ALL PRIVILEGES ON DATABASE mydb TO username;
GRANT SELECT, INSERT ON users TO username;
REVOKE ALL ON users FROM username;


Transactions:

BEGIN;           -- start a transaction

COMMIT;          -- save changes

ROLLBACK;        -- undo changes


SELECT id AS product_id, is_sale AS on_sale FROM products;

here with this request we'll get id and is_sale columns with given another names for example here id returns to product_id is_sale to on_sale.


SELECT * FROM products WHERE id = 5; --> take the all data from products but only the product with id 5;

SELECT * FROM products WHERE name = 'something'; --> take the all data from products but only the product with name something;
U CAN USE ONLY SINGLE QUOTES. .
AND ALSO WE CAN USE >, <, >=, <= for integer data.


SELECT * FROM products WHERE name != 'TV' and price != 250;

SELECT * FROM products WHERE id IN (1,2,3);

SELECT * FROM products WHERE id LIKE 'TV%';  --> Select all the data which starts with 'TV' and after that any characters=%

SELECT * FROM products WHERE id LIKE '%e';   --> Select all the data which starts with any characters=% and ends with 'e'

SELECT * FROM products WHERE id NOT LIKE '%e';   --> Select all the data which starts with any characters=% and doesn't end with 'e'

SELECT * FROM products WHERE id LIKE '%e%';   --> Select all the data which starts with any characters=% and ends with any characters=% and exists 'e' anywhere

SELECT * FROM products WHERE id NOT LIKE '%e';   --> Select all the data which starts with any characters=% and ends with any characters=% and doesn't exist 'e' anywhere of the requested data
for example -> select it won't be at output because it has e in the letters if it starts with e or ends with it is okay but if it's not there, and it's in letters it won't be returned.

SELECT * FROM products where price < 10 limit 3;

SELECT * FROM products order by id limit 5 offset 2; first 2 item will be skipped.

While working with CRUD in postgres if you get error: TypeError: 'int' object does not support indexing change this:

    cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (id,))

    to this:

    cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (str(id),))