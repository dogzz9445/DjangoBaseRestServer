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
        
class TransformSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)

    class Meta: 
        model = Transform
        fields = ('ID', 'PositionX', 'PositionY', 'PositionZ') 

    def create(self, validated_data):
        return Transform.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance
        
class InteractionPointSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    
    class Meta: 
        model = InteractionPoint
        fields = '__all__'

    def create(self, validated_data):
        return InteractionPoint.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance
        
class CutSceneSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    
    class Meta: 
        model = CutScene
        fields = '__all__'

    def create(self, validated_data):
        return CutScene.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance
        
class ObjectInfoSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    
    class Meta: 
        model = ObjectInfo
        fields = '__all__'

    def create(self, validated_data):
        return ObjectInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance
        
class SoundSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    
    class Meta: 
        model = Sound
        fields = '__all__'

    def create(self, validated_data):
        return Sound.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance
        
class FDSFileSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    
    class Meta: 
        model = FDSFile
        fields = '__all__'

    def create(self, validated_data):
        return FDSFile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance
        
class FDSSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    
    class Meta: 
        model = FDS
        fields = '__all__'

    def create(self, validated_data):
        return FDS.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance
        
class XREventSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    
    class Meta: 
        model = XREvent
        fields = '__all__'

    def create(self, validated_data):
        return XREvent.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance
        
class EvaluationSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    
    class Meta: 
        model = Evaluation
        fields = '__all__'

    def create(self, validated_data):
        return Evaluation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance
        
class EvaluationActionSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    
    class Meta: 
        model = EvaluationAction
        fields = '__all__'

    def create(self, validated_data):
        return EvaluationAction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance
        
class InteractionAreaSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    
    class Meta: 
        model = InteractionArea
        fields = '__all__'

    def create(self, validated_data):
        return InteractionArea.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance
        
class SeparatedScenarioSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    
    class Meta: 
        model = SeparatedScenario
        fields = '__all__'

    def create(self, validated_data):
        return SeparatedScenario.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance
        
class CombinedScenarioSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    
    class Meta: 
        model = CombinedScenario
        fields = '__all__'

    def create(self, validated_data):
        return CombinedScenario.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance
        
# Serializer for multiple files upload.
# Serializer for multiple files upload.
class MultipleFilesUploadSerializer(serializers.Serializer):
    file_uploaded = serializers.ListField(child=serializers.FileField())
    class Meta:
        fields = ['file_uploaded']