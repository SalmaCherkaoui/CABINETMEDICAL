# Generated by Django 4.0.5 on 2022-06-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet', '0010_alter_rendezvous_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rendezvous',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
