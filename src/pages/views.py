from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import Registered
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


from django.http import HttpResponse
from django.utils.encoding import smart_str

# -----Packages for extracting metadata-----
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from tinytag import TinyTag
import csv

# from metadata.models import Contact
from django.http import HttpResponseRedirect

import xtracto

from .forms import FileUpload
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User, auth







def index(request):
    return render(request, "xtracto/home.html")


def about(request):
    return render(request, "xtracto/About-us.html")


def contact(request):
    return render(request, "xtracto/contact.html")


# def register(request):
#     if request.method == "POST":
#         if request.POST.get("email") and request.POST.get("password"):
#             post = Registered()
#             post.email = request.POST.get("email")
#             post.password = request.POST.get("password")
#             post.save()
#             # mydictionary= {}
#             # mydictionary['SuccessMsg'] = 'Form Submitted: You can now login'
#             messages.success(request, "You nhave been succefully registered")
#             return render(
#                 request,
#                 "xtracto/login.html",
#             )
#         else:
#             return render(request, "xtracto/register.html")

#     else:
#         return render(request, "xtracto/register.html")


# def login(request):
#     if request.method == "POST":
#         if request.POST.get("email") and request.POST.get("password"):
#             email = request.POST["email"]
#             password = request.POST["password"]

#             user = authenticate(email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 email = user.email
#                 return render(request, "xtracto/dashboard.html", {"email": email})
#             else:
#                 messages.error(request, "Invalid details")
#     return render(request, "xtracto/login.html")

def faqs(request):
    return render(request, "xtracto/faqs.html")

def pwdreset(request):
    return render(request, "xtracto/pwdreset.html")

def verify(request):
    return render(request, "xtracto/verify.html")

def docs(request):
    return render(request, "xtracto/docs.html")

def dashboard(request):
    return render(request, "xtracto/dashboard.html")


def collections(request):
    return render(request, "xtracto/collections.html")


def features(request):
    return render(request, "xtracto/features.html")


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("xtracto:login")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="xtracto/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("xtracto:dashboard")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="xtracto/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("xtracto:home")





# ------Metadata-------#
class view_xtracto(View):
    success_url = reverse_lazy("xtracto:viewXtracto")
    template_name = "upload.html"

    def post(self, request):
        form = FileUpload(request.POST, request.FILES)
        context = {"xtracto": []}
        if form.is_valid():

            uploaded_file = request.FILES["upload_file"]
            file_type = uploaded_file.content_type.split("/")

            context["xtracto"].append(
                {"label_name": "File Name", "label_value": uploaded_file.name}
            )
            context["xtracto"].append(
                {"label_name": "Mime Type", "label_value": uploaded_file.content_type}
            )
            context["xtracto"].append(
                {"label_name": "File Size", "label_value": uploaded_file.size}
            )
            context["xtracto"].append(
                {"label_name": "File Type", "label_value": file_type[0].capitalize()}
            )

            if (
                file_type[0] == "video"
                or file_type[0] == "image"
                or file_type[0] == "audio"
            ):

                parser = createParser(uploaded_file)
                xtracto = extractMetadata(parser)

                context["file_name"] = uploaded_file.name
                context["file_size"] = uploaded_file.size
                context["file_type"] = file_type[0].capitalize()
                context["mime_type"] = uploaded_file.content_type

                for line in enumerate(xtracto.exportPlaintext()):
                    if line[0] != 0:
                        label = line[1].split(":")
                        label_name = label[0][1:].split()
                        label_value = label[1][:]

                        if len(label_name) > 1:
                            label_name = f"{label_name[0]}_{label_name[1]}"
                        else:
                            label_name = label_name[0]

                        context["xtracto"].append(
                            {"label_name": label_name, "label_value": label_value}
                        )

            request.session["xtracto"] = context
            return redirect("xtracto:result")
        return render(request, self.template_name, {"form": form})

    def get(self, request):
        form = FileUpload()
        return render(request, self.template_name, {"form": form})


# ---------------------------------#


def result(request):
    xtracto = request.session.get("xtracto")
    context = xtracto
    return render(request, "result.html", context)


# ---------------------------------------------#


def download_csv_data(request):
    #  content type
    xtracto = request.session.get("xtracto")
    metadata_label = list(xtracto.keys())[1:]

    response = HttpResponse(content_type="text/csv")
    # file name
    response["Content-Disposition"] = "attachment; filename= label_value.csv"
    # ' "download.csv" '

    writer = csv.writer(response, csv.excel)
    response.write("\ufeff".encode("utf8"))

    metadata_label_name = []
    metadata_label_value = []

    for metadata_val in xtracto["xtracto"]:
        metadata_label_name.append(smart_str(metadata_val["label_name"]))
        metadata_label_value.append(smart_str(metadata_val["label_value"]))

    writer.writerow(metadata_label_name)
    writer.writerow(metadata_label_value)

    return response


# saving the extracted metadata
# still working on this code
# ---------------------------
# def saveMeta(request):
#     template = "save.html"
#     form = saveMetada(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect("/")
#     context = {"form": form}
#     return render(request, template, context)




