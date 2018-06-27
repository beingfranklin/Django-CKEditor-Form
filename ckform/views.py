from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .forms import ArticleForm

def index(request):
	context = {'form': ArticleForm()}
	return render(request,'index.html',context)