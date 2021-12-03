from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Images(models.Model):

    image= CloudinaryField('image')
    title = models.CharField(max_length=100)
    caption= models.TextField(max_length=100)
    post_date = models.DateTimeField(auto_now_add=True,null=True)

    def save_image(self):
        self.save()

    def __str__(self):
        return self.title 

    def delete_image(self):
            self.delete()    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = CloudinaryField('image')
    bio = models.TextField(max_length=500, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)

    def update(self):
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
