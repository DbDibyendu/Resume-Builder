# Generated by Django 3.1.7 on 2021-05-08 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210508_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='other_info',
        ),
    ]
