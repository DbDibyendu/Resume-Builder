# Generated by Django 3.1.7 on 2021-05-12 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20210509_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='pj1_link',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='pj2_link',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='pj3_link',
            field=models.CharField(max_length=100, null=True),
        ),
    ]