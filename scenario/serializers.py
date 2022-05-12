from pkg_resources import require
from rest_framework import serializers 
from scenario.models import * 

class InteractionAreaSerializer(serializers.ModelSerializer): 
    id = serializers.IntegerField(read_only=True)
    Name = serializers.CharField(required=True, max_length=40)
    Facility = serializers.ChoiceField(choices=FACILITY_CHOICES, default='MultiUseFacility')

    class Meta: 
        model = InteractionArea
        fields = ('id','Name', 'Facility', 'Type', 'Transform', 'Collider_Size_X', 'Collider_Size_Y', 'Collider_Size_Z', 'Next1', 'Next2') 

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return InteractionArea.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.Name = validated_data.get('Name', instance.Name)
        instance.Facility = validated_data.get('Facility', instance.Facility)
        
        
        instance.save()
        return instance
        
# Serializer for multiple files upload.
# Serializer for multiple files upload.
class MultipleFilesUploadSerializer(serializers.Serializer):
    file_uploaded = serializers.ListField(child=serializers.FileField())
    class Meta:
        fields = ['file_uploaded']