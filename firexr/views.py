from django.shortcuts import render
from rest_framework import viewsets, response, permissions
from rest_framework.decorators import api_view, permission_classes
from django.conf import settings
from rest_framework.views import APIView
from firexr.models import *
from firexr.serializers import *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class TransformViewSet(viewsets.ModelViewSet):
    queryset = Transform.objects.all()
    serializer_class = TransformSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

@method_decorator(csrf_exempt, name='dispatch')
class InteractionPointViewSet(viewsets.ModelViewSet):
    queryset = InteractionPoint.objects.all()
    serializer_class = InteractionPointSerializer

@method_decorator(csrf_exempt, name='dispatch')
class CutSceneViewSet(viewsets.ModelViewSet):
    queryset = CutScene.objects.all()
    serializer_class = CutSceneSerializer

@method_decorator(csrf_exempt, name='dispatch')
class ObjectInfoViewSet(viewsets.ModelViewSet):
    queryset = ObjectInfo.objects.all()
    serializer_class = ObjectInfoSerializer

    def create(self, request, *args, **kwargs):
        """
        #checks if post request data is an array initializes serializer with many=True
        else executes default CreateModelMixin.create function 
        """
        is_many = isinstance(request.data, list)
        if not is_many:
            return super(ObjectInfoViewSet, self).create(request, *args, **kwargs)
        else:
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return response.Response(serializer.data, status=201, headers=headers)

@method_decorator(csrf_exempt, name='dispatch')
class SoundViewSet(viewsets.ModelViewSet):
    queryset = Sound.objects.all()
    serializer_class = SoundSerializer

@method_decorator(csrf_exempt, name='dispatch')
class FDSFileViewSet(viewsets.ModelViewSet):
    queryset = FDSFile.objects.all()
    serializer_class = FDSFileSerializer

@method_decorator(csrf_exempt, name='dispatch')
class FDSViewSet(viewsets.ModelViewSet):
    queryset = FDS.objects.all()
    serializer_class = FDSSerializer

@method_decorator(csrf_exempt, name='dispatch')
class XREventViewSet(viewsets.ModelViewSet):
    queryset = XREvent.objects.all()
    serializer_class = XREventSerializer

@method_decorator(csrf_exempt, name='dispatch')
class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

@method_decorator(csrf_exempt, name='dispatch')
class EvaluationActionViewSet(viewsets.ModelViewSet):
    queryset = EvaluationAction.objects.all()
    serializer_class = EvaluationActionSerializer

@method_decorator(csrf_exempt, name='dispatch')
class SeparatedScenarioViewSet(viewsets.ModelViewSet):
    queryset = SeparatedScenario.objects.all()
    serializer_class = SeparatedScenarioSerializer

@method_decorator(csrf_exempt, name='dispatch')
class CombinedScenarioViewSet(viewsets.ModelViewSet):
    queryset = CombinedScenario.objects.all()
    serializer_class = CombinedScenarioSerializer


###
### Integrated ViewSets
###

class IntegratedTransformViewSet(viewsets.ModelViewSet):
    queryset = Transform.objects.all()
    serializer_class = IntegratedTransformSerializer

class IntegratedInteractionPointViewSet(viewsets.ModelViewSet):
    queryset = InteractionPoint.objects.all()
    serializer_class = IntegratedInteractionPointSerializer

class IntegratedCutSceneViewSet(viewsets.ModelViewSet):
    queryset = CutScene.objects.all()
    serializer_class = IntegratedCutSceneSerializer

class IntegratedObjectInfoViewSet(viewsets.ModelViewSet):
    queryset = ObjectInfo.objects.all()
    serializer_class = IntegratedObjectInfoSerializer

class IntegratedSoundViewSet(viewsets.ModelViewSet):
    queryset = Sound.objects.all()
    serializer_class = IntegratedSoundSerializer

class IntegratedFDSFileViewSet(viewsets.ModelViewSet):
    queryset = FDSFile.objects.all()
    serializer_class = IntegratedFDSFileSerializer

class IntegratedFDSViewSet(viewsets.ModelViewSet):
    queryset = FDS.objects.all()
    serializer_class = IntegratedFDSSerializer

class IntegratedXREventViewSet(viewsets.ModelViewSet):
    queryset = XREvent.objects.all()
    serializer_class = IntegratedXREventSerializer

class IntegratedEvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = IntegratedEvaluationSerializer

