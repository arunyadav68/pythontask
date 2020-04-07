from django.db import models

# Create your models here.
class movie(models.Model):
	name = models.CharField(max_length=100, blank=False)
	location = models.CharField(max_length=100,blank=False)
	timing = models.CharField(max_length=250,blank=False)