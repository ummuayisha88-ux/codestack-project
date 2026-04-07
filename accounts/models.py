from django.db import models
from django.contrib.auth.models import AbstractUser

class UserAccount(AbstractUser):
      Role_choices = (
        ('admin','Admin'),
        ('instructor','Instructor'),
        ('student','Student'),
        )

      role = models.CharField(max_length=20, choices = Role_choices, default = 'student')


