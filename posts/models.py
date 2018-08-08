from django.db import models
from datetime import datetime

# Create your models here.


class User(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    age=models.IntegerField()
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

    def __str__(self):
        return "{}{}".format(self.firstname,self.lastname)


class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    createted_at= models.DateField(default=datetime.now,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title