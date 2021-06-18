from django import forms
from django.db import models
from django.db.models import fields
from .models import Post
from django.forms import widgets
from django.forms.forms import Form
from django.forms.widgets import Textarea, Widget
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _

class ContactForm(forms.Form):
    user_name=forms.CharField(max_length=100,label="Name",widget=forms.TextInput(attrs={'class':'form-control'}))
    user_email=forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'class':'form-control'}))
    user_address=forms.CharField(max_length=300,label="Address",widget=forms.TextInput(attrs={'class':'form-control'}))
    user_msg=forms.CharField(label='Massage',widget=forms.TextInput(attrs={'class':'form-control'}))

class SignupForm(UserCreationForm):
    password1=forms.CharField(label="Password" ,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=("username","first_name","last_name","email")
        labels={
            'username':"UserName",'first_name':"First Name",'last_name':"Last Name",'email':"Email"}
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'})
        }

class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={"autofocus":True,'class':'form-control'}))
    password=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','desc']
        labels={'title':'Title','desc':'Description'}
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'})

        }