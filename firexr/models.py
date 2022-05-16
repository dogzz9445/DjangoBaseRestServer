from django.db import models
from pb_model.models import ProtoBufMixin
from django.core.validators import int_list_validator
import firexr.proto.firexr_scenario_pb2 as proto

# Create your models here.

class Transform(ProtoBufMixin, models.Model):
    pb_model = proto.Transform
    pb_2_dj_fields = '__all__'

    ID = models.IntegerField(primary_key=True, auto_created=True, editable=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.pk: # new instance
            last = Transform.objects.last()
            if last is None:
                self.ID = 1
            else:
                self.ID = last.ID + 1
        return super().save(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        model = None
        id = request.data.get('ID')
        if id:
            model = self.get_object(ID=id)
        
        if model:
            return self.update(request, *args, **kwargs)
        else:
            return self.create(request, *args, **kwargs)

class InteractionPoint(ProtoBufMixin, models.Model):
    pb_model = proto.InteractionPoint
    pb_2_dj_fields = '__all__'

    ID = models.IntegerField(primary_key=True, auto_created=True, editable=False, unique=True)
    Facility = models.IntegerField(choices=proto.FacilityType.items(), default=0)
    LocalTransform = models.OneToOneField(Transform, related_name='transformposes', on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk: # new instance
            last = InteractionPoint.objects.last()
            if last is None:
                self.ID = 1
            else:
                self.ID = last.ID + 1
        return super().save(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        model = None
        id = request.data.get('ID')
        if id:
            model = self.get_object(ID=id)
        
        if model:
            return self.update(request, *args, **kwargs)
        else:
            return self.create(request, *args, **kwargs)


class CutScene(ProtoBufMixin, models.Model):
    pb_model = proto.CutScene
    pb_2_dj_fields = '__all__'

    ID = models.IntegerField(primary_key=True, auto_created=True, editable=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.pk: # new instance
            last = CutScene.objects.last()
            if last is None:
                self.ID = 1
            else:
                self.ID = last.ID + 1
        return super().save(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        model = None
        id = request.data.get('ID')
        if id:
            model = self.get_object(ID=id)
        
        if model:
            return self.update(request, *args, **kwargs)
        else:
            return self.create(request, *args, **kwargs)


class ObjectInfo(ProtoBufMixin, models.Model):
    pb_model = proto.ObjectInfo
    pb_2_dj_fields = '__all__'

    ID = models.IntegerField(primary_key=True, auto_created=True, editable=False, unique=True)
    ActivateObjects = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='activate_objects')
    DeactivateObjects = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='deactivate_objects')

    def save(self, *args, **kwargs):
        if not self.pk: # new instance
            last = ObjectInfo.objects.last()
            if last is None:
                self.ID = 1
            else:
                self.ID = last.ID + 1
        return super().save(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        model = None
        id = request.data.get('ID')
        if id:
            model = self.get_object(ID=id)
        
        if model:
            return self.update(request, *args, **kwargs)
        else:
            return self.create(request, *args, **kwargs)


class Sound(ProtoBufMixin, models.Model):
    pb_model = proto.Sound
    pb_2_dj_fields = '__all__'
    ID = models.IntegerField(primary_key=True, auto_created=True, editable=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.pk: # new instance
            last = Sound.objects.last()
            if last is None:
                self.ID = 1
            else:
                self.ID = last.ID + 1
        return super().save(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        model = None
        id = request.data.get('ID')
        if id:
            model = self.get_object(ID=id)
        
        if model:
            return self.update(request, *args, **kwargs)
        else:
            return self.create(request, *args, **kwargs)


class FDSFile(ProtoBufMixin, models.Model):
    pb_model = proto.FDSFile
    pb_2_dj_fields = '__all__'
    ID = models.IntegerField(primary_key=True, auto_created=True, editable=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.pk: # new instance
            last = FDSFile.objects.last()
            if last is None:
                self.ID = 1
            else:
                self.ID = last.ID + 1
        return super().save(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        model = None
        id = request.data.get('ID')
        if id:
            model = self.get_object(ID=id)
        
        if model:
            return self.update(request, *args, **kwargs)
        else:
            return self.create(request, *args, **kwargs)


class XREvent(ProtoBufMixin, models.Model):
    pb_model = proto.XREvent
    pb_2_dj_fields = '__all__'
    ID = models.IntegerField(primary_key=True, auto_created=True, editable=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.pk: # new instance
            last = XREvent.objects.last()
            if last is None:
                self.ID = 1
            else:
                self.ID = last.ID + 1
        return super().save(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        model = None
        id = request.data.get('ID')
        if id:
            model = self.get_object(ID=id)
        
        if model:
            return self.update(request, *args, **kwargs)
        else:
            return self.create(request, *args, **kwargs)


class FDS(ProtoBufMixin, models.Model):
    pb_model = proto.FDS
    pb_2_dj_fields = '__all__'

    ID = models.IntegerField(primary_key=True, auto_created=True, editable=False, unique=True)
    FDSFiles = models.ManyToManyField(FDSFile, symmetrical=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk: # new instance
            last = FDS.objects.last()
            if last is None:
                self.ID = 1
            else:
                self.ID = last.ID + 1
        return super().save(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        model = None
        id = request.data.get('ID')
        if id:
            model = self.get_object(ID=id)
        
        if model:
            return self.update(request, *args, **kwargs)
        else:
            return self.create(request, *args, **kwargs)


class EvaluationAction(ProtoBufMixin, models.Model):
    pb_model = proto.EvaluationAction
    pb_2_dj_fields = '__all__'
    ID = models.IntegerField(primary_key=True, auto_created=True, editable=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.pk: # new instance
            last = EvaluationAction.objects.last()
            if last is None:
                self.ID = 1
            else:
                self.ID = last.ID + 1
        return super().save(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        model = None
        id = request.data.get('ID')
        if id:
            model = self.get_object(ID=id)
        
        if model:
            return self.update(request, *args, **kwargs)
        else:
            return self.create(request, *args, **kwargs)


class Evaluation(ProtoBufMixin, models.Model):
    pb_model = proto.Evaluation
    pb_2_dj_fields = '__all__'
    
    ID = models.IntegerField(primary_key=True, auto_created=True, editable=False, unique=True)
    EvaluationActions = models.ManyToManyField(EvaluationAction, symmetrical=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk: # new instance
            last = Evaluation.objects.last()
            if last is None:
                self.ID = 1
            else:
                self.ID = last.ID + 1
        return super().save(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        model = None
        id = request.data.get('ID')
        if id:
            model = self.get_object(ID=id)
        
        if model:
            return self.update(request, *args, **kwargs)
        else:
            return self.create(request, *args, **kwargs)


class SeparatedScenario(ProtoBufMixin, models.Model):
    pb_model = proto.SeparatedScenario
    pb_2_dj_fields = '__all__'

    ID = models.IntegerField(primary_key=True, auto_created=True, editable=False, unique=True)
    Category = models.JSONField()
    Facility = models.IntegerField(choices=proto.FacilityType.items(), default=0)
    Evaluations = models.ManyToManyField(Evaluation, symmetrical=False, blank=True)
    XREvents = models.ManyToManyField(XREvent, symmetrical=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk: # new instance
            last = SeparatedScenario.objects.last()
            if last is None:
                self.ID = 1
            else:
                self.ID = last.ID + 1
        return super().save(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        model = None
        id = request.data.get('ID')
        if id:
            model = self.get_object(ID=id)
        
        if model:
            return self.update(request, *args, **kwargs)
        else:
            return self.create(request, *args, **kwargs)


class CombinedScenario(ProtoBufMixin, models.Model):
    pb_model = proto.CombinedScenario
    pb_2_dj_fields = '__all__'

    ID = models.IntegerField(primary_key=True, auto_created=True, editable=False, unique=True)
    Facility = models.IntegerField(choices=proto.FacilityType.items(), default=0)
    Scenarios = models.ManyToManyField(SeparatedScenario, symmetrical=False, blank=True, related_name='combined_scenario')

    def save(self, *args, **kwargs):
        if not self.pk: # new instance
            last = CombinedScenario.objects.last()
            if last is None:
                self.ID = 1
            else:
                self.ID = last.ID + 1
        return super().save(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        model = None
        id = request.data.get('ID')
        if id:
            model = self.get_object(ID=id)
        
        if model:
            return self.update(request, *args, **kwargs)
        else:
            return self.create(request, *args, **kwargs)

