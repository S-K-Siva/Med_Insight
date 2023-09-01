from django.db import models
from django.contrib.auth.models import User
import uuid


class Profile(models.Model):
    CATEGORIES = ('PATIENT','DOCTOR')
    author = models.OneToOneField(User,on_delete=True,blank=True,null=True,default=None)
    username = models.CharField(max_length=200,null=True,blank=True)
    bio = models.TextField(max_length=2000,null=True,blank=True)
    email = models.EmailField(max_length=200,null=True,blank=True)
    profile_image = models.ImageField(null=True,blank=True)
    category = models.CharField(max_length=8,choices=CATEGORIES,default=CATEGORIES[0])
    id = models.UUIDField(uuid=uuid.uuid5,unique=True,editable=False,primary_key=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.author} - {self.category}"


    


