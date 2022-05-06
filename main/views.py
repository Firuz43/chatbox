from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.


def home(request):
    return render(request, 'main/home.html')


# User Registration
def signUp(request):
    if request.method == 'post':
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})
