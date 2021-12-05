from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
    image= CloudinaryField('image')
    title = models.CharField(max_length=100)
    caption= models.TextField(max_length=100)
    post_date = models.DateTimeField(auto_now_add=True,null=True)
    # profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    like_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    def save_image(self):
        self.save()

    def __str__(self):
        return self.title 

    def delete_image(self):
            self.delete()    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    profile_photo = CloudinaryField('image')
    bio = models.TextField(max_length=500, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)
    
    def update(self,title,caption):
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    
class Likes(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.likes

    # def __str__(self):
    #     return self.user


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    comment = models.CharField(max_length=50)
    comment_date = models.DateTimeField(auto_now_add=True)

    def save_comment(self):
        self.save()

   
    def delete_comment(self):
        self.delete()

    def __str__(self):
        return self.comment_date        