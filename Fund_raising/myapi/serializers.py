from rest_framework import serializers
from projects.models import *
class ProjectDataSerializers(serializers.ModelSerializer):
    class Meta :
        model = Project_data
        fields = '__all__'
class CategorySerializers(serializers.ModelSerializer):
    class Meta :
        model = Category
        fields = '__all__'
class PicsSerializers(serializers.ModelSerializer):
    class Meta :
        model = Project_pics
        fields = '__all__'
class CommentsSerializers(serializers.ModelSerializer):
    class Meta :
        model = project_comments
        fields = '__all__'
# class TagsSerializers(serializers.ModelSerializer):
#     class Meta :
#         model = project_tags
#         fields = '__all__'
class ReportsSerializers(serializers.ModelSerializer):
    class Meta :
        model = Report_project
        fields = '__all__'
class RatesSerializers(serializers.ModelSerializer):
    class Meta :
        model = Rate_project
        fields = '__all__'
class DonationsSerializers(serializers.ModelSerializer):
    class Meta :
        model = Donate_project
        fields = '__all__'
class ReportComments_Serializers(serializers.ModelSerializer):
    class Meta :
        model = Report_comment
        fields = '__all__'

