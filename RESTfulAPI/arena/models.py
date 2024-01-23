from django.db import models

# Create your models here.
class Teacher(models.Model):
    
    techer_name = models.CharField(max_length = 30)
    course_name = models.CharField(max_length = 30)
    course_duration = models.IntegerField()
    