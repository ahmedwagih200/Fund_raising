from django import forms
from .models import Users


class Register_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'phone', 'image', 'email', 'password']

    def clean(self):
        cleaned_data = super(Register_form, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        print(password)
        print(confirm_password)
        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )


class Update_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'phone', 'password', 'birth_date', 'facebook_profile', 'country', 'image']
