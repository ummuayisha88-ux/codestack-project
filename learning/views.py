from django.shortcuts import render, get_object_or_404, redirect
from courses.models import Course
from .models import Note
from enrollments.models import Enrollment
from .models import Assignment, Submission,LiveClass


def learning_dashboard(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if not Enrollment.objects.filter(student=request.user, course=course).exists():
        return redirect('course_detail', id=course.id)

    return render(request, 'learning/dashboard.html', {'course': course})

def notes_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    
    if not Enrollment.objects.filter(student=request.user, course=course).exists():
        return redirect('course_detail', id=course.id)

    notes = Note.objects.filter(course=course)

    return render(request, 'learning/notes.html', {
        'notes': notes,
        'course': course
    })
def assignment_view(request, course_id):
    assignments = Assignment.objects.filter(course_id=course_id)

    
    submitted_ids = Submission.objects.filter(
        student=request.user
    ).values_list('assignment_id', flat=True)

    if request.method == 'POST':
        assignment_id = request.POST.get('assignment_id')
        file = request.FILES.get('file')

        
        if not Submission.objects.filter(
            student=request.user,
            assignment_id=assignment_id
        ).exists():

            Submission.objects.create(
                assignment_id=assignment_id,
                student=request.user,
                file=file
            )

    return render(request, 'learning/assignments.html', {
        'assignments': assignments,
        'submitted_ids': submitted_ids
    })

def live_classes_view(request, course_id):
    classes = LiveClass.objects.filter(course_id=course_id)

    return render(request, 'learning/liveclasses.html', {
        'classes': classes
    })