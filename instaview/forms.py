from django import forms
from django.db.models import fields
from instaview.models import Image,Profile

class ImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={

        'id': 'imageform', 'class': 'uploadimage'

    }))

    class Meta:
        model = Image
        fields = ['image','title','caption']