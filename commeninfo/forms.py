from django import forms
from django.forms import ModelForm
from .models import UserInfo
from django.contrib.admin import widgets


# Create a UserInfo form
class UserInfoAddForm(ModelForm):
    class Meta:
        def clean(self):
            cleaned_data = super(ModelForm, self).clean()
            # additional cleaning here
            return cleaned_data
        model = UserInfo
        fields = ('username', 'email', 'password', 'password_re_type', 'first_name', 'last_name', 'uniqueID', 'date_of_birth',)
        #
        labels = {
            'username': 'Username',
            'email': 'Email',
            'password': 'Password',
            'password_re_type': 'Password (Re-Type)',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'uniqueID': 'UniqueID',      
            'date_of_birth': 'Date of Birth (Month/Day/Year)',
        }
        #
        widgets = {
            'username': forms.TextInput(attrs={'class': 'from-control', 'placeholder': 'username'}),
            'email': forms.EmailInput(attrs={'class': 'from-control', 'placeholder': 'email'}),
            'password': forms.PasswordInput(attrs={'class': 'from-control', 'placeholder': 'password'}),
            'password_re_type': forms.PasswordInput(attrs={'class': 'from-control', 'placeholder': 'password_re_type'}),
            'first_name': forms.TextInput(attrs={'class': 'from-control', 'placeholder': 'first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'from-control', 'placeholder': 'last_name'}),
            'uniqueID': forms.NumberInput(attrs={'class': 'from-control', 'placeholder': 'uniqueID'}),
            'date_of_birth': forms.SelectDateWidget(years = range(2022, 1930, -1))#
        }
