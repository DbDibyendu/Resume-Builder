# Generated by Django 3.1.7 on 2021-05-09 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_info_exp1_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='exp2_info',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='exp3_info',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='pg1_info',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='pg2_info',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='pg3_info',
            field=models.TextField(max_length=10000, null=True),
        ),
    ]
