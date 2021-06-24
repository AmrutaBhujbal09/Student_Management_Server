from rest_framework import serializers
from .models import Student

class AddStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=["first_name","last_name","date_of_birth","age","Gender_Choice","id"]
        """reate(self,validated_data):
            studentval=User.objects.create_user(
                first_name=validated_data.pop('first_name'),
                last_name=validated_data.pop('last_name'),
                date_of_birth=validated_data.pop('date_of_birth'),
                age=validated_data.pop('age'),
                Gender_Choice=validated_data.pop('Gender_Choice')
            )
            return studentval
"""


class UpdateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=["id","first_name","last_name","date_of_birth","age","Gender_Choice"]





