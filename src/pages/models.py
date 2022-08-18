from django.db import models
from django.conf import settings

# Create your models here.

class verify_email(models.Model):
    email =models.EmailField(max_length=200)
    code = models.TextField()
    verifiedBool = models.BooleanField()
    def __str__(self):
        return self.email

class Records(models.Model):
    name = models.CharField(max_length=200)
    data = models.TextField(null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    Phone_no = models.CharField(max_length=20)
    Country = models.TextField(null=True)
    full_name = models.CharField(max_length=200)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    no_of_downloads = models.PositiveSmallIntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.full_name


class Files(models.Model):
    file_name = models.CharField(max_length=200)
    uploaded_file = models.FileField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name


class fileUpload(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to="media/store/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
