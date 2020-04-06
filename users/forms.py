from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm my-4' ,'placeholder':"Username"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm my-4','placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm my-4','placeholder':'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-sm my-4','placeholder':'Email (example@gmail.com)'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm my-4','placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm my-4','placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1',
                  'password2',)
