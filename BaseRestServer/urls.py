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
from rest_framework.authtoken import views as auth_views
import os

from api.views import *
from scenario.views import *
from firexr.views import *

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
        return response.Response(filelist)

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
router.register(r'scenario', UploadViewSet, basename='scenario')
router.register(r'interactionarea', UploadViewSet, basename='interactionarea')
router.register(r'objectinfo', UploadViewSet, basename='objectinfo')
router.register(r'interactionarea', InteractionAreaViewSet)

router.register(r'unit/transform', TransformViewSet, basename='unit/transform')
router.register(r'unit/interactionpoint', InteractionPointViewSet, basename='unit/interactionpoint')
router.register(r'unit/cutscene', CutSceneViewSet, basename='unit/cutscene')
router.register(r'unit/objectinfo', ObjectInfoViewSet, basename='unit/objectinfo')
router.register(r'unit/sound', SoundViewSet, basename='unit/sound')
router.register(r'unit/fdsfile', FDSFileViewSet, basename='unit/fdsfile')
router.register(r'unit/fds', FDSViewSet, basename='unit/fds')
router.register(r'unit/xrevent', XREventViewSet, basename='unit/xrevent')
router.register(r'unit/evaluation', EvaluationViewSet, basename='unit/evaluation')
router.register(r'unit/evaluationaction', EvaluationActionViewSet, basename='unit/evaluationaction')
router.register(r'unit/separatedscenario', SeparatedScenarioViewSet, basename='unit/separatedscenairo')
router.register(r'unit/combinedscenario', CombinedScenarioViewSet, basename='unit/combinedscenario')

router.register(r'integrated/transform', IntegratedTransformViewSet, basename='integrated/transform')
router.register(r'integrated/interactionpoint', IntegratedInteractionPointViewSet, basename='integrated/interactionpoint')
router.register(r'integrated/cutscene', IntegratedCutSceneViewSet, basename='integrated/cutscene')
router.register(r'integrated/objectinfo', IntegratedObjectInfoViewSet, basename='integrated/objectinfo')
router.register(r'integrated/sound', IntegratedSoundViewSet, basename='integrated/sound')
router.register(r'integrated/fdsfile', IntegratedFDSFileViewSet, basename='integrated/fdsfile')
router.register(r'integrated/fds', IntegratedFDSViewSet, basename='integrated/fds')
router.register(r'integrated/xrevent', IntegratedXREventViewSet, basename='integrated/xrevent')
router.register(r'integrated/evaluation', IntegratedEvaluationViewSet, basename='integrated/evaluation')
router.register(r'integrated/evaluationaction', IntegratedEvaluationActionViewSet, basename='integrated/evaluationaction')
router.register(r'integrated/separatedscenario', IntegratedSeparatedScenarioViewSet, basename='integrated/separatedscenario')
router.register(r'integrated/combinedscenario', IntegratedCombinedScenarioViewSet, basename='integrated/combinedscenario')

# router.register(r'api/transform', APITransformList.as_view(), basename='api/transform')
# router.register(r'api/transform/<int:pk>/', APITransformDetail.as_view(), basename='api/transform')
# router.register(r'api/interactionpoint', APIInteractionPointList.as_view(), basename='api/interactionpoint')
# router.register(r'api/cutscene', APICutSceneList.as_view(), basename='api/cutscene')
# router.register(r'api/objectinfo', APIObjectInfoList.as_view(), basename='api/objectinfo')
# router.register(r'api/sound', APISoundList.as_view(), basename='api/sound')
# router.register(r'api/fdsfile', APIFDSFileList.as_view(), basename='api/fdsfile')
# router.register(r'api/fds', APIFDSList.as_view(), basename='api/fds')
# router.register(r'api/xrevent', APIXREventList.as_view(), basename='api/xrevent')
# router.register(r'api/evaluation', APIEvaluationList.as_view(), basename='api/evaluation')
# router.register(r'api/evaluationaction', APIEvaluationActionList.as_view(), basename='api/evaluationaction')
# router.register(r'api/separatedscenario', APISeparatedScenarioList.as_view(), basename='api/separatedscenario')
# router.register(r'api/combinedscenario', APICombinedScenarioList.as_view(), basename='api/combinedscenario')

router.register(r'combinedscenario', CombinedScenarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', auth_views.obtain_auth_token),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
