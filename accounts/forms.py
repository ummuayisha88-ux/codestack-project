from django.contrib.auth.forms import UserCreationForm
from .models import UserAccount

class RegisterForm(UserCreationForm):
      class Meta:
            model = UserAccount
            fields = [ 'username','email','password1','password2','role']
            
      def save(self, commit=True):
                user = super().save(commit=False)
                user.email = self.cleaned_data.get('email')
                user.role = self.cleaned_data.get('role')   
                if commit:
                   user.save()
                return user