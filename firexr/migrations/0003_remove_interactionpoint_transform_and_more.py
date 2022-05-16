# Generated by Django 4.0.4 on 2022-05-16 02:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firexr', '0002_alter_interactionpoint_transform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interactionpoint',
            name='Transform',
        ),
        migrations.AddField(
            model_name='interactionpoint',
            name='LocalTransform',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transformposes', to='firexr.transform'),
        ),
    ]