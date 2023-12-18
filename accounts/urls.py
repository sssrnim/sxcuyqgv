from django.urls import path
from . import views

urlpatterns = [
path('addeducation/',views.addeducation,name='add-education.html'),
path('addexperience/',views.addexperience,name='add-experience.html'),
path('createprofile/',views.createprofile,name='create-profile.html'),
path('dashboard/',views.dashboard,name='dashboard.html'),
path('login/',views.login,name='login.html'),
path('profile/',views.profile,name='profile.html'),
path('profiles/',views.profiles,name='profiles.html'),
path('register/',views.register,name='register.html'),
]