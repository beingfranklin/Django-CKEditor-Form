from django.db import models

# Create your models here.
from ckeditor.fields import RichTextField

# from ckform.models import HTMLField

# class MyModel(models.Model):
#     content = HTMLField()


class MyModel(models.Model):
    content = RichTextField(null=True,blank=True)