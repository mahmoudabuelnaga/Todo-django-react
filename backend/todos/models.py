from pydoc import describe
from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=220)
    body = models.TextField()

    def __str__(self):
        return self.title