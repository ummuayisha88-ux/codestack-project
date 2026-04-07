from django.urls import path
from .views import *

urlpatterns = [
    path('pay/<int:course_id>/', make_payment, name='payment'),
]