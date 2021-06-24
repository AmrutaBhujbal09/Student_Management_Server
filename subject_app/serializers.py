from rest_framework import serializers
from .models import Subject

class AddSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields=["id","subject_name","marks","student_id"]