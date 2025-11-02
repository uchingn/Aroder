from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.
class Qrcode(models.Model):
    mobile_number=models.CharField(max_length=10)
    data=models.CharField(max_length=255)
    
    
class Post(models.Model):
    
    title =models.CharField(max_length=255)
    content=CKEditor5Field(config_name='extends')