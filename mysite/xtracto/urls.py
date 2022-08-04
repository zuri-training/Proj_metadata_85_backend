from django.contrib import admin
from django.urls import include, path, re_path
from . import views

app_name = "xtracto"


urlpatterns = [
    path("", views.index, name="home"),
    path("register/", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("registerfrontend/", views.register, name="registerfrontend"),
    path("loginfrontend/", views.login, name="loginfrontend"),
    # path("register/", views.register, name=""),
]
