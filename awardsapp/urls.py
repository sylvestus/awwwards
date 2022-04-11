from unicodedata import name
from django.urls import path
from . import views

from django.conf import settings

urlpatterns = [
    path('',views.landingPage,name='landingPage'),
    path('more/<int:id>',views.more_on_pic,name='more'),
    path('profile/',views.profile,name='profile'),
    path('showProfile',views.profile,name='showProfile'),
    path('showProfile/update/<int:id>',views.uprofile,name='uprofile'),
    path('rate/<int:id>',views.rate,name='rate'),
    path('newpost/',views.new_post,name='new_post'),
    # path('updateProfile/',views.updateProfile,name='updateProfile'),
    path('search/',views.search,name='search'),
    path('api/postapi/', views.PostList.as_view()),
    path('api/profileapi/', views.ProfileList.as_view())


]