from django.db import models
from users.models import Student

# Create your models here.
class Subject(models.Model):
    subject_name=models.CharField(max_length=20,null=False)
    marks=models.IntegerField(null=False)
    student_id=models.ForeignKey(Student,null=False,blank=False,on_delete=models.DO_NOTHING)