# from django.shortcuts import render
# from django.http import HttpResponse
# from projects.models import Project_data
# from .serializers import ProjectDataSerializers
# from rest_framework.decorators import api_view
# from rest_framework import viewsets,status
# from django.http.response import JsonResponse# Create your views here.
# from rest_framework.response import Response
# class ProjectList(viewsets.ModelViewSet):
#     queryset = Project_data.objects.all()
#     serializer_class= ProjectDataSerializers
# # class Trackviewset(viewsets.ModelViewSet):
# #     queryset = Track.objects.all()
# #     serializer_class= Trackserializers
# @api_view(['GET', 'PUT', 'DELETE'])
# def projectDetail(request, id):
#     try:
#         project = Project_data.objects.get(id=id)
#     except Project_data.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = ProjectDataSerializers(project)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         studnt = Project_data.objects.get(id=request.POST.get('id'))
#         studnt.title = request.POST.get('title')
#         studnt.save()
#         return Response({'student updated '})

#     elif request.method == 'DELETE':
#         project.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)
