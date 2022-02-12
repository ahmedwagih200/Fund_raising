from dataclasses import field, fields
from pyclbr import Class
from django import forms
from .models import Project_data , Category
class Project_Data(forms.ModelForm):
    class Meta:
        model = Project_data
        fields = ('title', 'details','category','target','end_date')
