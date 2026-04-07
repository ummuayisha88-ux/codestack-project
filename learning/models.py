from django.db import models
from courses.models import Course
from django.conf import settings

class Note(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='notes/')

    def __str__(self):
        return self.title

User = settings.AUTH_USER_MODEL

class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    question = models.TextField()
    due_date = models.DateField()

    def __str__(self):
        return self.title


class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='submissions/')

    def __str__(self):
        return f"{self.student} - {self.assignment}"


class LiveClass(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    meet_link = models.URLField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.title

