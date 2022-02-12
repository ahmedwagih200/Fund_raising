from django import forms
from .models import Users


class Register_form(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = '__all__'
        model = Users

