from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm, Enable2FAForm, VerifyTOTPForm
from .utils import generate_qr, generate_totp
from .models import ExtendedUser
import json

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
            request.session["verify_email"] = user.email
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
    if request.method == "GET":
        form = VerifyTOTPForm()
        return render(request, "verify.html", {"form":form})
    elif request.method == "POST":
        email = request.session["verify_email"]
        valid_totp = generate_totp(email)
        form = VerifyTOTPForm(request.POST)
        if not form.is_valid():
            return render(request, "verify.html", {"form":form})
        user_totp = int(form.cleaned_data["code"])

        if valid_totp == user_totp:
            user = ExtendedUser.objects.get(email=email)
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Invalid TOTP")
            return render(request, "verify.html", {"form":form})
        return redirect("/")


def dashboard_page(request):
    if request.user.is_authenticated:
        return render(request, "dashboard.html", {"user":request.user})
    else:
        return redirect("/error")

def enable_2fa_page(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            qr, token = generate_qr(request.user.email)
            form = Enable2FAForm()
            return render(request, "enable_2fa.html", {"user":request.user, "qr":qr, "token":token, "form":form})
        elif request.method == "POST":
            valid_totp = generate_totp(request.user.email) # Generating ASAP to reduce time conflicts
            form = Enable2FAForm(request.POST)
            if not form.is_valid():
                return render(request, "enable_2fa.html", {"user":request.user, "qr":qr, "token":token, "form":form})
            user_totp = int(form.cleaned_data["code"])

            if not valid_totp == user_totp:
                qr, token = generate_qr(request.user.email)
                messages.error(request, "Invalid TOTP provided")
                return render(request, "enable_2fa.html", {"user":request.user, "qr":qr, "token":token, "form":form})
            user_model = ExtendedUser.objects.get(pk=request.user.id)
            user_model.has_2fa = True
            user_model.save()
            messages.success(request, "Enabled 2FA")
            return redirect("/")

    else:
        return redirect("/error")

def error_page(request):
    return render(request, "error.html")

def logout_route(request):
    logout(request)
    messages.success(request, "Logged Out")
    return redirect("/login")

