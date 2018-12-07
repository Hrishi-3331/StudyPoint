from django.contrib.auth.models import User
from django import forms


class SignupForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'custom-form-input'}))
    idnumber = forms.FloatField(max_value=23000, min_value=20000, widget=forms.TextInput(attrs={'class': 'custom-form-input'}))
    username = forms.CharField(widget= forms.TextInput(attrs={'class': 'custom-form-input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'custom-form-input'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'idnumber', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'custom-form-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'custom-form-input'}))
