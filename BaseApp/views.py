from django.shortcuts import render,redirect
from .models import Project,Education,Certificate
# Create your views here.
def HomeView(request, *args,**kwargs):
	educations = Education.objects.all()
	certificates = Certificate.objects.all()
	return render (request, 'index.html',context={"educations":educations,
												"certificates":certificates})
def ProjectView(request, *args):
	projects = Project.objects.all()
	return render(request,'Projects.html',context={"projects":projects})
