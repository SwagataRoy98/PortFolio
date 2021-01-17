from django.shortcuts import render
from .models import Project
# Create your views here.
def HomeView(request, *args,**kwargs):
	projects = Project.objects.all()
	return render (request, 'index.html',context={"projects":projects})
