# Generated by Django 2.2.9 on 2020-01-27 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20200122_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='telephone',
            field=models.CharField(blank=True, max_length=16, null=True, unique=True),
        ),
    ]
