from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }
    ), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }
    ), required=True)


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control my-3',
        'placeholder': 'Username *'
    }
    ), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control my-3',
        'placeholder': 'Email'
    }
    ), required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control my-3',
        'placeholder': 'Full Name *'
    }
    ), required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control my-3',
        'placeholder': 'Password *'
    }
    ), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control my-3',
        'placeholder': 'Confirm Password *'
    }
    ), required=True)

    class Meta:
        model = User
        fields = ("username","first_name","email")
