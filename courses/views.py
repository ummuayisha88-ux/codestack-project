from django.shortcuts import render,redirect,get_object_or_404
from .models import Course
from .forms import CourseForm 
from django.contrib.auth.decorators import login_required
from enrollments.models import Enrollment



def homepage(request):
    courses = Course.objects.all()[:4] 
    return render(request,'home.html',{'courses':courses}) 

@login_required
def create_course(request):

    if request.user.role not in ['admin', 'instructor']:
        return redirect('home')   

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)

        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user
            course.save()
            return redirect('home')

    else:
        form = CourseForm()

    return render(request, 'course/create_course.html', {'form': form})


def course_list(request):
     course = Course.objects.all()
     return render(request,'course/course_list.html',{'course':course})
    

def course_detail(request, id):
    course = get_object_or_404(Course, id=id)

    is_enrolled = False
    if request.user.is_authenticated:
        is_enrolled = Enrollment.objects.filter(
            student=request.user,
            course=course
        ).exists()

    return render(request, 'course/course_details.html', {
        'course': course,
        'is_enrolled': is_enrolled
    })
@login_required
def update_course(request, id):

    course = get_object_or_404(Course, id=id)

    
    if request.user != course.instructor and request.user.role != 'admin':
        return redirect('home')

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)

        if form.is_valid():
            form.save()
            return redirect('course_list')

    else:
        form = CourseForm(instance=course)

    return render(request, 'course/create_course.html', {'form': form})

@login_required
def delete_course(request, id):

    course = get_object_or_404(Course, id=id)
    if request.user != course.instructor and request.user.role != 'admin':
        return redirect('home')

    course.delete()
    return redirect('course_list')

def my_courses(request):
    enrollments = Enrollment.objects.filter(student=request.user)

    return render(request, 'course/my_courses.html', {
        'enrollments': enrollments
    })


