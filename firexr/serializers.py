from pkg_resources import require
from rest_framework import serializers 
from firexr.models import * 
import firexr.proto.firexr_scenario_pb2 as proto
import json


###
### Util
###
class TextInputListField(serializers.ListField):
    #child = serializers.CharField()

    def __init__(self, *args, **kwargs):
        style = {'base_template':  'input.html'}
        super().__init__(*args, style=style, **kwargs)
    
    def get_value(self, dictionary):
        value = super().get_value(dictionary)
        is_querydict = hasattr(dictionary, 'getlist')
        is_form = 'csrfmiddlewaretoken' in dictionary
        if value and is_querydict and is_form:
            try:
                value = json.loads(value[0])
            except Exception:
                pass
        return value
        
###
### Unit Serializers
###

class TransformSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField()

    class Meta: 
        model = Transform
        fields = '__all__'

    def create(self, validated_data):
        return Transform.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance = Transform.objects.update(**validated_data)
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

    ActivateObjects = serializers.SlugRelatedField(many=True, slug_field='ID', queryset=ObjectInfo.objects.all())
    DeactivateObjects = serializers.SlugRelatedField(many=True, slug_field='ID', queryset=ObjectInfo.objects.all())

    def get_or_create_objinfo(self, objinfos):
        objinfo_ids = []
        for objinfo in objinfos:
            objinfo_instance, created = ObjectInfo.objects.get_or_create(pk=objinfo.ID, defaults=objinfo)
            objinfo_ids.append(objinfo_instance.pk)
        return objinfo_ids

    def update_or_create_objinfo(self, objinfos):
        objinfo_ids = []
        for objinfo in objinfos:
            objinfo_instance, created = ObjectInfo.objects.update_or_create(pk=objinfo.ID, defaults=objinfo)
            objinfo_ids.append(objinfo_instance.pk)
        return objinfo_ids
    
    class Meta: 
        model = ObjectInfo
        fields = '__all__'


    def create(self, validated_data):
        activate_objects = validated_data.pop("ActivateObjects")
        deactivate_objects = validated_data.pop("DeactivateObjects")
        instance = ObjectInfo.objects.create(**validated_data)
        instance.save()
        instance.ActivateObjects.set(self.get_or_create_objinfo(activate_objects))
        instance.DeactivateObjects.set(self.get_or_create_objinfo(deactivate_objects))
        return instance

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
    
    FDSFiles = serializers.SlugRelatedField(many=True, slug_field='ID', queryset=FDSFile.objects.all())
    
    def get_or_create_fdsfiles(self, fdsfiles):
        fdsfile_ids = []
        for fdsfile in fdsfiles:
            fdsfile_instance, created = FDSFile.objects.get_or_create(pk=fdsfile.ID, defaults=fdsfile)
            fdsfile_ids.append(fdsfile_instance.pk)
        return fdsfile_ids

    def update_or_create_fdsfiles(self, fdsfiles):
        fdsfile_ids = []
        for fdsfile in fdsfiles:
            fdsfile_instance, created = FDSFile.objects.update_or_create(pk=fdsfile.ID, defaults=fdsfile)
            fdsfile_ids.append(fdsfile_instance.pk)
        return fdsfile_ids


    class Meta: 
        model = FDS
        fields = '__all__'

    def create(self, validated_data):
        fdsfiles = validated_data.pop("FDSFiles")
        instance = FDS.objects.create(**validated_data)
        instance.save()
        instance.FDSFiles.set(self.get_or_create_fdsfiles(fdsfiles))
        return instance

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
    
    def get_or_create_evaluation_actions(self, evaluation_actions):
        evaluation_action_ids = []
        for evaluation_action in evaluation_actions:
            evaluation_action_instance, created = EvaluationAction.objects.get_or_create(pk=evaluation_action.ID, defaults=evaluation_action)
            evaluation_action_ids.append(evaluation_action_instance.pk)
        return evaluation_action_ids

    def update_or_create_evaluation_actions(self, evaluation_actions):
        evaluation_action_ids = []
        for evaluation_action in evaluation_actions:
            evaluation_action_instance, created = EvaluationAction.objects.update_or_create(pk=evaluation_action.ID, defaults=evaluation_action)
            evaluation_action_ids.append(evaluation_action_instance.pk)
        return evaluation_action_ids

    class Meta: 
        model = Evaluation
        fields = '__all__'

    def create(self, validated_data):
        evaluation_actions = validated_data.pop("EvaluationActions")
        instance = Evaluation.objects.create(**validated_data)
        instance.save()
        instance.EvaluationActions.set(self.get_or_create_evaluation_actions(evaluation_actions))
        return instance

    def update(self, instance, validated_data):
        instance = Evaluation.objects.update(**validated_data)
        return instance
    

class SeparatedScenarioSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    Version = serializers.IntegerField(default=1)
    Category = TextInputListField()
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
        instance = SeparatedScenario.objects.create(**validated_data)
        instance.save()
        instance.Evaluations.set(self.get_or_create_evaluations(evaluations))
        instance.XREvents.set(self.get_or_create_xrevents(xrevents))
        return instance

    def update(self, instance, validated_data):
        instance = SeparatedScenario.objects.update(**validated_data)
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
        instance = CombinedScenario.objects.update(**validated_data)
        return instance
    





###
### Integrated Scenario Serializers
###

class IntegratedTransformSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)

    class Meta: 
        model = Transform
        fields = '__all__'

    def create(self, validated_data):
        return Transform.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance
        
class IntegratedInteractionPointSerializer(serializers.ModelSerializer): 
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
        
class IntegratedCutSceneSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    
    class Meta: 
        model = CutScene
        fields = '__all__'

    def create(self, validated_data):
        return CutScene.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance
        
class IntegratedObjectInfoSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)

    ActivateObjects = serializers.SlugRelatedField(many=True, slug_field='ID', queryset=ObjectInfo.objects.all())
    DeactivateObjects = serializers.SlugRelatedField(many=True, slug_field='ID', queryset=ObjectInfo.objects.all())

    class Meta: 
        model = ObjectInfo
        fields = '__all__'

        
class IntegratedSoundSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    
    class Meta: 
        model = Sound
        fields = '__all__'

    def create(self, validated_data):
        return Sound.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance
        
class IntegratedFDSFileSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    
    class Meta: 
        model = FDSFile
        fields = '__all__'

class IntegratedFDSSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    FDSFiles = IntegratedFDSFileSerializer(read_only=True, many=True)

    class Meta: 
        model = FDS
        fields = '__all__'
        
class IntegratedXREventSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    
    class Meta: 
        model = XREvent
        fields = '__all__'

class IntegratedEvaluationActionSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    
    class Meta: 
        model = EvaluationAction
        fields = '__all__'

class IntegratedEvaluationSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    EvaluationActions = IntegratedEvaluationActionSerializer(read_only=True, many=True)
    
    class Meta: 
        model = Evaluation
        fields = '__all__'

class IntegratedSeparatedScenarioSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    Version = serializers.IntegerField(default=1)
    Category = TextInputListField()
    Facility = serializers.ChoiceField(choices=[(value, key) for key, value in proto.FacilityType.items()], default=0)
    Evaluations = IntegratedEvaluationSerializer(read_only=True, many=True)
    XREvents = IntegratedXREventSerializer(read_only=True, many=True)

    class Meta: 
        model = SeparatedScenario
        fields = '__all__'

class IntegratedCombinedScenarioSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(read_only=True)
    Facility = serializers.ChoiceField(choices=[(value, key) for key, value in proto.FacilityType.items()], default=0)
    Scenarios = IntegratedSeparatedScenarioSerializer(read_only=True, many=True)
    
    class Meta: 
        model = CombinedScenario
        fields = '__all__'
    

