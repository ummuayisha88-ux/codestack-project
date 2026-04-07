from django.urls import path
from .views import *


urlpatterns=[
    path('learning/<int:course_id>/',learning_dashboard,name='learning_dashboard'),
    path('notes/<int:course_id>/', notes_view, name='notes'),
    path('assignments/<int:course_id>/',assignment_view, name='assignments'),
    path('live/<int:course_id>/',live_classes_view, name='live_classes'),
]