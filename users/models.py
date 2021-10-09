from django.db import models


# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
