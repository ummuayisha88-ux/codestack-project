from django.urls import path
from .views import *
urlpatterns = [
 
 path('register/',registerpage,name='register'),
  path('login/',loginpage,name='login'),
  path('logout/',logoutpage),
]