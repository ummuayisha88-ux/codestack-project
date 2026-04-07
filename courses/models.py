from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
import re 

def validate_capital(value):
    if not value[0].isupper():
        raise ValidationError("First letter must be capital")

def validate_symbol(value):
    if not re.match(r'^[A-Za-z0-9 ]+$', value):
        raise ValidationError("Symbols are not allowed")

def validate_price(value):
    if value < 10:
        raise ValidationError("Price must be at least 10")

User = settings.AUTH_USER_MODEL

class Course(models.Model):
      title = models.CharField(max_length = 200,validators=[validate_capital,validate_symbol])
      description = models.TextField()
      price = models.DecimalField(max_digits = 8,decimal_places = 2,validators=[validate_price])
      instructor = models.ForeignKey(User,on_delete = models.CASCADE,related_name ='courses')
      image = models.ImageField(upload_to='courses/',null = True,blank = True)
      created_at = models.DateTimeField(auto_now_add = True)


      def __str__(self):
          return self.title




