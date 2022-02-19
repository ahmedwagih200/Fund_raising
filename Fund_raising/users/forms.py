from django import forms
from .models import Users


class Register_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'phone', 'image', 'email', 'password']


class Update_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'phone', 'password', 'birth_date', 'facebook_profile', 'country', 'image']


