from django.db import models

class MyModel(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    passwordcheack = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    studentid = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)