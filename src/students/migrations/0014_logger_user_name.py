# Generated by Django 2.2.9 on 2020-02-04 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0013_auto_20200204_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='logger',
            name='user_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
