from pkg_resources import require
from rest_framework import serializers 
from firexr.models import * 

class TransformSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)

    class Meta: 
        model = Transform
        fields = '__all__'

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
        
class SeparatedScenarioSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    Scenarios = serializers.SlugRelatedField(many=True, slug_field='ID', queryset=SeparatedScenario.objects.all())
    
    class Meta: 
        model = SeparatedScenario
        fields = '__all__'


class CombinedScenarioSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    Scenarios = serializers.SlugRelatedField(many=True, slug_field='ID', queryset=SeparatedScenario.objects.all())
    
    class Meta: 
        model = CombinedScenario
        fields = '__all__'

    def get_or_create_scenarios(self, scenarios):
        scenario_ids = []
        for scenario in scenarios:
            package_instance, created = SeparatedScenario.objects.get_or_create(pk=scenario.ID, defaults=scenario)
            scenario_ids.append(package_instance.pk)
        return scenario_ids

    def create_or_update_packages(self, scenarios):
        scenario_ids = []
        for scenario in scenarios:
            package_instance, created = SeparatedScenario.objects.update_or_create(pk=scenario.ID, defaults=scenario)
            scenario_ids.append(package_instance.pk)
        return scenario_ids

    def create(self, validated_data):
        separated_scenarios = validated_data.pop("Scenarios")
        instance = CombinedScenario.objects.create(**validated_data)
        instance.save()
        instance.Scenarios.set(self.get_or_create_packages(separated_scenarios))
        return instance

    def update(self, instance, validated_data):
        instance.save()
        return instance
    
