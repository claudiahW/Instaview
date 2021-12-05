from django.shortcuts import render
from .models import Image,Profile 
from django.contrib.auth.decorators import login_required
from .forms import ImageForm
from django.shortcuts import render,redirect, get_object_or_404


def index(request):
    image= Image.objects.all().order_by('-id')
    return render(request, 'all-photos/index.html', {'image':image})
 
@login_required(login_url='/accounts/login/')
# def profile(request):
#     current_user = request.user
#     # get images for the current logged in user
#     image = Image.objects.filter(user_id=current_user.id)
#     # get the profile of the current logged in user
#     profile = Profile.objects.filter(user_id=current_user.id).first()
#     form = ImageForm()
#     if request.method == 'POST':
#         form = ImageForm (request.POST , request.FILES)
#         if form.is_valid():
#             form.instance.user = request.user
#             form.save()
#         redirect('profile')
#     return render(request, 'profile.html', {"image": image, "profile": profile , "form": form})

@login_required(login_url='/accounts/login')
def search_profile(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get("search_user")
        results = Profile.search_profile(name)
        message = f'name'
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'results.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'results.html', {'message': message})    


    