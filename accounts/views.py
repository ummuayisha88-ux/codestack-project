from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


   
def registerpage(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                messages.success(request, "Registered successfully!")
                return redirect('login')
            except Exception as e:
                print("SAVE ERROR:", e)   
        else:
            print("FORM ERRORS:", form.errors)  
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('course_list')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        if user:
            login(request,user)
            messages.success(request,'User logged in successfully')
            return redirect('course_list')
        else:
            messages.error(request,'invalid credentials')
            return redirect('login')
    return render(request,'accounts/login.html')

def logoutpage(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('home')

    
