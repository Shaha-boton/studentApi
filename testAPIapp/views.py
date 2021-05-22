from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *



class StudentInfo_API_objects(generics.ListCreateAPIView):
    queryset = StudentInfo.objects.all()
    serializer_class = StudentInfoSerializer
class StudentInfo_API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentInfo.objects.all()
    serializer_class = StudentInfoSerializer



class StudentProfile_API_objects(generics.ListCreateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
class StudentProfile_API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer