from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    createted_at= models.DateField(default=datetime.now,blank=True)
    user= models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE,default=1)
    is_locked= models.BooleanField(default=False)
    lock_password= models.CharField(max_length=255,default='')

    def __str__(self):
        return self.title
    