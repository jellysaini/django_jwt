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


### To run run the swagger go to
### `http://localhost:8000/api/swagger/`


### Login or signup. This will return the access token

### Click on `Authorize` Button. Fill `Bearer your_access_token`


### Now you can access any url with authentication required. For example in this case `/home/` url.

