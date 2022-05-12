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

class TransformViewSet(viewsets.ModelViewSet):
    queryset = Transform.objects.all()
    serializer_class = TransformSerializer

class InteractionPointViewSet(viewsets.ModelViewSet):
    queryset = InteractionPoint.objects.all()
    serializer_class = InteractionPointSerializer

class CutSceneViewSet(viewsets.ModelViewSet):
    queryset = CutScene.objects.all()
    serializer_class = CutSceneSerializer

class ObjectInfoViewSet(viewsets.ModelViewSet):
    queryset = ObjectInfo.objects.all()
    serializer_class = ObjectInfoSerializer

class SoundViewSet(viewsets.ModelViewSet):
    queryset = Sound.objects.all()
    serializer_class = SoundSerializer

class FDSFileViewSet(viewsets.ModelViewSet):
    queryset = FDSFile.objects.all()
    serializer_class = FDSFileSerializer

class FDSViewSet(viewsets.ModelViewSet):
    queryset = FDS.objects.all()
    serializer_class = FDSSerializer

class XREventViewSet(viewsets.ModelViewSet):
    queryset = XREvent.objects.all()
    serializer_class = XREventSerializer

class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

class EvaluationActionViewSet(viewsets.ModelViewSet):
    queryset = EvaluationAction.objects.all()
    serializer_class = EvaluationActionSerializer

class SeparatedScenarioViewSet(viewsets.ModelViewSet):
    queryset = SeparatedScenario.objects.all()
    serializer_class = SeparatedScenarioSerializer

class CombinedScenarioViewSet(viewsets.ModelViewSet):
    queryset = CombinedScenario.objects.all()
    serializer_class = CombinedScenarioSerializer
