# Generated by Django 4.0.4 on 2022-05-13 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firexr', '0006_alter_combinedscenario_scenarios'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evaluation',
            old_name='Name',
            new_name='Action',
        ),
        migrations.RenameField(
            model_name='evaluationaction',
            old_name='Name',
            new_name='Action',
        ),
        migrations.AddField(
            model_name='evaluation',
            name='Category',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='Contents',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='Desc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='EvaluationActions',
            field=models.ManyToManyField(blank=True, to='firexr.evaluationaction'),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='Score',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='Type',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='Weight',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='evaluationaction',
            name='Desc',
            field=models.TextField(null=True),
        ),
    ]
