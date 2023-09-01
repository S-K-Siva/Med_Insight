from django.db import models
from django.contrib.auth.models import User
import uuid
def upload_to(instance, filename):
    return '/Users/sivasakthivel/Desktop/Med_Insighto/Med_Insight/users/images/{filename}'.format(filename=filename)

# class MyModel(models.Model):
#     creator = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="listings")
#     title = models.CharField(
#         max_length=80, blank=False, null=False)
#     description = models.TextField()
#     image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)

# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

class MyModel(models.Model):
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="listings")
    # title = models.CharField(
    #     max_length=80, blank=False, null=False)
    # description = models.TextField()
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)


class Profile(models.Model):
    CATEGORIES = (
        ('PATIENT','P'),
        ('DOCTOR','D')
    )

    author = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True,default=None)
    username = models.CharField(max_length=200,null=True,blank=True)
    bio = models.TextField(max_length=2000,null=True,blank=True)
    email = models.EmailField(max_length=200,null=True,blank=True)
    profile_image = models.ImageField(null=True,blank=True,upload_to="")
    category = models.CharField(max_length=8,choices=CATEGORIES,default=CATEGORIES[0])
    id = models.UUIDField(default=uuid.uuid4,unique=True,editable=False,primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.category}"

    