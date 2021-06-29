from django.shortcuts import render
from rest_framework.generics import (GenericAPIView,DestroyAPIView,CreateAPIView,ListAPIView,UpdateAPIView)
from rest_framework.response import Response
from.models import Subject
from users.models import Student
from rest_framework import status

from .serializers import (AddSubjectSerializer)
# Create your views here.

class AddSubjectAPIView(CreateAPIView):
    serializer_class = AddSubjectSerializer
    def post(self, request, *args, **kwargs):
        print("REQUEST DATA",request.data)
        serializer=self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)






class GetSubjectListAPIView(ListAPIView):
    serializer_class = AddSubjectSerializer

    def get_queryset(self):
        return Subject.objects.filter()

    def get(self, request, *args, **kwargs):
        serializer = super().list(request, *args, **kwargs)
        print("seriaizer", request.data)
        return Response(serializer.data, status.HTTP_200_OK)




class getSubjectDetails(ListAPIView):
    serializer_class = AddSubjectSerializer

    def get_queryset(self):
        return Subject.objects.filter()

    def get(self, request, *args, **kwargs):
        data=list()
        subject_id=self.kwargs["pk"]
        sub_data=Subject.objects.filter(id=subject_id)

        serializer =self.get_serializer(sub_data,many=True)

        for subject_app in serializer.data:
            get_student=Student.objects.filter(id=subject_app["student_id"]).values("first_name","last_name","age","date_of_birth","Gender_Choice","id")
            print("Student Details",get_student)
            data.append({
                "id":subject_app["id"],
                "subject_name":subject_app["subject_name"],
                "marks":subject_app["marks"],
                "first_name":get_student[0]["first_name"],
                "last_name": get_student[0]["last_name"],
                "age":get_student[0]["age"],
                "date_of_birth":get_student[0]["date_of_birth"],
                "Gender_Choice":get_student[0]["Gender_Choice"],
                "student_id":get_student[0]["id"]
            })

        return Response(data, status.HTTP_200_OK)



class getStudentDetails(ListAPIView):
    serializer_class = AddSubjectSerializer

    def get_queryset(self):
        get_student_id=self.kwargs["pk"]
        student_data=Subject.objects.filter(student_id=get_student_id)
        return student_data


    def get(self, request, *args, **kwargs):
        data=list()
        get_student_id=self.kwargs["pk"]
        student_data = Subject.objects.filter(student_id=get_student_id)
        serializer=self.get_serializer(student_data,many=True)

        for subject_app in serializer.data:
            get_student=Student.objects.filter(id=subject_app["student_id"]).values("first_name","last_name","age","date_of_birth","Gender_Choice","id")
            print("Student Details",get_student)

            data.append({
                #"id": subject_app["id"],
                "subject_name": subject_app["subject_name"],
                "marks": subject_app["marks"],
                #"age": get_student[0]["age"],
		"first_name":get_student[0]["first_name"],
		"last_name":get_student[0]["last_name"],
                #"date_of_birth": get_student[0]["date_of_birth"],
                #"Gender_Choice": get_student[0]["Gender_Choice"],
                "id": get_student[0]["id"]
            })

        return Response(data, status.HTTP_200_OK)



