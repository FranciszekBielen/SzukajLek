# Generated by Django 3.2 on 2021-05-29 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchEngine', '0003_auto_20210529_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rowa',
            name='substance_name',
        ),
        migrations.DeleteModel(
            name='ActiveSubstanceName',
        ),
    ]
