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

# 	ANSWER_CHOICES = (
#     (1, 'Strongly Dislike'),
#     (2, 'Dislike'),
#     (3, 'Unsure'),
#     (4, 'Like'),
#     (5, 'StronglyLike'),
# )

	Question = models.CharField(max_length=300)
	area = models.CharField(max_length=30)
	# answers = max_length=2,
 #        choices=ANSWER_CHOICES,
 #        default=1,


	def __str__(self):
		return self.Question