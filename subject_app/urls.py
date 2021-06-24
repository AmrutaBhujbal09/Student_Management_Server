from django.conf.urls import url
from .views import (AddSubjectAPIView,GetSubjectListAPIView,getSubjectDetails)
urlpatterns=[
    url('AddSub',AddSubjectAPIView.as_view()),
    url('Sublist',GetSubjectListAPIView.as_view()),
    url('GetSubD/(?P<pk>.+)',getSubjectDetails.as_view())
]