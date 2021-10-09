from django.db import models

# Create your models here.
from newsletters.models import NewsLetters
from users.models import Users


class Votes(models.Model):
    updatedAt = models.DateTimeField(auto_now=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    newsletter = models.ForeignKey(NewsLetters, on_delete=models.CASCADE)
