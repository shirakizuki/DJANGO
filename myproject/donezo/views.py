from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

def landing_page(request):
    return render(request, 'landing_page.html')

def register(request):
    if request.method == 'POST':
        # get all parameters from reqest
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirmPassword']

        # Check password match
        if password1 != password2:
            messages.error(request, "Passwords don't match.")
            return redirect('register')

        # Check username uniqueness
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')
        
        # Check email uniqueness
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return redirect('register')
        
        # Validate password using Django's validators
        try:
            validate_password(password1)
        except ValidationError as e:
            for error in e:
                messages.error(request, error)
            return redirect('register')

        user = User.objects.create_user(username=username, password=password1, email=email, first_name=firstName, last_name=lastName)
        login(request, user)
        return redirect('home')
    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        # get all parameters from reqest
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        # validate if user exists from db
        # if exists redirec to home
        # otherwise throws error
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html', {'user': request.user})  # existing home view, now protected