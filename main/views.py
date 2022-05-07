from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from main.forms import RegisterUserForm
# Create your views here.


# Login decorator will check if user is not logged in will redirect user to login page
@login_required(login_url='login')
def home(request):
    return render(request, 'main/home.html')


# Login function
def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'main/login_register.html', {'page': page})


# Logout - simply logs out user)
def logoutUSer(request):
    logout(request)
    return redirect('login')


# Checks if user is not registered saving user to our Database
def registerUser(request):
    page = 'register'
    form = RegisterUserForm()

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate(request, username=user.username,
                                password=request.POST['password1'])

            if user is not None:
                login(request, user)
                return redirect('home')

    context = {"form": form}
    return render(request, 'main/login_register.html', context)
