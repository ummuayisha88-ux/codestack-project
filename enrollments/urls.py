from django.urls import path
from .views import *

urlpatterns = [
    path('enroll/<int:course_id>/',enroll, name='enroll_course'),
]