from audioop import avg
from csv import field_size_limit
from pyexpat import model
from urllib import request
from django.shortcuts import get_object_or_404, render, redirect
from .forms import *
from .models import Project_data, Project_pics, project_comments, Donate_project, Report_project, Rate_project
from django.http import HttpResponse
from django.views.generic import View, TemplateView, CreateView, FormView, DetailView, ListView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator
from django.contrib import messages

from django.http import JsonResponse
from django.conf import settings
from django.db.models import Avg
from .models import *
from .forms import *
from users.models import Users


# Create your views here.


def project_list(request, id):
    user = Users.objects.get(id=id)
    Projects = Project_data.objects.all()
    title1 = request.GET.get('title')
    tag1 = request.GET.get('tag')
    if title1 != '' and title1 is not None:
        Projects = Projects.filter(title__icontains=title1)
    if tag1 != '' and tag1 is not None:
        Projects = Projects.filter(tags__slug__icontains=tag1)
    context = {'projects': Projects, 'user': user}
    return render(request, 'projects/list_project.html', context)


def project_details(request, id):
    project_details = get_object_or_404(Project_data, id=id)
    project_pics = Project_pics.objects.filter(id=id)

    comments = project_details.comments
    comment_form = CommentForm()
    new_comment = None

    rate = Rate_project.objects.filter(project=id)
    average = rate.aggregate(Avg("value"))["value__avg"]
    if average == None:
        average = 0

    context = {'project_details': project_details, 'comment_form': CommentForm, 'comment': comments, "average": average
        , 'project_pics': project_pics}
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


def add_project(request, id):
    if request.method == 'GET':
        form_dict = {}
        form = Project_Data()
        form_dict['form'] = form
        return render(request, 'projects/form.html', form_dict)
    else:
        if request.method == 'POST':
            form = Project_Data(request.POST, request.FILES)
            if form.is_valid():
                user = Users.objects.get(id=id)
                project = form.save(commit=False)
                images = request.FILES.getlist("more_images")

                project.user = user
                form.save()
                for i in images:
                    Project_pics.objects.create(image=i, project=project)
                project_pics = Project_pics.objects.filter(id=id)
                Projects = Project_data.objects.all()
                context = {'projects': Projects, 'project_pics': project_pics}

                return render(request, 'projects/list_project.html', context)


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


def donate(request, project_id, user_id):
    if request.method == 'POST':
        # d=request.POST.get['dontation_value']
        donating_value = int(request.POST.get('donation_value'))
        project = Project_data.objects.get(id=project_id)
        project.current_money += donating_value
        if project.current_money <= project.target:
            project.save()
            Donate_project.objects.create(
                project=project,
                user=Users.objects.get(id=user_id),
                value=donating_value
            )
            a = messages.success(request, 'Your Donation done successfully!')
            return redirect(f"/{project_id}")
        else:
            messages.error(request, 'Your Donation failed')
            return redirect(f"/{project_id}")


def report_p(request, id):
    if request.method == 'POST':
        project = Project_data.objects.get(id=id)

        project.save()
        if Report_project().is_reported == True:
            messages.error(request, "reported")
            return redirect(f"/{id}")
        else:
            Report_project.objects.create(
                user=Users.objects.get(id=request.POST['u']),
                project=project,

                is_reported=True
            )
        a = messages.success(request, 'Your Donation done successfully!')

        return redirect(f"/{id}")


def project_rating(request, id):
    if request.method == "POST":
        user = request.user.id
        project = Project_data.objects.get(id=id)
        Rate_project.project = project
        Rate_project.objects.update_or_create(
            project_id=id, user_id=request.POST['u'], value=request.POST['v'])
        project_rating = project.project_rating_set.all().aggregate(Avarage=avg("rating"))
        Rate_project.objects.update_or_create(
            id=id, defaults={'rating': project_rating})
        return redirect(f"/{id}")


def add_rate(request, id):
    project = Project_data.objects.get(id=id)
    if request.method == "POST":
        rate = Rate_project.objects.filter(id=id)
        Rate_project.objects.create(
            user=Users.objects.get(id=request.POST['u']),
            project=project,
            value=request.POST["rating"],
        )

    return redirect(f"/{id}")
