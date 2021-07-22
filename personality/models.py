from django.db import models
from account.models import student
# Create your models here.

class User_Personality(models.Model):
    Realistic = models.FloatField()
    Investigative = models.FloatField()
    Artistic = models.FloatField()
    Social = models.FloatField()
    Enterprising = models.FloatField()
    Conventional = models.FloatField()
    user_id = models.ForeignKey(student, on_delete=models.CASCADE, null=False)

class Questions(models.Model):


	Question = models.CharField(max_length=300)
	area = models.CharField(max_length=30)
	

	def __str__(self):
		return self.Question