# Generated by Django 4.0.5 on 2022-06-04 15:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dossiermedical',
            name='dateCreation',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 6, 4, 16, 50, 16, 468887)),
        ),
        migrations.AlterField(
            model_name='rendezvous',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 4, 16, 50, 16, 466890)),
        ),
    ]
