from django import forms

class NameForm(forms.Form):
	name = forms.CharField(label='', max_length=100)


class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'username'}),
        required = True)
    password = forms.CharField(
        widget = forms.PasswordInput(attrs = {'placeholder': 'password'}),
        required = True)



class SignUpForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'username'}),
        required = True)
    email = forms.EmailField(
        widget = forms.TextInput(attrs = {'placeholder': 'email'}),
        required = True)
    password = forms.CharField(
        widget = forms.PasswordInput(attrs = {'placeholder': 'password'}),
        required = True)