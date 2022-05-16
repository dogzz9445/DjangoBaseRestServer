# Generated by Django 4.0.4 on 2022-05-16 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firexr', '0003_remove_interactionpoint_transform_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interactionpoint',
            name='LocalTransform',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transformposes', to='firexr.transform'),
        ),
    ]