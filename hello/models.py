from django.db import models

# Create your models here.
class City(models.Model):
	name = models.CharField(max_length=100, blank=True, null=True)
	state = models.CharField(max_length=100, blank=True, null=True)
