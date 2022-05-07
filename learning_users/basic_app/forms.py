from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfoModel
from django.core import validators



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField()

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfoModel
        fields = ('portfolio_site', 'profile_pic')
