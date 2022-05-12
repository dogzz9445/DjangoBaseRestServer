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
            self.ID = CombinedScenario.objects.last().ID + 1
        return super().save(*args, **kwargs)


class InteractionPoint(ProtoBufMixin, models.Model):
    pb_model = proto.InteractionPoint
    pb_2_dj_fields = '__all__'

    ID = models.IntegerField(primary_key=True, auto_created=True, editable=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.pk: # new instance
            self.ID = CombinedScenario.objects.last().ID + 1
        return super().save(*args, **kwargs)

class CutScene(ProtoBufMixin, models.Model):
    pb_model = proto.CutScene
    pb_2_dj_fields = '__all__'

    ID = models.IntegerField(primary_key=True, auto_created=True, editable=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.pk: # new instance
            self.ID = CombinedScenario.objects.last().ID + 1
        return super().save(*args, **kwargs)

class ObjectInfo(ProtoBufMixin, models.Model):
    pb_model = proto.ObjectInfo
    pb_2_dj_fields = '__all__'

    ID = models.IntegerField(primary_key=True, auto_created=True, editable=False, unique=True)
    ActivateObjects = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='activate_objects')
    DeactivateObjects = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='deactivate_objects')

    def save(self, *args, **kwargs):
        if not self.pk: # new instance
            self.ID = CombinedScenario.objects.last().ID + 1
        return super().save(*args, **kwargs)

class Sound(ProtoBufMixin, models.Model):
    pb_model = proto.Sound
    pb_2_dj_fields = '__all__'
    ID = models.IntegerField(primary_key=True, auto_created=True, editable=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.pk: # new instance
            self.ID = CombinedScenario.objects.last().ID + 1
        return super().save(*args, **kwargs)

class FDSFile(ProtoBufMixin, models.Model):
    pb_model = proto.FDSFile
    pb_2_dj_fields = '__all__'
    ID = models.IntegerField(primary_key=True, auto_created=True, editable=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.pk: # new instance
            self.ID = CombinedScenario.objects.last().ID + 1
        return super().save(*args, **kwargs)

class XREvent(ProtoBufMixin, models.Model):
    pb_model = proto.XREvent
    pb_2_dj_fields = '__all__'
    ID = models.IntegerField(primary_key=True, auto_created=True, editable=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.pk: # new instance
            self.ID = CombinedScenario.objects.last().ID + 1
        return super().save(*args, **kwargs)

class FDS(ProtoBufMixin, models.Model):
    pb_model = proto.FDS
    pb_2_dj_fields = '__all__'

    ID = models.IntegerField(primary_key=True, auto_created=True, editable=False, unique=True)
    FDSFileID = models.ManyToManyField(FDSFile, symmetrical=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk: # new instance
            self.ID = CombinedScenario.objects.last().ID + 1
        return super().save(*args, **kwargs)

class Evaluation(ProtoBufMixin, models.Model):
    pb_model = proto.Evaluation
    pb_2_dj_fields = '__all__'
    ID = models.IntegerField(primary_key=True, auto_created=True, editable=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.pk: # new instance
            self.ID = CombinedScenario.objects.last().ID + 1
        return super().save(*args, **kwargs)

class EvaluationAction(ProtoBufMixin, models.Model):
    pb_model = proto.EvaluationAction
    pb_2_dj_fields = '__all__'
    ID = models.IntegerField(primary_key=True, auto_created=True, editable=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.pk: # new instance
            self.ID = CombinedScenario.objects.last().ID + 1
        return super().save(*args, **kwargs)

class SeparatedScenario(ProtoBufMixin, models.Model):
    pb_model = proto.SeparatedScenario
    pb_2_dj_fields = '__all__'

    ID = models.IntegerField(primary_key=True, auto_created=True, editable=False, unique=True)
    Category = models.CharField(max_length=256, default='')
    Evaluations = models.ManyToManyField(Evaluation, symmetrical=False, blank=True)
    XREvents = models.ManyToManyField(XREvent, symmetrical=False, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk: # new instance
            self.ID = CombinedScenario.objects.last().ID + 1
        return super().save(*args, **kwargs)

class CombinedScenario(ProtoBufMixin, models.Model):
    pb_model = proto.CombinedScenario
    pb_2_dj_fields = '__all__'

    ID = models.IntegerField(primary_key=True, auto_created=True, editable=False, unique=True)
    Scenarios = models.ManyToManyField(SeparatedScenario, symmetrical=False, blank=True, related_name='combined_scenario')

    def save(self, *args, **kwargs):
        if not self.pk: # new instance
            self.ID = CombinedScenario.objects.last().ID + 1
        return super().save(*args, **kwargs)
