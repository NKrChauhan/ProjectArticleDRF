# Documentation

This is a Django project that consists of two apps - `user` and `article`. The `user` app provides functionality for user registration, authentication, and password management, while the `article` app allows users to create, view, update, and delete articles.

## Requirements

To run this project, you will need to have the following installed on your system:

- Python 3.x
- Django 3.x
- Django Rest Framework (DRF) 3.x

## Installation

1. Clone the repository: `git clone https://github.com/NKRChauhan/ProjectArticleDRF.git`.
2. Install the project requirements: `pip install -r requirements.txt`.
3. Run database migrations: `python manage.py migrate`.

## Usage

### User app

#### Registration

To register a new user, send a `POST` request to the `/api/v1/user/` endpoint with the following data:

```json
{
  "email": "<email>",
  "password": "<password>"
}
```

If the request is successful, it will return status_code=201 and a new user will be created in the database, and a response with the following data will be returned:

```json
{
  "access_token": "<auth_token>"
}
```

#### Curl
```curl
    curl --request POST \
      --url http://127.0.0.1:8000/api/v1/user/ \
      --header 'Content-Type: application/json' \
      --data '{
      "email": "test_user1@gmail.com",
      "password" : "abcd@123456"
    }'
```

#### Authentication

To authenticate a user and obtain an auth token, send a `POST` request to the `/api/v1/user/` endpoint with the following data:

```json
{
  "email": "<email>",
  "password": "<password>"
}
```

If the request is successful, it will return status_code=200 and a response with the following data will be returned:

```json
{
  "access_token": "<auth_token>"
}
```

#### Curl
```curl
    curl --request POST \
      --url http://127.0.0.1:8000/api/v1/user/ \
      --header 'Content-Type: application/json' \
      --data '{
      "email": "test_user1@gmail.com",
      "password" : "abcd@123456"
    }'
```

#### Password Management

To obtain an auth token after changing the password, send a `PUT` request to the `/api/v1/user/` endpoint with the following data:

```json
{
  "email": "<email>"
  "previous_password": "<old_password>",
  "password": "<new_password>"
}
```
If the request is successful, it will return status_code=200 and a response with the following data will be returned:

```json
{
  "access_token": "<auth_token>"
}
```

#### Curl
```curl
    curl --request POST \
      --url http://127.0.0.1:8000/api/v1/user/ \
      --header 'Content-Type: application/json' \
      --data '{
      "email": "test_user1@gmail.com",
      "previous_password" : "abcd@123456",
      "password" : "abcd@1234567"
    }'
```

### Article app

#### Articles

##### Note
Each article request made must contain an `Authorization` token header like this:
```
    "Authorization": "Token <access_token>"
```


To retrieve a list of all articles, send a `GET` request to the `/api/v1/article/` endpoint. 
If the request is successful, it will return status_code=200 and a response with the following data will be returned:

```json
[
  {
    "id": "<article_id>",
    "title": "<title>",
    "content": "<content>",
    "banner": "<encoded_banner_image>"
  },
  ...
]
```

#### Curl
```curl
    curl --request GET \
      --url http://127.0.0.1:8000/api/v1/article/ \
      --header 'Authorization: Token 41be6b8847fbb184d8925754aaa130d68ea672df' \
      --header 'Content-Type: application/json'
    }'
```


To retrieve details for a specific article, send a `GET` request to the `/api/v1/article/<article_id>` endpoint, where `<article_id>` is the ID of the article you want to retrieve. 
If the request is successful, it will return status_code=200 and a response with the following data will be returned:

```json
{
  "id": "<article_id>",
  "title": "<title>",
  "content": "<content>",
  "banner": "<encoded_banner_image>"
}
```

#### Curl
```curl
    curl --request GET \
      --url http://127.0.0.1:8000/api/v1/article/1 \
      --header 'Authorization: Token 41be6b8847fbb184d8925754aaa130d68ea672df' \
      --header 'Content-Type: application/json'
    }'
```

#### Create and Update Articles

To create a new article, send a `POST` request to the `/api/v1/article/` endpoint with the following data:

```json
{
  "title": "<title>",
  "content": "<content>",
  "banner": "<banner_image_encoded>"
}
```

If the request is successful, it will return status_code=201 and a response with the following data will be returned:

```json
{
  "id": "<article_id>",
  "title": "<title>",
  "content": "<content>",
  "banner": "<banner_image_encoded>"
}
```

##### Curl
```curl
  curl --request POST \
    --url http://127.0.0.1:8000/api/v1/article/ \
    --header 'Authorization: Token 41be6b8847fbb184d8925754aaa130d68ea672df' \
    --header 'Content-Type: application/json' \
    --data '{
    "title": "test",
    "content": "something awesome1"
  }'
```

To update an existing article, send a `PUT` request to the `/api/v1/article/<article_id>` endpoint, where `<article_id>` is the ID of the article you want to update. Include the updated data:

```json
{
  "title": "<title>",
  "content": "<content>",
  "banner": "<encoded_banner_image>"
}
```

If the request is successful, it will return status_code=200 and a response with the following data will be returned:

```json
{
  "id": "<article_id>",
  "title": "<title>",
  "content": "<content>",
  "banner": "<banner_image_encoded>"
}
```

##### Curl
```curl
  curl --request PUT \
    --url http://127.0.0.1:8000/api/v1/article/3 \
    --header 'Authorization: Token 41be6b8847fbb184d8925754aaa130d68ea672df' \
    --header 'Content-Type: application/json' \
    --data '{
    "title": "test",
    "content": "something awesome1"
  }'
```

#### Delete Articles

To delete a specific article, send a `DELETE` request to the `/api/v1/article/<article_id>` endpoint, where `<article_id>` is the ID of the article you want to delete. 
##### Delete
```curl
  curl --request DELETE \
    --url http://127.0.0.1:8000/api/v1/article/3 \
    --header 'Authorization: Token 41be6b8847fbb184d8925754aaa130d68ea672df' \
    --header 'Content-Type: application/json'
  }'
```

If the request is successful, a response with status_code = 204 will be returned

#### Points of improvement:
- test cases can be added more
- user endpoints can be different for eg: 
  - /register/ -> for new user registration
  - /auth/ -> for retriving auth token
  - /change_password/ -> to change password
