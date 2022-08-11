from django.contrib import admin
from django.urls import include, path, re_path
from . import views
from .views import *

app_name = "xtracto"


urlpatterns = [
    path("", views.index, name="home"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("collections/", views.collections, name="collections"),
    path("features/", views.features, name="features"),
    path("docs/", views.docs, name="docs"),
    path("faqs/", views.faqs, name="faqs"),
    path("pwdreset/", views.pwdreset, name="pwdreset"),
    path("verify/", views.verify, name="verify"),
    path("download", views.download_csv_data, name="download"),
    path("viewXtracto", views.view_xtracto.as_view(), name="viewXtracto"),
    path("result", views.result, name="result"),
    path("save_metadata", views.save_metadata, name="save_metadata"),
    path("uploaded_records", views.uploaded_records.as_view(), name="uploaded_records"),
    path("metadata_view/<int:pk>", views.metadata_view, name="metadata_view"),
    path("records/<int:pk>", views.records.as_view(), name="records"),
]
