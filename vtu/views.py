from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
# Create your views here.
def home(request):
    
        return render(request, 'home.html')
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have login  successfully')
            return redirect('dashboard')
        else:
            messages.success(request, "we couldn't find an account with that usernam, try again")
            return redirect('login')
    else:
      return render(request, 'login.html')
    
def logout_user(request):
    logout(request)
    messages.success(request, "you've logout successfully")
    return redirect('dashboard')

def register(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully registered!")
            return redirect('dashboard')
        else:
            messages.error(request, "Please enter correct data for registration.")
            # Optionally, you can pass the invalid form back to the template for display.
            return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})

def dashboard(request):
    return render(request, 'dashbord/dashboard.html')