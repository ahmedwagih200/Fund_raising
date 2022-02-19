from rest_framework import viewsets,status
from projects.models import *
from .serializers import *
class ProjectList(viewsets.ModelViewSet):
    queryset = Project_data.objects.all()
    serializer_class= ProjectDataSerializers
class CategoryViewset(viewsets.ModelViewSet):
     queryset = Category.objects.all()
     serializer_class= CategorySerializers
class PicsViewset(viewsets.ModelViewSet):
     queryset = Project_pics.objects.all()
     serializer_class= PicsSerializers
class CommentsViewset(viewsets.ModelViewSet):
     queryset = project_comments.objects.all()
     serializer_class= CommentsSerializers
# class TagsViewset(viewsets.ModelViewSet):
#      queryset = project_tags.objects.all()
#      serializer_class= TagsSerializers
class ReportsViewset(viewsets.ModelViewSet):
     queryset = Report_project.objects.all()
     serializer_class= ReportsSerializers
class RatesViewset(viewsets.ModelViewSet):
     queryset = Rate_project.objects.all()
     serializer_class= RatesSerializers
class DonationsViewset(viewsets.ModelViewSet):
     queryset = Donate_project.objects.all()
     serializer_class= DonationsSerializers
class ReportComments_Viewset(viewsets.ModelViewSet):
     queryset = Report_comment.objects.all()
     serializer_class= DonationsSerializers