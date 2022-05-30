from pkg_resources import require
from rest_framework import serializers 
from django.core.exceptions import ObjectDoesNotExist
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

class CreatableSlugRelatedField(serializers.SlugRelatedField):
    
    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(**{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            self.fail('does_not_exist', slug_name=self.slug_field, value=data)
        except (TypeError, ValueError):
            self.fail('invalid')

###
### Unit Serializers
###

class TransformSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(allow_null=True)
    Name = serializers.CharField(allow_blank=True)
    Desc = serializers.CharField(allow_blank=True)

    class Meta: 
        model = Transform
        fields = '__all__'

    def create(self, validated_data):
        content_id = validated_data.pop('ID')
        instance, created = Transform.objects.get_or_create(ID=content_id, defaults=validated_data)
        if not created:
            for field, value in validated_data.items():
                setattr(instance, field, value)
        return instance

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
        
class InteractionPointSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(allow_null=True)
    Type = serializers.CharField(allow_blank=True)
    Contents = serializers.CharField(allow_blank=True)
    Desc = serializers.CharField(allow_blank=True)
    Facility = serializers.ChoiceField(choices=[(value, key) for key, value in proto.FacilityType.items()], default=0)
    LocalTransform = CreatableSlugRelatedField(many=False, slug_field='ID', queryset=Transform.objects.all())
    
    class Meta: 
        model = InteractionPoint
        fields = '__all__'

    def create(self, validated_data):
        transform_id = validated_data.pop("LocalTransform")
        content_id = validated_data.pop('ID')
        instance, created = InteractionPoint.objects.get_or_create(ID=content_id, defaults=validated_data)
        if not created:
            for field, value in validated_data.items():
                setattr(instance, field, value)
        instance.LocalTransform = transform_id
        instance.save()
        return instance

    def update(self, instance, validated_data):
        transformid = validated_data.pop("LocalTransform")
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.LocalTransform = transformid
        instance.save()
        return instance
        
class CutSceneSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(allow_null=True)
    Type = serializers.CharField(allow_blank=True)
    FileName = serializers.CharField(allow_blank=True)
    Desc = serializers.CharField(allow_blank=True)
    
    class Meta: 
        model = CutScene
        fields = '__all__'

    def create(self, validated_data):
        content_id = validated_data.pop('ID')
        instance, created = CutScene.objects.get_or_create(ID=content_id, defaults=validated_data)
        if not created:
            for field, value in validated_data.items():
                setattr(instance, field, value)
            instance.save()
        return instance

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
        
class ObjectInfoSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(allow_null=True)
    Name = serializers.CharField(allow_null=True, allow_blank=True, default=None, required=False)
    Type = serializers.CharField(allow_null=True, allow_blank=True, default=None, required=False)
    FileName = serializers.CharField(allow_null=True, allow_blank=True, default=None, required=False)
    Desc = serializers.CharField(allow_null=True, allow_blank=True, default=None, required=False)

    ActivateObjects = CreatableSlugRelatedField(many=True, slug_field='ID', queryset=ObjectInfo.objects.all())
    DeactivateObjects = CreatableSlugRelatedField(many=True, slug_field='ID', queryset=ObjectInfo.objects.all())

    def get_or_create_objinfo(self, objinfos):
        objinfo_ids = []
        for objinfo in objinfos:
            objinfo_instance, created = ObjectInfo.objects.get_or_create(ID=objinfo.ID, defaults=objinfo)
            objinfo_ids.append(objinfo_instance.pk)
        return objinfo_ids

    class Meta: 
        model = ObjectInfo
        fields = '__all__'


    def create(self, validated_data):
        activate_objects = validated_data.pop("ActivateObjects")
        deactivate_objects = validated_data.pop("DeactivateObjects")
        content_id = validated_data.pop('ID')
        instance, created = ObjectInfo.objects.get_or_create(ID=content_id, defaults=validated_data)
        if not created:
            for field, value in validated_data.items():
                setattr(instance, field, value)
        instance.ActivateObjects.set(self.get_or_create_objinfo(activate_objects))
        instance.DeactivateObjects.set(self.get_or_create_objinfo(deactivate_objects))
        instance.save()
        return instance

    def update(self, instance, validated_data):
        activate_objects = validated_data.pop("ActivateObjects")
        deactivate_objects = validated_data.pop("DeactivateObjects")
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.ActivateObjects.set(self.get_or_create_objinfo(activate_objects))
        instance.DeactivateObjects.set(self.get_or_create_objinfo(deactivate_objects))
        instance.save()
        return instance
        
class SoundSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(allow_null=True)
    Type = serializers.CharField(allow_blank=True)
    FileName = serializers.CharField(allow_blank=True)
    Desc = serializers.CharField(allow_blank=True)
    
    class Meta: 
        model = Sound
        fields = '__all__'

    def create(self, validated_data):
        content_id = validated_data.pop('ID')
        instance, created = Sound.objects.get_or_create(ID=content_id, defaults=validated_data)
        if not created:
            for field, value in validated_data.items():
                setattr(instance, field, value)
            instance.save()
        return instance

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
        
class FDSFileSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(allow_null=True)
    DataType = serializers.CharField(allow_blank=True)
    DeviceType = serializers.CharField(allow_blank=True)
    FileName = serializers.CharField(allow_blank=True)
    Desc = serializers.CharField(allow_blank=True)
    
    class Meta: 
        model = FDSFile
        fields = '__all__'

    def create(self, validated_data):
        content_id = validated_data.pop('ID')
        instance, created = FDSFile.objects.get_or_create(ID=content_id, defaults=validated_data)
        if not created:
            for field, value in validated_data.items():
                setattr(instance, field, value)
            instance.save()
        return instance

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
        
class FDSSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(allow_null=True)
    Desc = serializers.CharField(allow_blank=True)
    
    FDSFiles = CreatableSlugRelatedField(many=True, slug_field='ID', queryset=FDSFile.objects.all())
    
    def get_or_create_fdsfiles(self, fdsfiles):
        fdsfile_ids = []
        for fdsfile in fdsfiles:
            fdsfile_instance, created = FDSFile.objects.get_or_create(pk=fdsfile.ID, defaults=fdsfile)
            fdsfile_ids.append(fdsfile_instance.pk)
        return fdsfile_ids

    class Meta: 
        model = FDS
        fields = '__all__'

    def create(self, validated_data):
        fdsfiles = validated_data.pop("FDSFiles")
        content_id = validated_data.pop('ID')
        instance, created = FDS.objects.get_or_create(ID=content_id, defaults=validated_data)
        if not created:
            for field, value in validated_data.items():
                setattr(instance, field, value)
        instance.FDSFiles.set(self.get_or_create_fdsfiles(fdsfiles))
        instance.save()
        return instance

    def update(self, instance, validated_data):
        fdsfiles = validated_data.pop("FDSFiles")
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.FDSFiles.set(self.get_or_create_fdsfiles(fdsfiles))
        instance.save()
        return instance
        
class XREventSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(allow_null=True)
    Action = serializers.CharField(allow_blank=True)
    Target = serializers.CharField(allow_blank=True)
    Contents = serializers.CharField(allow_blank=True)
    Desc = serializers.CharField(allow_blank=True)
    
    class Meta: 
        model = XREvent
        fields = '__all__'

    def create(self, validated_data):
        content_id = validated_data.pop('ID')
        instance, created = XREvent.objects.get_or_create(ID=content_id, defaults=validated_data)
        if not created:
            for field, value in validated_data.items():
                setattr(instance, field, value)
            instance.save()
        return instance

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
        
class EvaluationActionSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(allow_null=True)
    Action = serializers.CharField(allow_blank=True)
    Desc = serializers.CharField(allow_blank=True)
    
    class Meta: 
        model = EvaluationAction
        fields = '__all__'

    def create(self, validated_data):
        content_id = validated_data.pop('ID')
        instance, created = EvaluationAction.objects.get_or_create(ID=content_id, defaults=validated_data)
        if not created:
            for field, value in validated_data.items():
                setattr(instance, field, value)
            instance.save()
        return instance

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
        
class EvaluationSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(allow_null=True)
    Category = serializers.CharField(allow_blank=True)
    Action = serializers.CharField(allow_blank=True)
    Type = serializers.CharField(allow_blank=True)
    Contents = serializers.CharField(allow_blank=True)
    Desc = serializers.CharField(allow_blank=True)
    EvaluationActions = CreatableSlugRelatedField(many=True, slug_field='ID', queryset=EvaluationAction.objects.all())
    
    def get_or_create_evaluation_actions(self, evaluation_actions):
        evaluation_action_ids = []
        for evaluation_action in evaluation_actions:
            evaluation_action_instance, created = EvaluationAction.objects.get_or_create(pk=evaluation_action.ID, defaults=evaluation_action)
            evaluation_action_ids.append(evaluation_action_instance.pk)
        return evaluation_action_ids

    # def update_or_create_evaluation_actions(self, evaluation_actions):
    #     evaluation_action_ids = []
    #     for evaluation_action in evaluation_actions:
    #         evaluation_action_instance, created = EvaluationAction.objects.update_or_create(pk=evaluation_action.ID, defaults=evaluation_action)
    #         evaluation_action_ids.append(evaluation_action_instance.pk)
    #     return evaluation_action_ids

    class Meta: 
        model = Evaluation
        fields = '__all__'

    def create(self, validated_data):
        evaluation_actions = validated_data.pop("EvaluationActions")
        content_id = validated_data.pop('ID')
        instance, created = EvaluationAction.objects.get_or_create(ID=content_id, defaults=validated_data)
        if not created:
            for field, value in validated_data.items():
                setattr(instance, field, value)
        instance.EvaluationActions.set(self.get_or_create_evaluation_actions(evaluation_actions))
        instance.save()
        return instance

    def update(self, instance, validated_data):
        evaluation_actions = validated_data.pop("EvaluationActions")
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.EvaluationActions.set(self.get_or_create_evaluation_actions(evaluation_actions))
        instance.save()
        return instance
    

class SeparatedScenarioSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(allow_null=True)
    Version = serializers.IntegerField(default=1)
    Category = TextInputListField()
    Title = serializers.CharField(allow_blank=True)
    Description = serializers.CharField(allow_blank=True)
    Facility = serializers.ChoiceField(choices=[(value, key) for key, value in proto.FacilityType.items()], default=0)
    Evaluations = CreatableSlugRelatedField(many=True, slug_field='ID', queryset=Evaluation.objects.all())
    XREvents = CreatableSlugRelatedField(many=True, slug_field='ID', queryset=XREvent.objects.all())
    
    def get_or_create_evaluations(self, evaluations):
        evaluation_ids = []
        for evaluation in evaluations:
            evaluation_instance, created = Evaluation.objects.get_or_create(pk=evaluation.ID, defaults=evaluation)
            evaluation_ids.append(evaluation_instance.pk)
        return evaluation_ids

    def get_or_create_xrevents(self, xrevents):
        xrevent_ids = []
        for xrevent in xrevents:
            xrevent_instance, created = XREvent.objects.get_or_create(pk=xrevent.ID, defaults=xrevent)
            xrevent_ids.append(xrevent_instance.pk)
        return xrevent_ids

    class Meta: 
        model = SeparatedScenario
        fields = '__all__'

    def create(self, validated_data):
        evaluations = validated_data.pop("Evaluations")
        xrevents = validated_data.pop("XREvents")
        content_id = validated_data.pop('ID')
        instance, created = EvaluationAction.objects.get_or_create(ID=content_id, defaults=validated_data)
        if not created:
            for field, value in validated_data.items():
                setattr(instance, field, value)
        instance.Evaluations.set(self.get_or_create_evaluations(evaluations))
        instance.XREvents.set(self.get_or_create_xrevents(xrevents))
        instance.save()
        return instance

    def update(self, instance, validated_data):
        evaluations = validated_data.pop("Evaluations")
        xrevents = validated_data.pop("XREvents")
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.Evaluations.set(self.get_or_create_evaluations(evaluations))
        instance.XREvents.set(self.get_or_create_xrevents(xrevents))
        instance.save()
        return instance
    


class CombinedScenarioSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(allow_null=True)
    Title = serializers.CharField(allow_blank=True)
    Description = serializers.CharField(allow_blank=True)
    Facility = serializers.ChoiceField(choices=[(value, key) for key, value in proto.FacilityType.items()], default=0)
    Scenarios = CreatableSlugRelatedField(many=True, slug_field='ID', queryset=SeparatedScenario.objects.all())
    
    class Meta: 
        model = CombinedScenario
        fields = '__all__'

    def get_or_create_separated_scenarios(self, scenarios):
        scenario_ids = []
        for scenario in scenarios:
            scenario_instance, created = SeparatedScenario.objects.get_or_create(pk=scenario.ID, defaults=scenario)
            scenario_ids.append(scenario_instance.pk)
        return scenario_ids

    def create(self, validated_data):
        separated_scenarios = validated_data.pop("Scenarios")
        content_id = validated_data.pop('ID')
        instance, created = EvaluationAction.objects.get_or_create(ID=content_id, defaults=validated_data)
        if not created:
            for field, value in validated_data.items():
                setattr(instance, field, value)
        instance.Scenarios.set(self.get_or_create_separated_scenarios(separated_scenarios))
        instance.save()
        return instance

    def update(self, instance, validated_data):
        separated_scenarios = validated_data.pop("Scenarios")
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.Scenarios.set(self.get_or_create_separated_scenarios(separated_scenarios))
        instance.save()
        return instance
    

###
### Integrated Scenario Serializers
###

class IntegratedTransformSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(allow_null=True)

    class Meta: 
        model = Transform
        fields = '__all__'

    def create(self, validated_data):
        return Transform.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance
        
class IntegratedInteractionPointSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(allow_null=True)
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
    ID = serializers.IntegerField(allow_null=True)
    
    class Meta: 
        model = CutScene
        fields = '__all__'

    def create(self, validated_data):
        return CutScene.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance
        
class IntegratedObjectInfoSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(allow_null=True)

    ActivateObjects = CreatableSlugRelatedField(many=True, slug_field='ID', queryset=ObjectInfo.objects.all())
    DeactivateObjects = CreatableSlugRelatedField(many=True, slug_field='ID', queryset=ObjectInfo.objects.all())

    class Meta: 
        model = ObjectInfo
        fields = '__all__'

        
class IntegratedSoundSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(allow_null=True)
    
    class Meta: 
        model = Sound
        fields = '__all__'

    def create(self, validated_data):
        return Sound.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance
        
class IntegratedFDSFileSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(allow_null=True)
    
    class Meta: 
        model = FDSFile
        fields = '__all__'

class IntegratedFDSSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(allow_null=True)
    FDSFiles = IntegratedFDSFileSerializer(read_only=True, many=True)

    class Meta: 
        model = FDS
        fields = '__all__'
        
class IntegratedXREventSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(allow_null=True)
    
    class Meta: 
        model = XREvent
        fields = '__all__'

class IntegratedEvaluationActionSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(allow_null=True)
    
    class Meta: 
        model = EvaluationAction
        fields = '__all__'

class IntegratedEvaluationSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(allow_null=True)
    EvaluationActions = IntegratedEvaluationActionSerializer(read_only=True, many=True)
    
    class Meta: 
        model = Evaluation
        fields = '__all__'

class IntegratedSeparatedScenarioSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(allow_null=True)
    Version = serializers.IntegerField(default=1)
    Category = TextInputListField()
    Facility = serializers.ChoiceField(choices=[(value, key) for key, value in proto.FacilityType.items()], default=0)
    Evaluations = IntegratedEvaluationSerializer(read_only=True, many=True)
    XREvents = IntegratedXREventSerializer(read_only=True, many=True)

    class Meta: 
        model = SeparatedScenario
        fields = '__all__'

class IntegratedCombinedScenarioSerializer(serializers.ModelSerializer): 
    ID = serializers.IntegerField(allow_null=True)
    Facility = serializers.ChoiceField(choices=[(value, key) for key, value in proto.FacilityType.items()], default=0)
    Scenarios = IntegratedSeparatedScenarioSerializer(read_only=True, many=True)
    
    class Meta: 
        model = CombinedScenario
        fields = '__all__'
    

