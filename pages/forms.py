from django import forms
from django.core import validators
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()

class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Your name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder": "Your email"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder": "Your Message"}))


    def cleaned_data(self):
        email = self.cleaned_data.get("email")
        return email

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder": "Password"}))


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder": "Your email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder": "Password"}))
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder": "Password Confirm"}))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email already exists")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError("Password must match")
        return data
