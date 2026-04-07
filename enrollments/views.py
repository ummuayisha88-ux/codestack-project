from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from courses.models import Course
from .models import Enrollment
from django.contrib import messages

  
def enroll(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    obj, created = Enrollment.objects.get_or_create(
        student=request.user,
        course=course
    )

    if created:
        messages.success(request, "Successfully enrolled!")
    else:
        messages.info(request, "Already enrolled!")

    return redirect('course_details', id=course.id)
