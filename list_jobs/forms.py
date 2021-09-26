from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from django.forms import ModelForm, fields
from .models import Job


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')
      
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None    

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')


class JobForm(ModelForm):
    class Meta:
        model=Job
        exclude=['owner']
    phone = forms.IntegerField(max_value=10000000000)