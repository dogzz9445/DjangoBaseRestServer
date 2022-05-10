"""BaseRestServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from email.mime import base
from django import forms
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets, response, permissions
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import FileUploadParser
import os

from api.views import *
from scenario.views import *

def handle_uploaded_file(filename, file):
    with open(filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
            
@permission_classes((permissions.AllowAny,))
class UploadViewSet(viewsets.ViewSet):
    parser_classes = [FileUploadParser]
    media_root = settings.MEDIA_ROOT

    def list(self, request):
        filelist = os.listdir(self.media_root)
        return response.Response('Get API')

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        # ...
        # do some stuff with uploaded file
        # ...
        handle_uploaded_file(self.media_root + '/' + filename, file_obj)

        return response.Response(status=204)

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'upload', UploadViewSet, basename='upload')
router.register(r'media', UploadViewSet, basename='media')
router.register(r'scenario/interactionarea', InteractionAreaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
