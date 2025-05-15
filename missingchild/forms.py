from django.db import models
from django.forms import Form, CharField,PasswordInput,FileField

class MissingPersons(Form):
    name=CharField(max_length=50)
    age=CharField(max_length=50)
    gender=CharField(max_length=50)
    skincolor=CharField(max_length=50)
    height = CharField(max_length=50)
    languages = CharField(max_length=50)
    isdisabled = CharField(max_length=50)
    ishavingmadness = CharField(max_length=50)
    image = FileField()
    nationality = CharField(max_length=50)
    state = CharField(max_length=50)
    education = CharField(max_length=50)
    dateofmissing = CharField(max_length=50)
    locationofmissing = CharField(max_length=50)
    locationofmoles = CharField(max_length=50)

class LoginForm(Form):
    username = CharField(max_length=100)
    password = CharField(widget=PasswordInput())

class UserForm(Form):

    name = CharField(max_length=500)
    username = CharField(max_length=500)
    password = CharField(max_length=500)
    email = CharField(max_length=500)
    mobile = CharField(max_length=500)
    address = CharField(max_length=500)
    gender = CharField(max_length=500)
    age = CharField(max_length=500)