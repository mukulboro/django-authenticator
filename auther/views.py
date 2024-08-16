from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, LoginForm

def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, "login.html", {"form":form})
        uname, pwd = form.cleaned_data["username"], form.cleaned_data["password"]
        user = authenticate(username=uname, password=pwd)
        if user is not None:
            has_2fa = user.has_2fa
            if not has_2fa:
                login(request, user)
                return redirect("/")
            return redirect("/verify-login")
        messages.error(request, "Invalid Credentials")
        return render(request, "login.html", {"form":form})
    else:
        form = LoginForm()
        return render(request, "login.html", {"form":form})

def register_page(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, "register.html", {"form":form})
        form.save()
        messages.success(request, f"User {form.cleaned_data["username"]} added")
        return redirect("/login")
    else:
        form = RegisterForm()
        return render(request, "register.html", {"form":form})

def verify_login_page(request):
    if request.user.is_authenticated:
        return render(request, "verify.html")
    else:
        return redirect("/error")

def dashboard_page(request):
    if request.user.is_authenticated:
        return render(request, "dashboard.html", {"user":request.user})
    else:
        return redirect("/error")

def error_page(request):
    return render(request, "error.html")

