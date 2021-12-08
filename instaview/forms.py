from django import forms
from django.db.models import fields
from instaview.models import Image,Profile,Comment

class ImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={

        'id': 'imageform', 'class': 'uploadimage'

    }))

    class Meta:
        model = Image
        fields = ['image','title','caption']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment        
        fields=['comment']    