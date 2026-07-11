from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def login(request):
    return render(request, "registration/login.html")


def logout(request):
    return render(request, "registration/logout.html")


def register(request):
    return render(request, "registration/register.html")


def forgot_password(request):
    return render(request, "registration/forgot_password.html")


def reset_password(request):
    return render(request, "registration/reset_password.html")


def change_password(request):
    return render(request, "registration/change_password.html")


def profile(request):
    return render(request, "registration/profile.html")