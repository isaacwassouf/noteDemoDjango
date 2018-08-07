from django.db import models
from datetime import datetime

# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    createted_at= models.DateField(default=datetime.now,blank=True)

    def __str__(self):
        return self.title