class IntegratedEvaluationActionViewSet(viewsets.ModelViewSet):
    queryset = EvaluationAction.objects.all()
    serializer_class = IntegratedEvaluationActionSerializer

class IntegratedSeparatedScenarioViewSet(viewsets.ModelViewSet):
    queryset = SeparatedScenario.objects.all()
    serializer_class = IntegratedSeparatedScenarioSerializer

class IntegratedCombinedScenarioViewSet(viewsets.ModelViewSet):
    queryset = CombinedScenario.objects.all()
    serializer_class = IntegratedCombinedScenarioSerializer



###
### API List and Details
###
class APITransformList(APIView):

    def get(self, request, format=None):
        datas = Transform.objects.all()
        serializer = IntegratedTransformSerializer(datas, many=True)
        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = TransformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=response.status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=response.status.HTTP_400_BAD_REQUEST)

class APITransformDetail(APIView):

    def get_object(self, pk):
        try:
            return Transform.objects.get(pk=pk)
        except Transform.DoesNotExist:
            raise response.Http404

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = IntegratedTransformSerializer(instance)
        return response.Response(serializer.data)

    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = TransformSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=response.status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=response.status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        return response.Response(status=response.status.HTTP_204_NO_CONTENT)

class APIInteractionPointList(APIView):

    def get(self, request, format=None):
        datas = InteractionPoint.objects.all()
        serializer = IntegratedInteractionPointSerializer(datas, many=True)
        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = InteractionPointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=response.status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=response.status.HTTP_400_BAD_REQUEST)

class APIInteractionPointDetail(APIView):

    def get_object(self, pk):
        try:
            return InteractionPoint.objects.get(pk=pk)
        except InteractionPoint.DoesNotExist:
            raise response.Http404

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = IntegratedInteractionPointSerializer(instance)
        return response.Response(serializer.data)

    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = InteractionPointSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=response.status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=response.status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        return response.Response(status=response.status.HTTP_204_NO_CONTENT)


class APICutSceneList(APIView):

    def get(self, request, format=None):
        datas = CutScene.objects.all()
        serializer = IntegratedCutSceneSerializer(datas, many=True)
        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = CutSceneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=response.status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=response.status.HTTP_400_BAD_REQUEST)

class APICutSceneDetail(APIView):

    def get_object(self, pk):
        try:
            return CutScene.objects.get(pk=pk)
        except CutScene.DoesNotExist:
            raise response.Http404

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = IntegratedCutSceneSerializer(instance)
        return response.Response(serializer.data)

    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = CutSceneSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=response.status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=response.status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        return response.Response(status=response.status.HTTP_204_NO_CONTENT)

class APIObjectInfoList(APIView):

    def get(self, request, format=None):
        datas = ObjectInfo.objects.all()
        serializer = IntegratedObjectInfoSerializer(datas, many=True)
        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = ObjectInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=response.status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=response.status.HTTP_400_BAD_REQUEST)

class APIObjectInfoDetail(APIView):

    def get_object(self, pk):
        try:
            return ObjectInfo.objects.get(pk=pk)
        except ObjectInfo.DoesNotExist:
            raise response.Http404

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = IntegratedObjectInfoSerializer(instance)
        return response.Response(serializer.data)

    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = ObjectInfoSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=response.status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=response.status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        return response.Response(status=response.status.HTTP_204_NO_CONTENT)

class APISoundList(APIView):

    def get(self, request, format=None):
        datas = Sound.objects.all()
        serializer = IntegratedSoundSerializer(datas, many=True)
        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = SoundSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=response.status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=response.status.HTTP_400_BAD_REQUEST)

class APISoundDetail(APIView):

    def get_object(self, pk):
        try:
            return Sound.objects.get(pk=pk)
        except Sound.DoesNotExist:
            raise response.Http404

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = IntegratedSoundSerializer(instance)
        return response.Response(serializer.data)

    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = SoundSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=response.status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=response.status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        return response.Response(status=response.status.HTTP_204_NO_CONTENT)

class APIFDSFileList(APIView):

    def get(self, request, format=None):
        datas = FDSFile.objects.all()
        serializer = IntegratedFDSFileSerializer(datas, many=True)
        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = FDSFileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=response.status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=response.status.HTTP_400_BAD_REQUEST)

class APIFDSFileDetail(APIView):

    def get_object(self, pk):
        try:
            return FDSFile.objects.get(pk=pk)
        except FDSFile.DoesNotExist:
            raise response.Http404

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = IntegratedFDSFileSerializer(instance)
        return response.Response(serializer.data)

    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = FDSFileSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=response.status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=response.status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        return response.Response(status=response.status.HTTP_204_NO_CONTENT)

