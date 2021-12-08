from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
    image= CloudinaryField('image')
    title = models.CharField(max_length=100)
    caption= models.TextField(max_length=100)
    post_date = models.DateTimeField(auto_now_add=True,null=True)
    liked= models.ManyToManyField(User,default=None,blank=True,related_name='liked')
    # profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    like_count = models.IntegerField(default=0)

    @receiver(post_save , sender = User)
    def create_profile(instance,sender,created,**kwargs):
      if created:
        Profile.objects.create(user = instance)

    @receiver(post_save,sender = User)
    def save_profile(sender,instance,**kwargs):
      instance.profile.save()
    
    def save_image(self):
        self.save()



    def __str__(self):
        return self.title 

    def delete_image(self):
            self.delete()    

    @classmethod
    # search images using image name
    def search_image_name(cls, search_term):
        images = cls.objects.filter(
        title__icontains=search_term)
        return images   

    @property
    def saved_comments(self):
        return self.comments.all() 

    def _str_(self):
        return self.user.username       

    def _str_(self):
        return self.title        

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    profile_photo = CloudinaryField('image')
    bio = models.TextField(max_length=500, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)

    @receiver(post_save , sender = User)
    def create_profile(instance,sender,created,**kwargs):
      if created:
        Profile.objects.create(user = instance)

    @receiver(post_save,sender = User)
    def save_profile(sender,instance,**kwargs):
      instance.profile.save()
    
    def update(self,title,caption):
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

LIKE_CHOICES={
    ('Like','Like'),
    ('Dislike','Dislike',)
}
class Likes(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,default='like',max_length=10)

    def _str_(self):
        return self.value
    
    def __str__(self):
        return self.likes

    # def __str__(self):
    #     return self.user


class Comment(models.Model):
    comment = models.CharField(max_length=250)
    image = models.ForeignKey(Image,on_delete = models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='comments')

    @classmethod
    def display_comment(cls,image_id):
        comments = cls.objects.filter(image_id = image_id)
        return comments

        
