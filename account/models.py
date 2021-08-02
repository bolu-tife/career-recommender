from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class student(models.Model):
	name = models.CharField(max_length=30)
	# first_name = models.CharField(max_length=30, null=True)
	# last_name = = models.CharField(max_length=True)
	Identification_no = models.ForeignKey(User, on_delete = models.CASCADE, null=False)
	email = models.CharField(max_length=30)
	# profile_pic = models.ImageField(null=True)

	def __str__(self):
		return self.name