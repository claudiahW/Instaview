from django.shortcuts import render
from .models import Image,Likes 
from django.contrib.auth.decorators import login_required
from .forms import ImageForm,CommentForm
from django.shortcuts import render,redirect, get_object_or_404


def index(request):
    image= Image.objects.all().order_by('-id')
    return render(request, 'all-photos/index.html', {'image':image})
 
@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    # get images for the current logged in user
    image = Image.objects.filter(user_id=current_user.id)
    # get the profile of the current logged in user
    # profile = Profile.objects.filter(user_id=current_user.id).first()
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm (request.POST , request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
        redirect('profile')
    return render(request, 'profile.html', {"image": image, "profile": profile , "form": form})
    
@login_required(login_url='/accounts/login/')
def search_post(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search').lower()
        images = Image.search_image_name(search_term)
        message = f'{search_term}'

        return render(request, 'all-photos/search.html', {'found': message, 'images': images})
    else:
        message = 'Not found'
        return render(request, 'all-photos/search.html', {'danger': message})
    
def like_image(request):
    user = request.user
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        image_pic =Image.objects.get(id=image_id)
        if user in image_pic.liked.all():
            image_pic.liked.add(user)
        else:
            image_pic.liked.add(user)    
            
        like,created =Likes.objects.get_or_create(user=user, image_id=image_id)
        if not created:
            if like.value =='Like':
               like.value = 'Dislike'
        else:
               like.value = 'Like'

        like.save()       
    return redirect('index')

@login_required
def comments(request,image_id):
  form = CommentForm()
  image = Image.objects.filter(pk = image_id).first()
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit = False)
      comment.user = request.user
      comment.image = image
      comment.save() 
  return redirect('index')    