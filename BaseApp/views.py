from django.shortcuts import render,redirect
from .models import Project
# Create your views here.
def HomeView(request, *args,**kwargs):
	projects = Project.objects.all()
	return render (request, 'index.html',context={"projects":projects})
def To_Projects(request, *args):
	return redirect('/projects')
def ProjectView(request, *args):
	projects = Project.objects.all()
	return render(request,'Projects.html',context={"projects":projects})
