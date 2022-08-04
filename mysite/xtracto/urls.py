from django.contrib import admin
from django.urls import include, path, re_path
from .views import index, register_request, login_request, login_request, about, contact, register, login

app_name = "xtracto"


urlpatterns = [
    path("", index, name="home"),
    path("register/", register_request, name="register"),
    path("login/", login_request, name="login"),
    path("logout/", logout_request, name="logout"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("registerfrontend/", register, name="registerfrontend"),
    path("loginfrontend/", login, name="loginfrontend"),
    # path("register/", views.register, name=""),
]