class APIFDSList(APIView):

    def get(self, request, format=None):
        datas = FDS.objects.all()
        serializer = IntegratedFDSSerializer(datas, many=True)
        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = FDSSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=response.status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=response.status.HTTP_400_BAD_REQUEST)

class APIFDSDetail(APIView):

    def get_object(self, pk):
        try:
            return FDS.objects.get(pk=pk)
        except FDS.DoesNotExist:
            raise response.Http404

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = IntegratedFDSSerializer(instance)
        return response.Response(serializer.data)

    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = FDSSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=response.status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=response.status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        return response.Response(status=response.status.HTTP_204_NO_CONTENT)

class APIXREventList(APIView):

    def get(self, request, format=None):
        datas = XREvent.objects.all()
        serializer = IntegratedXREventSerializer(datas, many=True)
        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = XREventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=response.status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=response.status.HTTP_400_BAD_REQUEST)

class APIXREventDetail(APIView):

    def get_object(self, pk):
        try:
            return XREvent.objects.get(pk=pk)
        except XREvent.DoesNotExist:
            raise response.Http404

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = IntegratedXREventSerializer(instance)
        return response.Response(serializer.data)

    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = XREventSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=response.status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=response.status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        return response.Response(status=response.status.HTTP_204_NO_CONTENT)

class APIEvaluationList(APIView):

    def get(self, request, format=None):
        datas = Evaluation.objects.all()
        serializer = IntegratedEvaluationSerializer(datas, many=True)
        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = EvaluationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=response.status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=response.status.HTTP_400_BAD_REQUEST)

class APIEvaluationDetail(APIView):

    def get_object(self, pk):
        try:
            return Evaluation.objects.get(pk=pk)
        except Evaluation.DoesNotExist:
            raise response.Http404

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = IntegratedEvaluationSerializer(instance)
        return response.Response(serializer.data)

    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = EvaluationSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=response.status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=response.status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        return response.Response(status=response.status.HTTP_204_NO_CONTENT)

class APIEvaluationActionList(APIView):

    def get(self, request, format=None):
        datas = EvaluationAction.objects.all()
        serializer = IntegratedEvaluationActionSerializer(datas, many=True)
        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = EvaluationActionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=response.status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=response.status.HTTP_400_BAD_REQUEST)

class APIEvaluationActionDetail(APIView):

    def get_object(self, pk):
        try:
            return EvaluationAction.objects.get(pk=pk)
        except EvaluationAction.DoesNotExist:
            raise response.Http404

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = IntegratedEvaluationActionSerializer(instance)
        return response.Response(serializer.data)

    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = EvaluationActionSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=response.status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=response.status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        return response.Response(status=response.status.HTTP_204_NO_CONTENT)

class APISeparatedScenarioList(APIView):

    def get(self, request, format=None):
        datas = SeparatedScenario.objects.all()
        serializer = IntegratedSeparatedScenarioSerializer(datas, many=True)
        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = SeparatedScenarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=response.status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=response.status.HTTP_400_BAD_REQUEST)

class APISeparatedScenarioDetail(APIView):

    def get_object(self, pk):
        try:
            return SeparatedScenario.objects.get(pk=pk)
        except SeparatedScenario.DoesNotExist:
            raise response.Http404

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = IntegratedSeparatedScenarioSerializer(instance)
        return response.Response(serializer.data)

    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = SeparatedScenarioSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=response.status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=response.status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        return response.Response(status=response.status.HTTP_204_NO_CONTENT)

class APICombinedScenarioList(APIView):

    def get(self, request, format=None):
        datas = CombinedScenario.objects.all()
        serializer = IntegratedCombinedScenarioSerializer(datas, many=True)
        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = CombinedScenarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=response.status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=response.status.HTTP_400_BAD_REQUEST)

class APICombinedScenarioDetail(APIView):

    def get_object(self, pk):
        try:
            return CombinedScenario.objects.get(pk=pk)
        except CombinedScenario.DoesNotExist:
            raise response.Http404

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = IntegratedCombinedScenarioSerializer(instance)
        return response.Response(serializer.data)

    def put(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = CombinedScenarioSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=response.status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=response.status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.delete()
        return response.Response(status=response.status.HTTP_204_NO_CONTENT)


