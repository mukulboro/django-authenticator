from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ExtendedUser

class RegisterForm(UserCreationForm): # Use default django user registration form
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
    """
    Although this form is similar to "Enable2FA" form, it is coded as a seperate form,
    incase future upgrades are required (e.g. if we need to include CAPTCHA)
    """
    code = forms.IntegerField()