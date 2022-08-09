from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

# <<<<<<< HEAD
# <<<<<<< HEAD
# =======
# from django import forms
# =======
# from django import forms


# Registration form
class Registrationform(forms.Form, forms.ModelForm):
    username = forms.EmailField(
        label="Email Address",
        required=True,
        widget=forms.TextInput(attrs={"id": "email"}),
    )
    password = forms.CharField(
        label="Password",
        max_length=200,
        widget=forms.PasswordInput(attrs={"id": "password"}),
    )

    class Meta:
        model = User
        fields = ("username", "password")


# Registration form
class Registrationform(forms.Form, forms.ModelForm):
    username = forms.EmailField(
        label="Email Address",
        required=True,
        widget=forms.TextInput(attrs={"id": "email"}),
    )
    password = forms.CharField(
        label="Password",
        max_length=200,
        widget=forms.PasswordInput(attrs={"id": "password"}),
    )

    class Meta:
        model = User
        fields = ("username", "password")


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label="email", widget=forms.TextInput(attrs={"id": "email"})
    )
    password = forms.CharField(
        label="password",
        max_length=200,
        widget=forms.TextInput(attrs={"id": "password"}),
    )


# -------metadata form----#
class FileUpload(forms.Form):
    upload_file = forms.FileField()
