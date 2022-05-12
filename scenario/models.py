import uuid
from django.db import models
from colorfield.fields import ColorField
import scenario.proto.firexr_scenario_pb2 as proto
from pb_model.models import ProtoBufMixin

class Transform(ProtoBufMixin, models.Model):
    pb_model = proto.Transform
    pb_2_dj_fields = '__all__'

class InteractionPoint(ProtoBufMixin, models.Model):
    pb_model = proto.InteractionPoint
    pb_2_dj_fields = '__all__'

class CutScene(ProtoBufMixin, models.Model):
    pb_model = proto.CutScene
    pb_2_dj_fields = '__all__'

class ObjectInfo(ProtoBufMixin, models.Model):
    pb_model = proto.ObjectInfo
    pb_2_dj_fields = '__all__'

class Sound(ProtoBufMixin, models.Model):
    pb_model = proto.Sound
    pb_2_dj_fields = '__all__'

class FDSFile(ProtoBufMixin, models.Model):
    pb_model = proto.FDSFile
    pb_2_dj_fields = '__all__'

class XREvent(ProtoBufMixin, models.Model):
    pb_model = proto.XREvent
    pb_2_dj_fields = '__all__'

class FDS(ProtoBufMixin, models.Model):
    pb_model = proto.FDS
    pb_2_dj_fields = '__all__'

class Evaluation(ProtoBufMixin, models.Model):
    pb_model = proto.Evaluation
    pb_2_dj_fields = '__all__'

class EvaluationAction(ProtoBufMixin, models.Model):
    pb_model = proto.EvaluationAction
    pb_2_dj_fields = '__all__'

class SeparatedScenario(ProtoBufMixin, models.Model):
    pb_model = proto.SeparatedScenario
    pb_2_dj_fields = '__all__'

class CombinedScenario(ProtoBufMixin, models.Model):
    pb_model = proto.CombinedScenario
    pb_2_dj_fields = '__all__'

MULTIUSE_FACILITY = 'MultiUseFacility'
COMPLEX_FACILITY = 'ComplexFacility'
ELDERLY_FACILITY = 'ElderlyFacility'
UNDERGROUND_FACILITY = 'UndergroundFacility'

FACILITY_CHOICES = [
    (MULTIUSE_FACILITY, 'MultiUseFacility'),
    (COMPLEX_FACILITY, 'ComplexFacility'),
    (ELDERLY_FACILITY, 'ElderlyFacility'),
    (UNDERGROUND_FACILITY, 'UndergroundFacility')
]

INTERACTION_AREA_CHOICES = [
    ('move_floor', 'move_floor'),
    ('floor', 'floor'),
    ('area', 'area')
]

class Transform3D(models.Model):
    PositionX = models.FloatField()
    PositionY = models.FloatField()
    PositionZ = models.FloatField()
    RotationX = models.FloatField()
    RotationY = models.FloatField()
    RotationZ = models.FloatField()


class InteractionArea(models.Model):
    # ID = models.IntegerField(primary_key=True, auto_created=True, editable=False, unique=True)
    # ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    Created = models.DateTimeField(auto_now_add=True)
    Name = models.CharField(max_length=40)
    Facility = models.CharField(choices=FACILITY_CHOICES, default='MultiUseFacility', max_length=25)
    Type = models.CharField(choices=INTERACTION_AREA_CHOICES, default='area', max_length=20)
    Transform = models.ForeignKey(Transform3D, related_name='Transform', on_delete=models.SET_NULL, null=True)
    Collider_Size_X = models.FloatField(default=0.0)
    Collider_Size_Y = models.FloatField(default=0.0)
    Collider_Size_Z = models.FloatField(default=0.0)
    Next1 = models.ForeignKey(Transform3D, related_name='Next1', on_delete=models.SET_NULL, null=True)
    Next2 = models.ForeignKey(Transform3D, related_name='Next2', on_delete=models.SET_NULL, null=True)

    # Pox_X = models.FloatField()
    # Pox_Y = models.FloatField()
    # Pox_Z = models.FloatField()
    # Rot_X = models.FloatField()
    # Rot_Y = models.FloatField()
    # Rot_Z = models.FloatField()
    # Collider_Size_X = models.FloatField()
    # Collider_Size_Y = models.FloatField()
    # Collider_Size_Z = models.FloatField()
    # Next1_Pox_X = models.FloatField()
    # Next1_Pox_Y = models.FloatField()
    # Next1_Pox_Z = models.FloatField()
    # Next1_Rot_X = models.FloatField()
    # Next1_Rot_Y = models.FloatField()
    # Next1_Rot_Z = models.FloatField()
    # Next2_Pox_X = models.FloatField()
    # Next2_Pox_Y = models.FloatField()
    # Next2_Pox_Z = models.FloatField()
    # Next2_Rot_X = models.FloatField()
    # Next2_Rot_Y = models.FloatField()
    # Next2_Rot_Z = models.FloatField()


# class Schedule(models.Model):
#     title = models.CharField(max_length=30)
#     color = ColorField(default='#FFFFFF', format='hexa')
#     description = models.CharField(max_length=100)
#     scheduledDate = models.DateField()
    
#     def __str__(self):
#         return self.title