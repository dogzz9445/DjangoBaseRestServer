from pkg_resources import require
from rest_framework import serializers 
from firexr.models import * 
import firexr.proto.firexr_scenario_pb2 as proto

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
    Facility = serializers.ChoiceField(choices=[(value, key) for key, value in proto.FacilityType.items()], default=0)
    
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
        
class EvaluationSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    EvaluationActions = serializers.SlugRelatedField(many=True, slug_field='ID', queryset=EvaluationAction.objects.all())
    
    class Meta: 
        model = Evaluation
        fields = '__all__'

    def create(self, validated_data):
        return Evaluation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance
        
class SeparatedScenarioSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    Facility = serializers.ChoiceField(choices=[(value, key) for key, value in proto.FacilityType.items()], default=0)
    Evaluations = serializers.SlugRelatedField(many=True, slug_field='ID', queryset=Evaluation.objects.all())
    XREvents = serializers.SlugRelatedField(many=True, slug_field='ID', queryset=XREvent.objects.all())
    
    def get_or_create_evaluations(self, evaluations):
        evaluation_ids = []
        for evaluation in evaluations:
            evaluation_instance, created = Evaluation.objects.get_or_create(pk=evaluation.ID, defaults=evaluation)
            evaluation_ids.append(evaluation_instance.pk)
        return evaluation_ids

    def update_or_create_evaluations(self, evaluations):
        evaluation_ids = []
        for evaluation in evaluations:
            evaluation_instance, created = Evaluation.objects.update_or_create(pk=evaluation.ID, defaults=evaluation)
            evaluation_ids.append(evaluation_instance.pk)
        return evaluation_ids

    def get_or_create_xrevents(self, xrevents):
        xrevent_ids = []
        for xrevent in xrevents:
            xrevent_instance, created = XREvent.objects.get_or_create(pk=xrevent.ID, defaults=xrevent)
            xrevent_ids.append(xrevent_instance.pk)
        return xrevent_ids

    def update_or_create_xrevents(self, xrevents):
        xrevent_ids = []
        for xrevent in xrevents:
            xrevent_instance, created = XREvent.objects.update_or_create(pk=xrevent.ID, defaults=xrevent)
            xrevent_ids.append(xrevent_instance.pk)
        return xrevent_ids

    class Meta: 
        model = SeparatedScenario
        fields = '__all__'

    def create(self, validated_data):
        evaluations = validated_data.pop("Evaluations")
        xrevents = validated_data.pop("XREvents")
        instance = CombinedScenario.objects.create(**validated_data)
        instance.save()
        instance.Evaluations.set(self.get_or_create_evaluations(evaluations))
        instance.XREvents.set(self.get_or_create_xrevents(xrevents))
        return instance


class CombinedScenarioSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    Facility = serializers.ChoiceField(choices=[(value, key) for key, value in proto.FacilityType.items()], default=0)
    Scenarios = serializers.SlugRelatedField(many=True, slug_field='ID', queryset=SeparatedScenario.objects.all())
    
    class Meta: 
        model = CombinedScenario
        fields = '__all__'

    def get_or_create_separated_scenarios(self, scenarios):
        scenario_ids = []
        for scenario in scenarios:
            scenario_instance, created = SeparatedScenario.objects.get_or_create(pk=scenario.ID, defaults=scenario)
            scenario_ids.append(scenario_instance.pk)
        return scenario_ids

    def update_or_create_separated_scenarios(self, scenarios):
        scenario_ids = []
        for scenario in scenarios:
            scenario_instance, created = SeparatedScenario.objects.update_or_create(pk=scenario.ID, defaults=scenario)
            scenario_ids.append(scenario_instance.pk)
        return scenario_ids

    def create(self, validated_data):
        separated_scenarios = validated_data.pop("Scenarios")
        instance = CombinedScenario.objects.create(**validated_data)
        instance.save()
        instance.Scenarios.set(self.get_or_create_separated_scenarios(separated_scenarios))
        return instance

    def update(self, instance, validated_data):
        instance.save()
        return instance
    
