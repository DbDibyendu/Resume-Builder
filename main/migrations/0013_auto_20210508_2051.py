# Generated by Django 3.1.7 on 2021-05-08 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210508_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='Hobbie',
            new_name='Hobbies',
        ),
    ]