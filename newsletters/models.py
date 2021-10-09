from django.db import models


# Create your models here.
from tags.models import Tags
from users.models import Users


class NewsLetters(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='assets/newsletters')
    target = models.CharField(max_length=50)
    frequency = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)

    users = models.ManyToManyField(Users, related_name='users')
    tags = models.ManyToManyField(Tags, related_name='tags')

    def __str__(self):
        return self.name



