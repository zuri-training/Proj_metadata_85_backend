from django.db import models

# Create your models here.
class fileUpload(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='media/store/')
    uploaded_at = models.DateTimeField(auto_now_add=True)