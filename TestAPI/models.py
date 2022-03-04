from tkinter import CASCADE
from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    phone = models.IntegerField()

class Profile(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    address = models.CharField(max_length=100)
    pincode = models.IntegerField()
    state = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)