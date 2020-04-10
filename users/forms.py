from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User

passMessage= """
<ul>
<li><small>password must contain a symbol $,%,@ etc</small> </li>
<li><small>password must contain a number 0-9 </small> </li>
<li><small>password must contain a upper case alphabet A-Z</small> </li>
<li><small>password must contain a lower case alphabet a-z</small> </li>

</ul>
"""
class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-sm my-4','placeholder':'Email (example@gmail.com)'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm my-4','placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-sm my-4','placeholder':'Last Name'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm my-4','placeholder':'Password' ,"data-toggle":"tooltip" ,"data-placement":"left", "data-html":"true", "title":""," data-original-title":passMessage}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-sm my-4','placeholder':'Confirm Password'}))
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2',)
