from django.shortcuts import render
from rest_framework import viewsets, response, permissions
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        return Token.objects.create(user=instance)

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
