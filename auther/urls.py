from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard_page, name="dashboard"),
    path("login/", views.login_page, name="login"),
    path("register/", views.register_page, name="regsiter"),
    path("verify-login/", views.verify_login_page, name="verify-login"),
    path("enable-2fa/", views.enable_2fa_page, name="enable-2fa"),
    path("error/", views.error_page, name="error"),
    path("logout/", views.logout_route, name="logout")
]