from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse
from .forms import ArticleForm

def index(request):
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()
			context = {'form': form}
			return redirect('index')
		else:
			context = {'form': ArticleForm()}
			return render(request, 'index.html', context)
	else:
		context = {'form': ArticleForm()}
		return render(request,'index.html',context)