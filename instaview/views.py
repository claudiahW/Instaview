from django.shortcuts import render
from .models import Images 



def index(request):
    image= Images.objects.all().order_by('-id')
    return render(request, 'all-photos/index.html', {'image':image})
 
# def index(request):

#     Image = Images.objects.all().order_by('-id')

#     return render(request, 'all-insta/index.html',{'Image':Image})