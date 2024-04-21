
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,  login as auth_login # Rename the Django login function
from django.contrib.auth import logout as auth_logout

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.

# Views For Home
def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use the renamed Django login function
            messages.success(request, 'You have logged in successfully')
            return redirect('dashboard')
        else:
            messages.error(request, "We couldn't find an account with that username, please try again.")
            return redirect('login_view')
    else:
        return render(request, 'login.html')



def logout(request):
    auth_logout(request)
    messages.success(request, "you've logout successfully")
    return redirect('home')




def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Registration successful. You are now logged in.')
                return redirect('dashboard')  # Redirect to the dashboard after successful registration and login
            else:
                messages.error(request, 'There was an error logging you in. Please try again.')
        else:
            messages.error(request, 'There was an error processing your registration. Please try again.')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})



# Views For Dashboard
def dashboard(request):
    return render(request, 'dashbord/dashboard.html')
