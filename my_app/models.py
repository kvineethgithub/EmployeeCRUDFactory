from django.db import models


# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    salary = models.CharField(max_length=55)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
