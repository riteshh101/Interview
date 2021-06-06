from django.db import models

# Create your models here.
class candidate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    password = models.CharField(max_length=2000)

class test_score(models.Model):
    candi = models.OneToOneField(candidate,on_delete=models.CASCADE)
    first_round_score = models.FloatField()
    second_round_score = models.FloatField()
    third_round_score = models.FloatField()


