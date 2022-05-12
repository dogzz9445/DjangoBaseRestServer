from django.shortcuts import render
from rest_framework import viewsets, response, permissions
from rest_framework.decorators import api_view, permission_classes
from django.conf import settings
from scenario.models import *
from scenario.serializers import *
#https://github.com/Joel-hanson/simple-file-upload/blob/master/project_name/urls.py

# Create your views here.
class InteractionAreaViewSet(viewsets.ModelViewSet):
    queryset = InteractionArea.objects.all()
    serializer_class = InteractionAreaSerializer

