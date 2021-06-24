from django.conf.urls import url
from .views import (AddStudentAPIView,UpdateStudentAPIView,DeleteStudentAPIView,GetStudentDetailsView,GetStudentListAPIView)

urlpatterns=[

    url('AddStudent',AddStudentAPIView.as_view()),
    url('UpdateStudent/(?P<pk>.+)',UpdateStudentAPIView.as_view()),
    url('DeleteStudent/(?P<pk>.+)',DeleteStudentAPIView.as_view()),
    url('Student detials/',GetStudentDetailsView.as_view()),
    url('GetStudent List',GetStudentListAPIView.as_view())
]