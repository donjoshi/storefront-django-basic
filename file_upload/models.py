from django.db import models

# Create your models here.

class File(models.Model):
    pdf=models.FileField(upload_to='pdf/')
    uploaded_at=models.DateTimeField(auto_now_add=True)