# Generated by Django 2.1.7 on 2019-10-04 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0006_auto_20191004_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packageuserrelation',
            name='passed',
        ),
    ]