from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import fileform
from .models import files 
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
	return render(request,'drive/home.html')

def about(request):
	return render(request,'drive/about.html')

def support(request):
	return render(request,'drive/support.html')

def help(request):
	return render(request,'drive/help.html')

@login_required
def my_drive(request):
	form = fileform()
	if request.method == 'POST':
		form = fileform(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		else:
			form = fileform(request.POST, request.FILES)
	return render(request,'drive/my_drive.html', {'form':form})

@login_required
def uploads(request):
	global files
	files = files.objects.all()
	return render(request,'drive/uploads.html',{'files':files})

def delete_file(request, pk):
	if request.method == 'POST':
		global files
		file = files.objects.get(pk=pk)
		file.delete()
	return render(request,'drive/uploads.html')


