from django.urls import path
from .views import *
urlpatterns = [
    path('',homepage,name='home'),
    path('create/',create_course,name ='create_course'),
    path('list/',course_list,name = 'course_list'),
    path('course/<int:id>/',course_detail,name ='course_details'),
    path('update/<int:id>/',update_course, name='update_course'),
    path('delete/<int:id>/',delete_course, name='delete_course'),
    path('my-courses/',my_courses, name='my_courses'),
    
]