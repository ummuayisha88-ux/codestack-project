from django.shortcuts import render, get_object_or_404, redirect
from .models import Payment
from courses.models import Course
from django.contrib import messages
from enrollments.models import Enrollment
from django.contrib.auth.decorators import login_required

@login_required
def make_payment(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    
    already_paid = Payment.objects.filter(
        student=request.user,
        course=course
    ).exists()

    
    already_enrolled = Enrollment.objects.filter(
        student=request.user,
        course=course
    ).exists()

    
    if already_enrolled:
        messages.info(request, "You are already enrolled!")
        return redirect('course_details', id=course.id)

    if request.method == 'POST':

        
        if not already_paid:

            
            Payment.objects.create(
                student=request.user,
                course=course,
                amount=course.price
            )

            
            Enrollment.objects.get_or_create(
                student=request.user,
                course=course
            )

            messages.success(request, "Payment Successful! 🎉")

        else:
            messages.info(request, "You already purchased this course!")

        return redirect('my_courses')

    return render(request, 'payments/payment.html', {
        'course': course,
        'already_paid': already_paid
    })

    

