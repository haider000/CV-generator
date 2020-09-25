from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200)
    career_objective =  models.TextField(max_length=2000)
    address =  models.TextField(max_length=2000)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    github = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    other_link = models.CharField(max_length=200)
    achievements =  models.TextField(max_length=2000)
    ug_course_name = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    ug_percentage = models.CharField(max_length=200)
    diploma_or_12th = models.CharField(max_length=200)
    school_12th = models.CharField(max_length=200)
    percentage_12th = models.CharField(max_length=200)
    school_10th = models.CharField(max_length=200)
    percentage_10th = models.CharField(max_length=200)
    work_or_project =  models.TextField(max_length=2000)
    technical_skills =  models.TextField(max_length=2000)
    soft_skills =  models.TextField(max_length=2000)