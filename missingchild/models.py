from django.db import models
from django.db.models import Model

class MissingPersonModel(Model):

    name=models.CharField(max_length=50)
    age=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    skincolor=models.CharField(max_length=50)
    height = models.CharField(max_length=50)
    languages = models.CharField(max_length=50)
    isdisabled = models.CharField(max_length=50)
    image = models.FileField(upload_to="images")
    ishavingmadness = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    education = models.CharField(max_length=50)
    dateofmissing = models.CharField(max_length=50)
    locationofmissing = models.CharField(max_length=50)
    locationofmoles = models.CharField(max_length=50)
    userid= models.CharField(max_length=50)

    class Meta:
        db_table = "missingpersons"


class RecordModel(models.Model):

    name = models.CharField(max_length=500)
    recordeddate = models.DateTimeField(auto_now=True, blank=False, null=False)

    class Meta:
        db_table = "record"


class UserModel(Model):

    name = models.CharField(max_length=500)
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    mobile = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    gender = models.CharField(max_length=500)
    age = models.CharField(max_length=500)

    class Meta:
        db_table = "clients"