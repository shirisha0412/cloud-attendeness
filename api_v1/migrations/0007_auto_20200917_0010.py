# Generated by Django 2.2 on 2020-09-16 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0006_auto_20200915_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='lectureDate',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='subjectCode',
            field=models.CharField(max_length=200),
        ),
    ]
