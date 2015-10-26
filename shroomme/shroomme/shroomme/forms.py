from django import forms
from django.contrib.auth.models import User

class NameForm(forms.Form):
	name = forms.CharField(label='', max_length=100)


class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'Email', 'class': 'form-control'}),
        required = True)
    password = forms.CharField(
        widget = forms.PasswordInput(attrs = {'placeholder': 'Password', 'class': 'form-control'}),
        required = True)



class SignUpForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'Email'}),
        required = True)
    # email = forms.EmailField(
    #     widget = forms.TextInput(attrs = {'placeholder': 'email'}),
    #     required = True)
    password = forms.CharField(
        widget = forms.PasswordInput(attrs = {'placeholder': 'password'}),
        required = True)