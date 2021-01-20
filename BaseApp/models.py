from django.db import models

# Create your models here.

class Project(models.Model):
	project_name = models.CharField(max_length=50)
	project_desc = models.TextField()
	github_link = models.CharField(max_length=250,null=True,blank=True)
	demo_file = models.FileField(upload_to='demos',null=True,blank=True)
	live_url = models.CharField(max_length=250,blank=True)
	def __str__(self):
		return f'{self.project_name}'
