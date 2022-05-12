from django.shortcuts import render
from rest_framework import viewsets, response, permissions
from rest_framework.decorators import api_view, permission_classes
from django.conf import settings
from firexr.models import *
from firexr.serializers import *

# Create your views here.
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
