from django.db import models

# Create your models here.


class phySemSubject(models.Model):
    subject_name = models.CharField(max_length=100)
    credits = models.CharField(max_length=10)
    difficulty = models.CharField(max_length=50)
    syllabus = models.CharField(max_length=100)
    image = models.FileField(null=True)
    link = models.CharField(default='#', max_length=100)

    def __str__(self):
        return self.subject_name


class chemSemSubject(models.Model):
    subject_name = models.CharField(max_length=100)
    credits = models.CharField(max_length=10)
    difficulty = models.CharField(max_length=50)
    syllabus = models.CharField(max_length=100)
    image = models.FileField(null=True)
    link = models.CharField(default='#', max_length=100)

    def __str__(self):
        return self.subject_name