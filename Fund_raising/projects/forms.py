from dataclasses import field, fields
from pyclbr import Class
from django import forms
from .models import Project_data, Category, Project_pics, project_comments, Donate_project, Report_project, Rate_project


class Project_Data(forms.ModelForm):
    more_images = forms.FileField(required=False, widget=forms.FileInput(attrs={
        "class": "form-control",
        "multiple": True
    }))

    class Meta:
        model = Project_data

        fields = ('title', 'details', 'category', 'target', 'end_date', 'img', 'tags')


class CommentForm(forms.ModelForm):
    class Meta:
        model = project_comments
        fields = ('comment',)




