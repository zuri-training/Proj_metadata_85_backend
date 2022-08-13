from django.contrib import admin
from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views
from . import views
from .views import PasswordsChangeView

app_name = "xtracto"


urlpatterns = [
    path("", views.index, name="home"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("verify/", views.verify, name="verify"),
    path("collections/", views.collections, name="collections"),
    path("collection/", views.collection, name="collection"),
    path("features/", views.features, name="features"),
    path("docs/", views.docs, name="docs"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("faqs/", views.faqs, name="faqs"),
    path("password/", PasswordsChangeView.as_view(
        template_name="xtracto/password_reset_confirm.html")),
        
    # -----metadata urls-----#

    path("download", views.download_csv_data, name="download"),
    path("viewXtracto", views.view_xtracto.as_view(), name="viewXtracto"),
    path("result", views.result, name="result"),
    path("save_metadata", views.save_metadata, name="save_metadata"),
    path("uploaded_records", views.uploaded_records.as_view(), name="uploaded_records"),
    path("metadata_view/<int:pk>", views.metadata_view, name="metadata_view"),
    path("records/<int:pk>", views.records.as_view(), name="records"),
]

# password reset urls
# path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
#     template_name='xtracto/password_reset_done.html'), name='password_reset_done'),
# path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
#     template_name="xtracto/password_reset_confirm.html"), name='password_reset_confirm'),
# path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
#     template_name='xtracto/password_reset_complete.html'), name='password_reset_complete'),
# path("password_reset", views.password_reset_request, name="password_reset"),
