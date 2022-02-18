from dataclasses import field, fields
from pyclbr import Class
from django import forms
from .models import Project_data, Category, Project_pics, project_comments, Donate_project, Report_project


class Project_Data(forms.ModelForm):
    more_images = forms.FileField(required=False, widget=forms.FileInput(attrs={
        "class": "form-control",
        "multiple": True
    }))

    class Meta:
        model = Project_data

        fields = ('title', 'details', 'category', 'target', 'end_date', 'current_money', 'user', 'img')


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'comment here ...',
        'rows': '4',
    }))

    class Meta:
        model = project_comments
        fields = ('content', 'comment_user')


class Donate(forms.ModelForm):
    value1 = forms.IntegerField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'donate ...',
        'rows': '1',
        'name': 'v'
    }))

    class Meta:
        model = Donate_project
        fields = ('value1', 'user')


class report_project(forms.ModelForm):
    class Meta:
        model = Report_project
        fields = ('user',)
