from django.db import models
from colorfield.fields import ColorField

# Create your models here.
class Schedule(models.Model):
    title = models.CharField(max_length=30)
    color = ColorField(default='#FFFFFF', format='hexa')
    description = models.CharField(max_length=100)
    scheduledDate = models.DateField()
    
    def __str__(self):
        return self.title