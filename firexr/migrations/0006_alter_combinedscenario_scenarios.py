# Generated by Django 4.0.4 on 2022-05-12 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firexr', '0005_alter_combinedscenario_scenarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combinedscenario',
            name='Scenarios',
            field=models.ManyToManyField(blank=True, related_name='combined_scenario', to='firexr.separatedscenario'),
        ),
    ]