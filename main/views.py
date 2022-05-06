from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def home(request):
    return render(request, 'main/home.html')


# User Registration
def register(request):
    form = UserCreationForm
    return render(request, 'registration/register.html', {'form': form})
