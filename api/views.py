from django.shortcuts import render
from rest_framework import viewsets, response, permissions
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *

# Create your views here.
class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    


@permission_classes((permissions.AllowAny,))
class MediaViewSet(viewsets.ViewSet):
    
    def list(self, request):
        
        # 1. Media의 아래 하위 파일들 목록 가져오기
        
        # 2. 파일명이랑 정리해서 내보내기
        
        
        return response.Response('test')
