from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard_page, name="dashboard"), # Main Dash
    path("login/", views.login_page, name="login"), # Login 
    path("register/", views.register_page, name="regsiter"), # Register
    path("verify-login/", views.verify_login_page, name="verify-login"), # Verify TOTP code
    path("enable-2fa/", views.enable_2fa_page, name="enable-2fa"), # Enable 2FA for users
    path("error/", views.error_page, name="error"), # Generic error page
    path("logout/", views.logout_route, name="logout") # Logout route
]