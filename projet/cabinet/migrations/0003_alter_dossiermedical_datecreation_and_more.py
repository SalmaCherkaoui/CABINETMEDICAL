# Generated by Django 4.0.5 on 2022-06-04 15:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0002_alter_dossiermedical_datecreation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dossiermedical',
            name='dateCreation',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 4, 16, 52, 2, 270400), null=True),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 4, 16, 52, 2, 269401)),
        ),
    ]
