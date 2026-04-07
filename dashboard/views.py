from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from courses.models import Course
from enrollments.models import Enrollment
from learning.models import Assignment
from payments.models import Payment

User = get_user_model()

def dashboard_view(request):

    if request.user.role == 'student':
        return redirect('my_courses')

    context = {
        'users': User.objects.count(),
        'courses': Course.objects.count(),
        'enrollments': Enrollment.objects.count(),
        'assignments': Assignment.objects.count(),
        'payments': Payment.objects.count(),
    }

    return render(request, 'dashboard/dashboard.html', context)



