# basic_api/models.py
from django.db import models

#list
Grade = [
    ('excellent', 5),
    ('average', 4),
    ('bad', 2)
]

# DataFlair
class StudentInfo(models.Model):
    name = models.CharField(max_length = 100)
    firstname= models.CharField(max_length = 100)
    class_student = models.CharField(max_length=3)
    age = models.IntegerField(blank=True)
    uploaded = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(choices = Grade, default = 'average', max_length = 50)

    class Meta:
        ordering = ['uploaded']

    def __str__(self):
        return self.name




class StudentProfile(models.Model):
    name = models.CharField(max_length = 100)
    teacher = models.CharField(max_length = 100)
    uspevaemost = models.CharField(choices = Grade, default = 'average', max_length = 50)
    add_date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to="pictures/" ,blank = True)
   

    class Meta:
        ordering = ['add_date']
    def __str__(self):
        return self.name


