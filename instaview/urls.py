from django.urls import path
from django.contrib import admin
from .import views


urlpatterns = [
    path('',views.index,name = 'index'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search_post, name='search.post')
]