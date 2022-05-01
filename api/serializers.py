from rest_framework import serializers 
from .models import * 

class ScheduleSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Schedule
        fields = ('id','title','color','description', 'scheduledDate') 
