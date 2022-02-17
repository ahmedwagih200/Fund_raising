from csv import field_size_limit
from pyexpat import model
from urllib import request
from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from .models import Project_data, Project_pics, project_comments, Donate_project
from django.http import HttpResponse
from django.views.generic import View, TemplateView, CreateView, FormView, DetailView, ListView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
from django.db.models import Q
from .models import *
from .forms import *
from users.models import Users


# Create your views here.


def project_list(request):
    Projects = Project_data.objects.all()
    context = {'projects': Projects}
    return render(request, 'projects/list_project.html', context)


def project_details(request, id):
    project_details = get_object_or_404(Project_data, id=id)

    comments = project_details.comments
    comment_form = CommentForm()
    new_comment = None

    context = {'project_details': project_details, 'comment': comments, 'comment_form': CommentForm}
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.project = project_details
            new_comment.save()
            comment_form = CommentForm
    else:
        comment_form = CommentForm()

    return render(request, 'projects/project_details.html', context)


class UserProjectCreateView(CreateView):
    template_name = "projects/form.html"
    form_class = Project_Data
    success_url = reverse_lazy("projects/project_list.html")

    def form_valid(self, form):
        p = form.save()
        images = self.request.FILES.getlist("more_images")
        for i in images:
            Project_pics.objects.create(project=p, image=i)
        return super().form_valid(form)


def donate(request, project_id):
    if request.method == 'POST':
        # d=request.POST.get['dontation_value']
        donating_value = int(request.POST.get('donation_value'))
        project = Project_data.objects.get(id=project_id)
        project.current_money += donating_value
        if project.current_money <= project.target:
            project.save()
            Donate_project.objects.create(
                project=project,
                user=Users.objects.get(id=request.POST['u']),
                value=donating_value
            )
            messages.success(request, 'Your Donation done successfully!')
            return redirect(f"/{project_id}")
        else:
            messages.error(request, 'Your Donation failed')
            return redirect(f"/{project_id}")


def report_project(request, id):
    project_details = get_object_or_404(Project_data, id=id)

    report = project_details.project
    report_form = report_project()
    reportproject = None

    context = {'project_details': project_details, 'report': report, 'report_form': report_project}
    if request.method == 'POST':
        report_form = report_project(data=request.POST)
        if report_form.is_valid():
            reportproject.is_reported = True
            reportproject = report_form.save(commit=False)
            reportproject.project = project_details

            reportproject.save()
            report_form = report_form
    else:
        report_form = report_form()

    return render(request, 'projects/project_details.html', context)
