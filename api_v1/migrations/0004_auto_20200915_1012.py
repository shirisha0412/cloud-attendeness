# Generated by Django 3.1.1 on 2020-09-15 02:12

import api_v1.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0003_auto_20200913_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='studentId',
            field=models.CharField(default=api_v1.models.generateUUID, editable=False, max_length=200, primary_key=True, serialize=False),
        ),
    ]
