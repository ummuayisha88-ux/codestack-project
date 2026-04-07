from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
      class Meta:
            model = Course
            fields = ['title','description','price','image']

            widgets = {
                    'title': forms.TextInput(attrs={'class': 'form-control'}),
                    'description': forms.Textarea(attrs={'class': 'form-control'}),
                    'price': forms.NumberInput(attrs={'class': 'form-control'}),
                    'image': forms.FileInput(attrs={'class': 'form-control'}),}
            

