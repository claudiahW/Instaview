from django.urls import path
from django.contrib import admin
from .import views


urlpatterns = [
    path('',views.index,name = 'index'),
    path('profile/', views.profile, name='profile'),
    path('like/<int:id>/', views.like_image, name='like.image'),

]