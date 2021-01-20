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
class Education(models.Model):
	level = models.CharField(max_length=30)
	institute = models.CharField(max_length = 200)
	start_date = models.DateField()
	end_date = models.DateField()
	stream = models.CharField(max_length=200)
	grade = models.DecimalField(max_digits=5,decimal_places=2)
	def __str__(self):
		return f'{self.level}'
class Certificate(models.Model):
	name = models.CharField(max_length=350)
	start_date = models.DateField()
	end_date = models.DateField()
	description = models.TextField()
	verification_link = models.CharField(max_length=300,blank=True)
	def __str__(self):
		return f'{self.name}'