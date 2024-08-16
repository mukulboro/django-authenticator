from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ExtendedUser

class RegisterForm(UserCreationForm): # Use default django user model
    email = forms.EmailField()

    class Meta:
        model = ExtendedUser
        fields = ["username", "email", "password1", "password2"]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class Enable2FAForm(forms.Form):
    code = forms.IntegerField()

class VerifyTOTPForm(forms.Form):
    code = forms.IntegerField()