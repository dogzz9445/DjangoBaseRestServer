# Generated by Django 4.0.4 on 2022-05-02 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenario', '0007_remove_interactionarea_id_interactionarea_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InteractionArea',
        ),
    ]