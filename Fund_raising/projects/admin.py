from django.contrib import admin

from users.models import Users
from .models import Category, Project_pics, Project_data, project_comments

# Register your models here.

admin.site.register(Category)

admin.site.register(Project_pics)
admin.site.register(Project_data)
admin.site.register(project_comments)
admin.site.register(Users)
