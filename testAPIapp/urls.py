# basic_api/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('info/', views.StudentInfo_API_objects.as_view()),
    path('info/<int:pk>/', views.StudentInfo_API_objects.as_view()),

    path('profile/', views.StudentProfile_API_objects.as_view()),
    path('profile/<int:pk>/', views.StudentProfile_API_objects.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)