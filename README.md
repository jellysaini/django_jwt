# Django with JWT

This project is helpful in case where you want to implement the JWT(JSON Web Token) in your django app.

## Step

### Create a python env(here we are using virtualwrapper package)
### `mkvirtualenv jwt`

### Activate env
### `workon jwt`

### Install the requirements
### `pip install -r requirements.txt`

### Run via
### `python manage.py runserver`


### To run the swagger go to
### `http://localhost:8000/api/swagger/`


### Login or signup. This will return the access token
```json
{
  "code": 200,
  "status": "success",
  "result": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg0MjQyMDk5LCJpYXQiOjE2ODQyNDE3OTksImp0aSI6IjVjMWRkMjc4NjIwZDQ4YTViYTc1MTA2MDEwNjM5MDZjIiwidXNlcl9pZCI6MX0.1bWgO8nCNM2IjiV8LMvAbNBDhhF7lYMSoDjyXJUR2Ik"
  }
}
```


### Click on `Authorize` Button. Fill `Bearer your_access_token`
for example
`Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg0MjQyMDk5LCJpYXQiOjE2ODQyNDE3OTksImp0aSI6IjVjMWRkMjc4NjIwZDQ4YTViYTc1MTA2MDEwNjM5MDZjIiwidXNlcl9pZCI6MX0.1bWgO8nCNM2IjiV8LMvAbNBDhhF7lYMSoDjyXJUR2Ik`


### Now you can access any url with authentication required. For example in this case `/home/` url.

