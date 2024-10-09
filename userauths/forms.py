from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from userauths.models import User
from django import forms

class UserRegisterForm(UserCreationForm):

    ##FORM FIELDS
    username = forms.CharField(max_length=20,widget=forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"Email"}))
    password1 = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
    password2 = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"}))

    class Meta:
        model = User
        fields = ["email", "username"]


class UserLoginForm(AuthenticationForm):
    ##FORM FIELDS
        username = forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"Email"}))
        password = forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
    
        class Meta:
            model = User
            fields = ["username","password"]
