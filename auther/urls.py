from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard_page, name="dashboard"),
    path("login/", views.login_page, name="login"),
    path("register/", views.register_page, name="regsiter"),
]