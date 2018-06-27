from django import forms

from django.forms import ModelForm
from .models import MyModel
class ArticleForm(ModelForm):
     class Meta:
        model = MyModel
        fields = ['content']


# from ckeditor.fields import RichTextFormField


# class ArticleForm(forms.Form):
#     # content = forms.CharField(label='Your name', max_length=100)
#     content = RichTextFormField()