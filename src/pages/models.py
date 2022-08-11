from django.db import models
from django.conf import settings

# Create your models here.


class Records(models.Model):
    name = models.CharField(max_length=200)
    data = models.TextField(null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Files(models.Model):
    file_name = models.CharField(max_length=200)
    uploaded_file = models.FileField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name
