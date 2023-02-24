from django.db import models

# Create your models here.
class student(models.Model):
    studentname = models.CharField(max_length=50)
    studentmothername = models.CharField(max_length=30)
    studentfathername = models.CharField(max_length=30)
    studentclass = models.IntegerField()
    studentage = models.IntegerField()
    studentmobilenumber = models.IntegerField()
    studentvillage = models.CharField(max_length=30)
