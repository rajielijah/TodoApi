from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length = 150)
    desc = models.CharField(max_length=100)
    body = models.CharField(max_length=450)

    def __str__(self):
        return self.title