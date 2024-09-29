from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.login_process, name="login"),
    path("logout/", views.logout_process, name="logout"),
    path("register/", views.register, name="register")
]