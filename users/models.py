from django.db import models
#from django.contrib.auth.models import AbstractUser
# Create your models here.

class Student(models.Model):
    Gender_Choice=(
        ('FEMALE','FEMALE'),
        ('MALE','MALE')
    )

    first_name=models.CharField(max_length=20,null=False)
    last_name=models.CharField(max_length=20,null=False)
    date_of_birth=models.DateField()
    age=models.IntegerField()
    Gender_Choice=models.CharField(max_length=10,null=True,blank=False,choices=Gender_Choice,default='FEMALE')