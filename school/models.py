from django.db import models

class Student(models.Model):
   
    GENDER_CHOICES = [
        ('f', 'Female'),
        ('m', 'Male'),
    ]
   
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.PositiveIntegerField(default=0)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    score = models.FloatField(default=0, null=True)
    class_number = models.PositiveIntegerField(null=True)
    