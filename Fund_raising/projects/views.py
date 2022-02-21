from audioop import avg
from django.contrib import messages
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.models import Users
from .forms import *

# Create your views here.
from .models import Report_comment


def project_list(request, id):
    user = Users.objects.get(id=id)
    projects = Project_data.objects.all()
    title1 = request.GET.get('title')
    tag1 = request.GET.get('tag')
    if title1 != '' and title1 is not None:
        projects = projects.filter(title__icontains=title1)
    if tag1 != '' and tag1 is not None:
        projects = projects.filter(tags__slug__icontains=tag1)
    context = {'projects': projects, 'user': user}
    return render(request, 'projects/list_project.html', context)


def project_details(request, project_id, user_id):
    project_details = get_object_or_404(Project_data, id=project_id)
    project_pics = Project_pics.objects.filter(id=project_id)
    rate = Rate_project.objects.filter(project=project_id)
    user = get_object_or_404(Users, id=user_id)

    average = rate.aggregate(Avg("value"))["value__avg"]
    if average == None:
        average = 0
    comments = project_details.comments
    comment_form = CommentForm()
    new_comment = None
    print("hi")
    print(project_pics)

    context = {'project_details': project_details, 'comment_form': CommentForm, "average": average, 'comment': comments
        , 'project_pics': project_pics, 'user': user}
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            project_comments.objects.create(
                project=project_details,
                comment_user=user,
                comment=request.POST['comment'],

            )

    else:
        comment_form = CommentForm()

    return render(request, 'projects/project_details.html', context)


def add_project(request, id):
    user = get_object_or_404(Users, id=id)
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
                context = {'projects': Projects, 'project_pics': project_pics, 'user': user}

                return render(request, 'profile.html', context)


def donate(request, project_id, user_id):
    if request.method == 'POST':

        donating_value = int(request.POST.get('donation_value'))
        project = Project_data.objects.get(id=project_id)
        project.current_money += donating_value
        if project.current_money <= project.target or project.current_money == project.target or project.current_money >= project.target:
            project.target = project.target - donating_value

            project.save()
            Donate_project.objects.create(
                project=project,
                user=Users.objects.get(id=user_id),
                value=donating_value,

            )

            return redirect(f"/{project_id}/{user_id}/project_details")
        else:

            return redirect(f"/{project_id}/{user_id}/project_details")


def report_p(request, project_id, user_id):
    if request.method == 'POST':
        user = Users.objects.get(id=user_id)
        project = Project_data.objects.get(id=project_id)
        Report_project.objects.create(
            user=Users.objects.get(id=user_id),
            project=project,
            is_reported=True
        )
        context = {'msg': "reported", 'project_details': project, 'user': user}
        return render(request, 'projects/project_details.html', context)


def report_c(request, project_id, user_id, comment_id):
    if request.method == 'POST':
        project = Project_data.objects.get(id=project_id)
        comment = project_comments.objects.get(id=comment_id)

        comment.save()
        if Report_comment.is_reported == True:
            messages.error(request, "reported")
            return redirect(f"/{project_id}/{user_id}/project_details")
        else:
            Report_comment.objects.create(
                user=Users.objects.get(id=user_id),
                comment=comment,
                project=project,
                is_reported=True
            )
            return redirect(f"/{project_id}/{user_id}/project_details")


def add_rate(request, project_id, user_id):
    user = Users.objects.get(id=user_id)
    project = Project_data.objects.get(id=project_id)
    if request.method == "POST":
        rate = Rate_project.objects.filter(id=project_id)
        Rate_project.objects.create(
            user=user,
            project=project,
            value=request.POST["rating"],
        )
        return redirect(f"/{project_id}/{user_id}/project_details")


# def add_rate(request, project_id, user_id):
#     user = Users.objects.get(id=user_id)
#
#     project = Project_data.objects.get(id=project_id)
#     try:
#         get_rate = Rate_project.objects.get(user=user, project=project)
#     except Rate_project.DoesNotExist:
#         get_rate = Rate_project.objects.filter(user=user, project=project)
#
#     if request.method == "POST":
#         defaults = {'user': user, 'project': project, 'value': request.POST["rating"]}
#         try:
#             rate = Rate_project.objects.get(user=user, project=project, value=0)
#             for key, value in defaults.items():
#                 setattr(rate, key, value)
#             rate.save()
#             return redirect(f"/{project_id}/{user_id}/project_details")
#         except Rate_project.DoesNotExist:
#             new_values = {'user': user, 'project': project, 'value': request.POST["rating"]}
#             new_values.update(defaults)
#             obj = Rate_project(**new_values)
#             obj.save()
#             return redirect(f"/{project_id}/{user_id}/project_details")


def home(req, id):
    user = Users.objects.get(id=id)

    projectRates = Rate_project.objects.all().values('project').annotate(
        Avg('value')).order_by('-value__avg')[:5]

    highRatedProjects = []
    # project_pics2 = {}
    for p in projectRates:
        # print("id ?? ", p.get('project') , projectRates)
        highRatedProjects.append(Project_data.objects.get(id=p.get('project')))

    latestFiveList = Project_data.objects.extra(order_by=['-created_at'])[:5]

    featuredList = Project_data.objects.all().filter(featured='True')[:5]
    print(featuredList)

    categories = Category.objects.all()
    context = {
        'lproj': latestFiveList,
        'fproj': featuredList,
        'hproj': highRatedProjects,
        'cate': categories,
        'user': user
    }
    # print(highRatedProjects)
    return render(req, 'home.html', context)


def cate_view(req, uid, cid):
    user = Users.objects.get(id=uid)
    cate = Category.objects.get(id=cid)
    projs = Project_data.objects.filter(category=cate)
    return render(req, 'projects/category.html', {'projs': projs, 'cname': cate.name, 'user': user})


def cancel_project(request, project_id, user_id):
    if request.method == "POST":
        user = Users.objects.get(id=user_id)
        project = Project_data.get(id=project_id)
        if project.current_money < project.target * 0.25:
            pr_cancel = Project_data.objects.get(id=project, user=user_id)
            pr_cancel.delete()

    return render("project_list_of_user")
