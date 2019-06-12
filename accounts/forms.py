from django import forms

class UserLoginForm(forms.Form):
    """From to be used to log in"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)