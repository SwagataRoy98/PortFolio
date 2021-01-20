from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
	path('', views.HomeView,name='home'),
	path('projects',views.ProjectView,name='projects')
]