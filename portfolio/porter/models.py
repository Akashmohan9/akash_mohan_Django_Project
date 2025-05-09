from django.db import models

#django:-
#D-b:- sub-module
#models:- main modules to use

# Create your models here.

class Product(models.Model):
    Name = models.CharField(max_length=122)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    message = models.CharField(max_length=1000)
