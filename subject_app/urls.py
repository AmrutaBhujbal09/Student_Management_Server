from django.conf.urls import url
from .views import (AddSubjectAPIView,GetSubjectListAPIView,getSubjectDetails,getStudentDetails)
urlpatterns=[
    url('AddSub',AddSubjectAPIView.as_view()),
    url('Sublist',GetSubjectListAPIView.as_view()),
    url('GetSubD/(?P<pk>.+)',getSubjectDetails.as_view()),
    url('getStudentDetails/(?P<pk>.+)',getStudentDetails.as_view())
]