# Generated by Django 3.1.7 on 2021-05-06 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_personal_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal',
            name='user',
        ),
    ]