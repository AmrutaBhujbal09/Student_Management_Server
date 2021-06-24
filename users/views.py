from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import (GenericAPIView,CreateAPIView,UpdateAPIView,ListAPIView,DestroyAPIView)
from rest_framework.response import Response
from .serializers import (AddStudentSerializer,UpdateStudentSerializer)
from .models import Student
# Create your views here.

class AddStudentAPIView(CreateAPIView):
    serializer_class = AddStudentSerializer

    def post(self, request, *args, **kwargs):
        print("REQUEST DATA",request.data);

        serializer=self.get_serializer(data=request.data)
        #passing request data to serilaizer for validation

        if serializer.is_valid(raise_exception=True):
            #serializer checks requested data is valid or not using is_valid() method .

            serializer.save()
            #save() method is used to insert validated data to the database .

        return Response(serializer.data)



class UpdateStudentAPIView(UpdateAPIView):
    serializer_class = UpdateStudentSerializer

    def get_queryset(self):
        student_id=self.kwargs['pk']
        return Student.objects.filter(id=student_id)

    def patch(self, request, *args, **kwargs):
        instance=self.get_object()

        instance.first_name=request.data["first_name"]
        instance.last_name=request.data["last_name"]
        instance.age=request.data["age"]
        instance.date_of_birth=request.data["date_of_birth"]
        instance.Gender_Choice=request.data["Gender_Choice"]

        serializer=self.get_serializer(instance,data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.partial_update(serializer)

        return Response(serializer.data,status.HTTP_200_OK)



class DeleteStudentAPIView(DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        student_id=self.kwargs["pk"]
        Student.objects.filter(id=student_id).delete()
        return Response(status.HTTP_204_NO_CONTENT)


class GetStudentDetailsView(ListAPIView):
    serializer_class = UpdateStudentSerializer

    def get_queryset(self):
        student_id=self.kwargs["pk"]
        return Student.objects.filter(id=student_id)

    def get(self, request, *args, **kwargs):
        serializer = super().list(request, *args, **kwargs)
        print("seriaizer", request.data)
        return Response(serializer.data, status.HTTP_200_OK)



class GetStudentListAPIView(ListAPIView):
    serializer_class = UpdateStudentSerializer

    def get_queryset(self):
        return Student.objects.filter()

    def get(self, request, *args, **kwargs):
        serializer = super().list(request, *args, **kwargs)
        print("seriaizer", request.data)
        return Response(serializer.data, status.HTTP_200_OK)
