from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Link(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.title
